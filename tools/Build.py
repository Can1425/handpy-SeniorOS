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
    "boot.py"
]
# TODO:实现自动生成目录树 无需手动提供文件位置

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
        print(f"MPYC {i}")
        path=outputDir+i
        os.system(f"mpy-cross-v5 {path} -march=xtensawin")
        os.remove(path)

# TODO:设计一个制作安装包的程序
def MakeInstaller():
    pass

if __name__=="__main__":
    Build(codeFile,codeDir,buildDir)