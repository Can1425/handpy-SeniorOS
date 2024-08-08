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
    <a href="exit" target="top">Click to exit and connect WIFI</a>
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