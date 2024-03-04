# 针对FlagOS的构建工具
from ReplaceExpression import ReplaceExpr
import shutil,os

codeDir="./code/"
buildDir="./build/"

codeFile=[
    "Flag_OS/system/core.py",
    "Flag_OS/system/main.py",
    "Flag_OS/system/ui.py",
    "Flag_OS/system/pages.py",
    "Flag_OS/fonts/quantum.py",
    "Flag_OS/system/update.py",
    "boot.py"
]
# TODO:实现自动生成目录树 无需手动提供文件位置
# TODO:未测试
def treeDir(dir):
    for i in os.listdir(dir):
        if os.path.isdir(dir+i):
            treeDir(dir+i+"/")
        else:
            #判断是不是py文件
            if i.split(".")[-1]=="py":
                codeFile.append(os.path.join(dir+i))


def Build(codeFile,inputDir,outputDir):
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
    Build(codeFile,codeDir,buildDir)