import uhashlib
# 更新函数

# --SURT--
eval('[/hashtag/]');requests=urequests;os=os
# --SURT--

# lambda: 值查找键
valueFindKey=lambda dictObj,value:{v : k for k, v in dictObj.items()}[value]

SERVER_URL="https://server.ip/port/Flag_OS_UPD/"
SYSTEM_VERSION=eval("[/Const('version')/]")
# 读取本地文件清单
def GetFileList():
    with open("/SeniorOS/data/fileList.json",'rb')as f:
        return f.read().decode()
# 获取更新清单
def GetUpdList():
    global SERVER_URL,SYSTEM_VERSION
    try:
        r=requests.get("{url}/GetUpdList/{sysversion}/{updversion}".format(SERVER_URL,SYSTEM_VERSION,updVersion))
    except OSError as e:
        if e.args[0]==113:
            raise AssertionError("连接超时/路由不可达")
    assert r.status_code == 200 ,"错误的HTTP状态码"
    return r.json()
# 获取最新版本
def GetLatestVer(version):
    global SERVER_URL
    try:
        r=requests.get("{}/LatestVer/version".format(SERVER_URL,version))
    except OSError as e:
        if e.args[0]==113:
            raise AssertionError("连接超时/路由不可达")
    assert r.status_code == 200 ,"错误的HTTP状态码"
    return r.text
# 获取更新文件
def GetUpdFile(fileMd5):
    global SERVER_URL
    try:
        r=requests.get("{}/GetUpdFile/{}".format(SERVER_URL,fileMd5))
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
# 获取本地文件MD5
def GetFileMD5(fileName):
    with open(fileName,'rb') as f:
        data = f.read()
        h = uhashlib.md5(data)
        return h
# 根据对应MD5下载配置文件更新策略并运行    
def UpdCfg(updCfgST_MD5):
    with open("/cfgUpdST.py",'rb')as f:
        f.write(GetUpdFile(updCfgST_MD5))
    os.chdir("/");__import__('cfgUpdST').UpdateST()
# 对比更新清单 返回需要更新的部分
def DiffUpdList(fileList:dict,updList:dict)->dict:
    updList_True={}
    for name,md5 in enumerate(...):
        ... # TODO:完成此处对比模块
            


""" # 因实际需要 会插入一定的UI展示 所以仅作一个例子
def Update():
    updList=GetUpdList()
    UpdFile(updList)
    UpdCfg(updList["cfgUpdST"])
"""