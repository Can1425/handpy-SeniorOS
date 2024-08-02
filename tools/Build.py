# 针对FlagOS的构建工具

import shutil,os

# 配置部分初始化
try:
    from BuildConfig import *
except:
    # 释放文件BuildCfg
    with open("./BuildConfig.py",'wb')as f:f.write(__import__('zlib').decompress(b'x\x9cM\x8f]K\xc2`\x18\x86\xcf\xf7+\xc6<)(\xb5S\xc1\xa3<\x95\x02;\x1fK_\xdd"6\xd9^\x83\x08C\xd3L1[\xa0&\xf8A\nR\x16\xe5\x8c>\xdc\xec\xc3?\xb3\xe7\xd1\xfd\x8bf\x12\xf8\x1c_\xf7}_\x8f\x87\x85\xef*\x94*N\xcf\x9a\xb5\x86\xf6g\x15&\xd5Y3?\x1f\x1b\xf0\x93g\x92\xaar@\xa2tW\xa0b\x90;\xf5\x89\x82\x1cK\x1eoF\x88,)\xeaN\xc4\xc71\x8c\x87\x05\xc3\x82I-N\x04\x9aRI D\xf6S\x890\xd14!A\xd8\xf9(77\xea\xf6\xb4\x87Y\xc3%\xf1\xb9\x0f\xfd<\xe8\x86\x93)a\xf9a\x19t\xda\x99\xf9]\x16\xbe2pm\xac\xf2\xae\x04\x0ez\xd0i,&t\xc3\x9ev\xf02\x0bW\xb7\xd8\x1d3\xb1\x95\x91\xe0\t\xc3\xba\xc7m+*\xf1\x86\x04*lS\xf5\xd0\xcb\xf3\x92,Q\x9e\xe7\x02{j\x8a0\xe9?Q\xd3t.t\xac\x8f\xb02d\xa1\x7f\xef\xe4\x06P,`\xee\x1c\n\xef\xb6Y\xb6\xcd\xca\xd2\x05[oX\xb3\x98\xa8"ktQ\xf8\xbf\xa0EUBdMTh\x98PQ\x89q\x01..h\x94\xdb`\xdd\xd7\x8a\x8f\xf0\xa2/\x85\xf1\xc6\xc2\xd7\xfa2sDTMRd\x17\xdd\xf2\xfa\xbd~\xceEg\xa5"\xb6\x9f@\x1f\xafa\xf3\x0c\x1b\x1f\xd8\xe8\xcej\x83u&\xfd\x0b\xd7k\xc8\x12'))
    raise OSError("请先配置 BuildConfig.py")
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