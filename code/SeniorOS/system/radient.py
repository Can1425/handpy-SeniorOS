import socket
#实现HTTP协议的GET
def NormalGet(url,timeout=2):
    #解析url
    url_parse = url.split('/')
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
    status_code, body = ParseResponse(response)
    return status_code, body
    # [0]是状态码 , [1]是响应体 , 建议放变量里面