import network
import socket
import gc
import time
import SeniorOS.system.log_manager as LogManager
Log = LogManager.Log
responseHeaders=b"""
HTTP/1.1 200 OK
Content-Type: text/html
Connection: close
"""

HTML=b'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SeniorOS WiFi Configuration</title>
    <style>
        body { font-family: sans-serif; background: #f5f5f7; margin: 0; padding: 100px; color: #333; }
        .form-container { max-width: 400px; margin: 40px auto; background: #fff; padding: 20px; box-shadow: 0 8px 16px rgba(0,0,0,.2); border-radius: 19px; }
        input[type="text"], input[type="submit"] { width: calc(100% - 22px); padding: 10px; margin: 10px 0; border: 1px solid #d9d9d9; border-radius: 10px; font-size: 16px; }
        input[type="submit"] { background: #007aff; color: white; cursor: pointer; }
        input[type="submit"]:hover { background: #006ae3; }
        a { display: inline-block; padding: 10px 15px; background: #ff3b30; color: white; text-decoration: none; border-radius: 25px; font-size: 16px; }
        a:hover { background: #e6332e; }
    </style>
</head>
<body>
    <div class="form-container">
        <form action="http://192.168.4.1" method="get">
            <label for="ssid">WiFiSSID</label>
            <input type="text" id="ssid" name="ssid" placeholder="Type your wifiSSID">
            <input type="submit" value="Upload">
        </form>
        <form action="http://192.168.4.1" method="get">
            <label for="pwd">WifiPassword</label>
            <input type="text" id="pwd" name="pwd" placeholder="Type your wifiPassword">
            <input type="submit" value="Upload">
        </form>
        <a href="http://192.168.4.1/exit">Exit</a>
    </div>
</body>
</html>
'''
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
#'''
ap = network.WLAN(network.AP_IF)
ap.config(essid='SeniorOS-WIFI', authmode=4, password='12345678')
ap.active(True)



def connectWIFI(ssid,pwd):
    global ap
    ap.active(False)
    del ap
    gc.collect()
    sta=wifi()
    sta.connectWiFi(ssid,pwd)
def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(socket.getaddrinfo("0.0.0.0", 80)[0][-1])
    s.listen(5)
    Log.Info(ap.ifconfig()[0])
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
        elif q.startswith('GET /?ssid='):
            q=q.split("/")[1]
            q=q[:-5]
            q=q.split("=")[1]
            print(q)
            ssid=q
            client_sock.write('get')
        elif q.startswith('GET /?pwd='):
            q=q.split("/")[1]
            q=q[:-5]
            q=q.split("=")[1]
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