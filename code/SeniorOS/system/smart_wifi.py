'''
  ___ _         _       ___                _ __      ___  __ _ 
 / __| |__ _ __| |__   / __|_ __  __ _ _ _| |\ \    / (_)/ _(_)
 \__ \ / _` / _| / /   \__ \ '  \/ _` | '_|  _\ \/\/ /| |  _| |
 |___/_\__,_\__|_\_\   |___/_|_|_\__,_|_|  \__|\_/\_/ |_|_| |_|

 Copyright 2024 CycleBai, All rights reserved

import SeniorOS.system.log_manager as LogManager
import network
import socket
import ure
import time
import _thread

# 配置 AP 模式
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32_Config', authmode=network.AUTH_WPA_WPA2_PSK, password='12345678')
ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))

# HTML 页面模板
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>ESP32 配置门户</title>
</head>
<body>
    <h1>ESP32 配置门户</h1>
    <form action="/wifi" method="post">
        <label for="ssid">SSID:</label><br>
        <select id="ssid" name="ssid">
            {options}
        </select><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="提交">
    </form>
</body>
</html>
"""

# 扫描 Wi-Fi 网络
def scan_wifi():
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    networks = sta.scan()
    options = ""
    for net in networks:
        ssid = net[0].decode('utf-8')
        options += f'<option value="{ssid}">{ssid}</option>'
    return options

# 启动 DNS 服务器
def start_dns_server():
    dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dns.bind(('0.0.0.0', 53))
    while True:
        try:
            data, addr = dns.recvfrom(1024)
            dns.sendto(data[:2] + b'\x81\x80' + data[4:6] * 2 + b'\x00\x00\x00\x00', addr)
            qname_end = 12
            while data[qname_end] != 0:
                qname_end += 1
            qname_end += 5
            dns.sendto(data[:2] + b'\x81\x80' + data[4:6] * 2 + b'\x00\x00\x00\x00' + data[12:qname_end] + b'\xc0\x0c' + b'\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04\xc0\xa8\x04\x01', addr)
        except OSError as error:
            LogManager.Output('DNS 服务器错误:' + error, "ERROR")

# 启动 Web 服务器
def start_web_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    LogManager.Output('正在监听连接', "INFO")
    while True:
        try:
            cl, addr = s.accept()
            LogManager.Output('客户端连接自 ' + addr, "INFO")
            cl_file = cl.makefile('rwb', 0)
            line = cl_file.readline()
            response = "未定义页面"
            if line:
                while True:
                    line = cl_file.readline()
                    if not line or line == b'\r\n':
                        break
                if b'GET / ' in line:
                    response = HTML_TEMPLATE.format(options=scan_wifi())
                elif b'POST /wifi ' in line:
                    length = 0
                    while True:
                        header = cl_file.readline()
                        if not header or header == b'\r\n':
                            break
                        m = ure.match(b"Content-Length: (\d+)", header)
                        if m:
                            length = int(m.group(1))
                    body = cl_file.read(length)
                    params = {}
                    for param in body.decode().split('&'):
                        k, v = param.split('=')
                        params[k] = v
                    ssid = params.get('ssid', '')
                    password = params.get('password', '')
                    connect_to_wifi(ssid, password)
                    response = "连接中，请等待..."
            cl.send('HTTP/1.1 200 OK\r\n')
            cl.send('Content-Type: text/html\r\n')
            cl.send('Connection: close\r\n\r\n')
            cl.sendall(response.encode('utf-8'))
        except OSError as e:
            pass
            #print('Web 服务器错误:', e)
        finally:
            cl.close()

# 连接到 Wi-Fi 网络
def connect_to_wifi(ssid, password):
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(ssid, password)
    timeout = 10
    while not sta.isconnected() and timeout > 0:
        LogManager.Output("Connection WiFi", "INFO")
        time.sleep(1)
        timeout -= 1
    if sta.isconnected():
        LogManager.Output('WiFi Connection Successful', "INFO")
    else:
        LogManager.Output("Timeout!,check your wifi password and keep your network unblocked", "Error")
'''
import network
import socket
import gc
import time
responseHeaders=b"""
HTTP/1.1 200 OK
Content-Type: text/html
Connection: close
"""

HTML=b"""
<!DOCTYPE html>
<html>
<head>
    <title>ESP32 Web Server</title>
</head>
<body>
    <p>192.168.4.1/ssid:WiFi name</p>
    <p>192.168.4.1/pwd:WiFi password</p>
    <a href="exit" target="top">exit</a>
</body>
"""
#报错了把这个打开就行
'''
class wifi:
    def __init__(self):
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)

    def connectWiFi(self, ssid, passwd, timeout=10):
        if self.sta.isconnected():
            self.sta.disconnect()
        self.sta.active(True)
        list = self.sta.scan()
        for i, wifi_info in enumerate(list):
            try:
                if wifi_info[0].decode() == ssid:
                    self.sta.connect(ssid, passwd)
                    wifi_dbm = wifi_info[3]
                    break
            except UnicodeError:
                self.sta.connect(ssid, passwd)
                wifi_dbm = '?'
                break
            if i == len(list) - 1:
                print("SSID invalid / failed to scan this wifi", "ERROR")
        start = time.time()
        print("Connection WiFi", "INFO")
        while (self.sta.ifconfig()[0] == '0.0.0.0'):
            if time.ticks_diff(time.time(), start) > timeout:
                print("")
                print("Timeout!,check your wifi password and keep your network unblocked", "Error")
            print(".", end="")
            time.sleep_ms(500)
        print("")
        print('WiFi(%s,%sdBm) Connection Successful, Config:%s' % (ssid, str(wifi_dbm), str(self.sta.ifconfig())), "INFO")
'''
ap = network.WLAN(network.AP_IF)
ap.config(essid='SeniorOS-WIFI', authmode=4, password='12345678')
ap.active(True)

import SeniorOS.system.daylight as DayLight
from SeniorOS.system.devlib import *
import SeniorOS.system.log_manager as LogManager

def connectWIFI(ssid,pwd):
    global ap
    ap.active(False)
    del ap
    gc.collect()
    sta=wifi()
    sta.connectWiFi(ssid,pwd)
def main():
    DayLight.App.Style1("高级 WIFI 配置")
    DayLight.Text('请连接以完成配置', 5, 18, 2)
    DayLight.Text('WIFIName:SeniorOS-WIFI', 5, 36, 2)
    DayLight.Text('WIFIPassWord:123456', 5, 54, 2)
    oled.show()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(socket.getaddrinfo("0.0.0.0", 80)[0][-1])
    s.listen(5)
    LogManager.Output('接入热点后可从浏览器访问下面地址:' + ap.ifconfig()[0], 'MSG')
    ssid="";pwd=""
    while True:
        client_sock, client_addr = s.accept()
        print('Client address:', client_addr)
        q=''
        while True:
            h = client_sock.readline()
            q += h.decode('utf8')
            if h == b'' or h == b'\r\n':
                break
        if q.startswith('GET / HTTP/1.1'):
            client_sock.write(HTML)
        elif q.startswith('GET /ssid:'):
            q=q.split("/")[1]
            q=q[:-5]
            q=q.split(":")[1]
            print(q)
            ssid=q
            client_sock.write('get')
        elif q.startswith('GET /pwd'):
            q=q.split("/")[1]
            q=q[:-5]
            q=q.split(":")[1]
            #print(q)
            pwd=q
            client_sock.write('get')
        elif q.startswith("GET /exit"):
            connectWIFI(ssid,pwd)
            break
        else:
            pass
        client_sock.write(responseHeaders)
        client_sock.write(HTML)
        client_sock.close()
    return(ssid,pwd)

#main()#运行