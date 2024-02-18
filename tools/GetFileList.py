# 对path下的所有文件扫描并生成目录树
import os,hashlib
def ScanFile(path):
    tree = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            tree.append(file_path)
    return tree
def GetMD5(path:list)->list:
    md5List=[]
    for i in path:
        with open(i,'rb')as f:fileData=f.read()
        md5List.append(hashlib.md5(fileData).hexdigest())
    return md5List

# 没啥修改 给Build.py定制的.
def GetMD5List(path):
    tree=ScanFile(input(path))
    md5List=GetMD5(tree)
    return dict(zip(tree,md5List))

if __name__=="__main__":
    tree=ScanFile(input("给个路径\n"))
    md5List=GetMD5(tree)
    print(dict(zip(tree,md5List)))