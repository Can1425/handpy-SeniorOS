import uhashlib,os,urequests
import SeniorOS.system.log_manager as LogManager
LogManager.Output("system/update.mpy", "INFO")
import ubinascii
# lambda: 值查找键
valueFindKey=lambda dictObj,value:{v : k for k, v in dictObj.items()}[value]

SERVER_URL="https://senior.flowecho.org/update"
SYSTEM_VERSION=eval("[/Const('version')/]")
# 读取本地文件清单
def GetFileList():
    with open("/SeniorOS/data/fileList.json",'rb')as f:
        return f.read().decode()
# 快速hash By CodeGeeX
def ReadChunk(c,bytes=4096):
    return c.read(bytes)
def hexdigest(digest):
    return ubinascii.hexlify(digest)

def FastHash(file_path, hash_type=uhashlib.md5):
    hash_obj = hash_type()
    with open(file_path, 'rb') as f:
        hash_obj.update(f.read())
    return hexdigest(hash_obj.digest())

# 获取更新清单
def GetUpdList(updVersion):
    global SERVER_URL,SYSTEM_VERSION
    try:
        r=urequests.get("{url}/GetUpdList/{sysversion}/{updversion}".format(SERVER_URL,SYSTEM_VERSION,updVersion))
    except OSError as e:
        if e.args[0]==113:
            raise AssertionError("连接超时/路由不可达")
    assert r.status_code == 200 ,"错误的HTTP状态码"
    return r.json()
# 获取最新版本
def GetLatestVer():
    global SERVER_URL
    try:
        r=urequests.get("{}/LatestVer/version".format(SERVER_URL))
    except OSError as e:
        if e.args[0]==113:
            raise AssertionError("连接超时/路由不可达")
    assert r.status_code == 200 ,"错误的HTTP状态码"
    return r.text
# 获取更新文件
def GetUpdFile(fileMd5):
    global SERVER_URL
    try:
        r=urequests.get("{}/GetUpdFile/{}".format(SERVER_URL,fileMd5))
    except OSError as e:
        if e.args[0]==113:
            raise AssertionError("连接超时/路由不可达")
    assert r.status_code == 200 ,"错误的HTTP状态码"
    return r.content
# 根据更新清单下载并获取文件
def UpdFile(updList):
    for i in updList:       # 这里的updList对应GetUpdList的返回值的["updateList"]
        with open(i["filePath"],'wb') as f:
            f.write(GetUpdFile(i["fileMd5"]))
# 根据对应MD5下载配置文件更新策略并运行    
def UpdCfg(updCfgST_MD5):
    with open("/cfgUpdST.py",'rb')as f:
        f.write(GetUpdFile(updCfgST_MD5))
    os.chdir("/");__import__('cfgUpdST').UpdateST()
# 对比更新清单 返回需要更新的部分 By CGPT
# https://chat.openai.com/share/f59bd4e3-ff2f-426a-b13d-4f2af52502b3
def DiffDict(oldData, newData):
    oldKeys = set(oldData.keys())
    newKeys = set(newData.keys())
    added_or_modified = {key: newData[key] for key in newKeys if key not in oldKeys or newData[key] != oldData[key]}
    removed = {key: oldData[key] for key in oldKeys if key not in newKeys}
    return added_or_modified, removed
def DiffUpdList(fileList:dict,updList:dict)->dict:
    needUpdData,needRmData=DiffDict(fileList,updList)
    updFile=[]
    updDir=[]
    rmFile=[]
    rmDir=[]
    for k, v in needUpdData.items():
        if k == "dir":
            for i in v:updDir.append(i)
        else:
            updFile.append({k:v})
    for k, v in needRmData.items():
        if k == "dir":
            for i in v:rmDir.append(i)
        else:
            rmFile.append({k:v})

    return updFile,updDir,rmFile,rmDir

# By CodeGeeX
def UpdateST():
    global SERVER_URL,SYSTEM_VERSION
    # 获取本地文件清单
    fileList=GetFileList()
    # 获取更新清单
    updList=GetUpdList()
    # 对比更新清单 返回需要更新的部分
    updFile,updDir,rmFile,rmDir=DiffUpdList(eval(fileList),updList)
    # 下载并获取文件
    UpdFile(updFile)
    # 更新文件夹
    for i in updDir:
        try:os.mkdir(i)
        except:pass
    # 删除文件
    for i in rmFile:
        os.remove(i["filePath"])
    # 删除文件夹
    for i in rmDir:
        try:os.rmdir(i)
        except:pass
    # 更新配置文件
    UpdCfg(updList["cfgUpdST"])