# 针对FlagOS的构建工具

import shutil,os

# 配置部分初始化
from BuildConfig import *
from git import Repo # git对应模块->GitPython
projectRepo=Repo(projectPath)
constData["branch"]=projectRepo.active_branch.name
constData["fullCommitID"]=projectRepo.head.object.hexsha
constData["commitID"]=projectRepo.head.object.hexsha[0:7]
os.chdir(projectPath)
codeDir="./code/"
buildDir="./build/"
from ReplaceExpression import *


# 自动生成构建清单
# 需要使用os.walk
def treeDir(dir):
    result=[]
    for root,dirs,files in os.walk(dir):
        for file in files:
            if file.endswith(".py"):
                result.append(os.path.join(root,file).strip(codeDir))
    return result


def Build(codeFile,inputDir,outputDir):
    print("\n")
    print(r"  /$$$$$$                      /$$                      /$$$$$$   /$$$$$$ ")
    print(r" /$$__  $$                    |__/                     /$$__  $$ /$$__  $$")
    print(r"| $$  \__/  /$$$$$$  /$$$$$$$  /$$  /$$$$$$   /$$$$$$ | $$  \ $$| $$  \__/")
    print(r"|  $$$$$$  /$$__  $$| $$__  $$| $$ /$$__  $$ /$$__  $$| $$  | $$|  $$$$$$ ")
    print(r" \____  $$| $$$$$$$$| $$  \ $$| $$| $$  \ $$| $$  \__/| $$  | $$ \____  $$")
    print(r" /$$  \ $$| $$_____/| $$  | $$| $$| $$  | $$| $$      | $$  | $$ /$$  \ $$")
    print(r"|  $$$$$$/|  $$$$$$$| $$  | $$| $$|  $$$$$$/| $$      |  $$$$$$/|  $$$$$$/")
    print(r"  \______/  \_______/|__/  |__/|__/ \______/ |__/       \______/  \______/ ")
    print("\n")
    try:shutil.rmtree(outputDir)
    except:pass
    shutil.copytree(inputDir,outputDir)
    # 替换表达式
    for i in codeFile:
        print(f"EXPR {i}")
        ReplaceExpr(outputDir+i)
    # 编译
    for i in codeFile:
        if i == "boot.py":
            continue
        print(f"MPYC {i}")
        path=outputDir+i
        os.system(f"mpy-cross-v5 {path} -march=xtensawin")
        os.remove(path)


if __name__=="__main__":
    
    Build(treeDir(codeDir),codeDir,buildDir)