import os
import shutil
import urllib.request
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from git import Repo
from ReplaceExpression import ReplaceExpr  # Ensure ReplaceExpr is imported

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 只记录INFO及以上级别的日志
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# 自动切换到父目录
def change_working_directory():
    current_dir = Path.cwd()
    if current_dir.name == 'tools':
        new_dir = current_dir.parent
        logging.info(f"当前工作目录以 'tools' 结尾，切换到父目录: {new_dir}")
        os.chdir(new_dir)

# 确保 BuildConfig.py 已下载
def ensure_build_config():
    tools_dir = Path("tools")
    tools_dir.mkdir(parents=True, exist_ok=True)  # 确保 tools/ 目录存在
    url = "https://raw.githubusercontent.com/Can1425/handpy-SeniorOS/Alpha/tools/BuildConfig.py"
    save_path = tools_dir / "BuildConfig.py"
    if not save_path.exists():
        logging.info("BuildConfig.py 不存在，正在下载...")
        urllib.request.urlretrieve(url, save_path)
        logging.info("BuildConfig.py 下载完成。")

# 确保 BuildConfig.py 已存在
change_working_directory()  # 确保在任何其他操作之前切换工作目录
ensure_build_config()

# 然后再导入所需模块
from BuildConfig import *

# 初始化Git仓库数据
def initialize_git_data(project_path):
    project_repo = Repo(project_path)
    return {
        "branch": project_repo.active_branch.name,
        "fullCommitID": project_repo.head.object.hexsha,
        "commitID": project_repo.head.object.hexsha[:7]
    }

# 遍历目录获取Python文件列表
def tree_dir(directory):
    return [str(file.relative_to(directory)) for file in Path(directory).rglob("*.py")]

# 替换表达式
def replace_expression(file):
    logging.debug(f"处理文件：{file}")  # 将文件处理日志级别设置为DEBUG
    ReplaceExpr(file)

# 编译文件
def compile_file(file_path):
    if Path(file_path).name == "boot.py":
        return
    logging.debug(f"编译文件：{file_path}")  # 将文件处理日志级别设置为DEBUG
    os.system(f"mpy-cross-v5 {file_path} -march=xtensawin")
    os.remove(file_path)

def build_project(code_files, input_dir, output_dir):
    logging.info("\n" + "=" * 40 + "\n" + " FlagOS 构建工具 ".center(40) + "\n" + "=" * 40 + "\n")

    start_time = time.time()

    # 清理输出目录
    output_path = Path(output_dir)
    if output_path.exists():
        shutil.rmtree(output_path)
    shutil.copytree(input_dir, output_path)

    # Multi-threaded expression replacement
    replace_start_time = time.time()
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        # 使用 map 函数批量处理替换任务
        list(executor.map(replace_expression, (output_path / file for file in code_files)))
        
    replace_duration = time.time() - replace_start_time
    logging.info(f"表达式替换耗时 {replace_duration:.2f} 秒")

    # Multi-threaded file compilation
    compile_start_time = time.time()
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        # 使用 map 函数批量处理编译任务
        list(executor.map(compile_file, (output_path / file for file in code_files)))

    compile_duration = time.time() - compile_start_time
    logging.info(f"文件编译耗时 {compile_duration:.2f} 秒")

    total_duration = time.time() - start_time
    logging.info(f"整个构建过程耗时 {total_duration:.2f} 秒")

if __name__ == "__main__":
    # 获取项目路径并初始化Git数据
    project_path = Path('./')
    const_data = initialize_git_data(project_path)

    # 构建项目
    code_files = tree_dir('./code/')
    build_project(code_files, './code/', './build/')
