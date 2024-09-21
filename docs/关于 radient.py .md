# radient.py --- 网络http通讯库

## 何为radient?
radient 是一个基于 **tcp**和**micropython**的网络请求库,适用于micropython设备,如esp8266,esp32等

radient 的通讯协议基于http 1.1,因此radient可以发送http请求,也可以接收http请求

## 如何使用radient?

### 1. 通讯函数
radient 提供了Get()函数用来发送http请求

#### 参数
1- Get(url,timeout=2)
url: 请求的url
timeout: 请求超时时间,默认为2秒

#### 返回值
返回一个元组,元组的第一个元素是响应状态码,第二个元素是响应内容
example:

```python
import radient
url = "http://www.baidu.com"
timeout = 5
status,content = radient.Get(url,timeout)
print(status,content)
```

### 2. 下载函数
radient 提供了GetToFile()函数用来下载文件

#### 参数
GetToFile(url,file,timeout=2,bufferSize=1024)
url: 请求的url
file: 要写入的文件(必须是文件对象)
timeout: 请求超时时间,默认为2秒
bufferSize: 缓冲区大小,默认为1024字节

#### GetToFile()的优点:
1. 下载大文件时,可以避免内存占用过大
2. 可以实时获取下载进度

#### example:

```python
import radient
url = "http://www.baidu.com"
file = open("baidu.html","wb")
timeout = 5
bufferSize = 1024
radient.GetToFile(url,file,timeout,bufferSize)
file.close()
```
