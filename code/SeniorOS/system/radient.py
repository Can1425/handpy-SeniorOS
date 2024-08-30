# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# SmartWifi - by LP_OVER
import socket
class CodeError(Exception):
    pass
def NormalGet(url,timeout=2):
    #解析url
    print("访问:"+url)
    url_parse = url.split('/')
    print("目标"+url_parse[2])
    host = url_parse[2]
    path = '/'
    if len(url_parse) > 3:
        path = '/' + '/'.join(url_parse[3:])
    #创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #连接服务器
    s.connect((host, 80))
    s.settimeout(timeout)
    #发送请求
    request = 'GET {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(path, host)
    s.send(request.encode())
    #接收响应
    response = b''
    while True:
        try:data = s.recv(1024)
        except:break
        if data == b"" and len(response)>0:break
        response += data
    #关闭socket
    s.close()
    #返回响应
    return response.decode()

#解析返回的数据
def ParseResponse(response):
    #解析响应头
    response_parse = response.split('\r\n\r\n')
    headers = response_parse[0].split('\r\n')
    status_line = headers[0].split(' ')
    status_code = status_line[1]
    #解析响应体
    body = response_parse[1]
    return status_code, body
def Get(url, timeout=2):
    response = NormalGet(url, timeout)
    print(repr(response))
    status_code, body = ParseResponse(response)
    if status_code == "308" or status_code == "301" or status_code == "302":
        print("重定向找我干嘛")
        redirect_data = body.split('\r\n')
        redirect_item = ""
        for i in redirect_data:
            if i.startswith('Location:'):redirect_item = i[10:]
        print("返回数据:"+str(redirect_item))
        print("重定向地址:"+redirect_item)
        Redirect(redirect_item, timeout)
    else:
        CodeError("status_code is {}".format(status_code))
    return status_code, body
    # [0]是状态码 , [1]是响应体 , 建议放变量里面
#实现HTTP的重定向
def Redirect(url, timeout=2):
    response = NormalGet(url, timeout)
    status_code, body = ParseResponse(response)
    if status_code == "308" or status_code == "301" or status_code == "302":
        print("重定向找我干嘛")
        redirect_data = body.split('\r\n')
        redirect_item = ""
        for i in redirect_data:
            if i.startswith('Location:'):redirect_item = i[10:]
        return Redirect(redirect_item, timeout)