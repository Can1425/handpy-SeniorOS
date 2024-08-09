import os
import shutil
import urllib.request
import logging
from git import Repo  # GitPython
from ReplaceExpression import ReplaceExpr  # 确保导入ReplaceExpr

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# 自动切换到父目录
def change_working_directory():
    current_dir = os.path.abspath(os.getcwd())
    if current_dir.endswith('tools'):
        new_dir = os.path.abspath(os.path.join(current_dir, '..'))
        logging.info(f"当前工作目录以 'tools' 结尾，切换到父目录: {new_dir}")
        os.chdir(new_dir)

# 首先确保 BuildConfig.py 已下载
def ensure_build_config():
    url = "https://raw.githubusercontent.com/Can1425/handpy-SeniorOS/Alpha/tools/BuildConfig.py"
    save_path = "BuildConfig.py"
    if not os.path.exists(save_path):
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
    const_data = {
        "branch": project_repo.active_branch.name,
        "fullCommitID": project_repo.head.object.hexsha,
        "commitID": project_repo.head.object.hexsha[:7]
    }
    return const_data

# 遍历目录获取Python文件列表
def tree_dir(directory):
    return [
        os.path.join(root, file).strip('./code/')
        for root, dirs, files in os.walk(directory)
        for file in files if file.endswith(".py")
    ]

# 构建功能
def build_project(code_files, input_dir, output_dir):
    logging.info("\n" + "=" * 40 + "\n" + " FlagOS 构建工具 ".center(40) + "\n" + "=" * 40 + "\n")

    # 清理输出目录
    shutil.rmtree(output_dir, ignore_errors=True)
    shutil.copytree(input_dir, output_dir)

    # 替换表达式
    for file in code_files:
        logging.info(f"EXPR {file}")
        ReplaceExpr(os.path.join(output_dir, file))

    # 编译文件
    for file in code_files:
        if file == "boot.py":
            continue
        logging.info(f"MPYC {file}")
        file_path = os.path.join(output_dir, file)
        os.system(f"mpy-cross-v5 {file_path} -march=xtensawin")
        os.remove(file_path)

if __name__ == "__main__":
    # 获取项目路径并初始化Git数据
    project_path = './'
    const_data = initialize_git_data(project_path)

    # 构建项目
    code_files = tree_dir('./code/')
    build_project(code_files, './code/', './build/')
