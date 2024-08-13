# update.py

## 常量

### `SERVER_URL`

服务器终结点，用于从服务器获取更新文件和更新清单。
<!-- 
这里 `终结点` 我不知道是否准确, 也可以表达为 `端点`?
主要是需要表达出 Endpoint 这个概念
说起来当时谁起的这个名字()
用 SERVER_ENDPOINT 不行吗
 -->

```python
SERVER_URL="https://gitee.com/can1425/mpython-senioros-radient/raw/update"
```

### `SYSTEM_VERSION`

系统版本号，通过评估常量 `'version'` 获取。

```python
SYSTEM_VERSION=eval("[/Const('version')/]")
```

## 函数

### `valueFindKey(dictObj, value)`

根据值查找字典中的键。

```python
valueFindKey=lambda dictObj,value:{v : k for k, v in dictObj.items()}[value]
```

### `GetFileList()`

读取本地文件清单。

```python
def GetFileList():
    with open("/SeniorOS/data/fileList.json",'rb') as f:
        return f.read().decode()
```

### `FastHash(file_path, hash_type=uhashlib.md5)`

快速计算文件的哈希值。

```python
def FastHash(file_path, hash_type=uhashlib.md5):
    hash_obj = hash_type()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()
```

### `GetUpdList(updVersion)`

从服务器获取更新清单。

```python
def GetUpdList(updVersion):
    global SERVER_URL, SYSTEM_VERSION
    try:
        r = urequests.get("{url}/GetUpdList/{sysversion}/{updversion}".format(SERVER_URL, SYSTEM_VERSION, updVersion))
    except OSError as e:
        if e.args[0] == 113:
            raise AssertionError("连接超时/路由不可达")
    assert r.status_code == 200, "错误的HTTP状态码"
    return r.json()
```

### `GetLatestVer()`

获取最新版本号。

```python
def GetLatestVer():
    global SERVER_URL
    try:
        r = urequests.get("{}/LatestVer/version".format(SERVER_URL))
    except OSError as e:
        if e.args[0] == 113:
            raise AssertionError("连接超时/路由不可达")
    assert r.status_code == 200, "错误的HTTP状态码"
    return r.text
```

### `GetUpdFile(fileMd5)`

从服务器获取指定 MD5 的更新文件。

```python
def GetUpdFile(fileMd5):
    global SERVER_URL
    try:
        r = urequests.get("{}/GetUpdFile/{}".format(SERVER_URL, fileMd5))
    except OSError as e:
        if e.args[0] == 113:
            raise AssertionError("连接超时/路由不可达")
    assert r.status_code == 200, "错误的HTTP状态码"
    return r.content
```

### `UpdFile(updList)`

根据更新清单下载并获取文件。

```python
def UpdFile(updList):
    for i in updList:  # 这里的updList对应GetUpdList的返回值的["updateList"]
        with open(i["filePath"], 'wb') as f:
            f.write(GetUpdFile(i["fileMd5"]))
```

### `UpdCfg(updCfgST_MD5)`

根据配置文件 MD5 下载并更新配置文件。

```python
def UpdCfg(updCfgST_MD5):
    with open("/cfgUpdST.py", 'rb') as f:
        f.write(GetUpdFile(updCfgST_MD5))
    os.chdir("/"); __import__('cfgUpdST').UpdateST()
```

### `DiffDict(oldData, newData)`

对比两个字典，返回新增或修改的部分和被删除的部分。

```python
def DiffDict(oldData, newData):
    oldKeys = set(oldData.keys())
    newKeys = set(newData.keys())
    added_or_modified = {key: newData[key] for key in newKeys if key not in oldKeys or newData[key] != oldData[key]}
    removed = {key: oldData[key] for key in oldKeys if key not in newKeys}
    return added_or_modified, removed
```

### `DiffUpdList(fileList: dict, updList: dict) -> dict`

对比文件列表和更新清单，返回需要更新和删除的文件及文件夹。

```python
def DiffUpdList(fileList: dict, updList: dict) -> dict:
    needUpdData, needRmData = DiffDict(fileList, updList)
    updFile = []
    updDir = []
    rmFile = []
    rmDir = []
    for k, v in needUpdData.items():
        if k == "dir":
            for i in v: updDir.append(i)
        else:
            updFile.append({k: v})
    for k, v in needRmData.items():
        if k == "dir":
            for i in v: rmDir.append(i)
        else:
            rmFile.append({k: v})

    return updFile, updDir, rmFile, rmDir
```

### `UpdateST()`

执行系统更新，包括下载更新文件、更新文件夹、删除文件及文件夹，以及更新配置文件。

```python
def UpdateST():
    global SERVER_URL, SYSTEM_VERSION
    # 获取本地文件清单
    fileList = GetFileList()
    # 获取更新清单
    updList = GetUpdList()
    # 对比更新清单 返回需要更新的部分
    updFile, updDir, rmFile, rmDir = DiffUpdList(eval(fileList), updList)
    # 下载并获取文件
    UpdFile(updFile)
    # 更新文件夹
    for i in updDir:
        try: os.mkdir(i)
        except: pass
    # 删除文件
    for i in rmFile:
        os.remove(i["filePath"])
    # 删除文件夹
    for i in rmDir:
        try: os.rmdir(i)
        except: pass
    # 更新配置文件
    UpdCfg(updList["cfgUpdST"])
```
