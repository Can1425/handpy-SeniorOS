import SeniorOS.system.log_manager as LogManager
Log = LogManager.Log
LogManager.Output("system/main.mpy", "INFO")
import uos as os;os.chdir('/')
import SeniorOS.system.pages as Pages
import SeniorOS.system.core as Core
import SeniorOS.system.smart_wifi as SmartWifi
from SeniorOS.system.devlib import wifi
import _thread
import ntptime
import gc
info=Core.Data.Get("text","connectWifiMode")
wifilist=[]
if info == "0":
    Pages.WifiPages()
elif info == "1":
    wifilist=[Core.Data.Get("list","wifiName"),Core.Data.Get("list","wifiPassword")]
    net=wifi()
    net.sta.active(True)
    netscan=net.sta.scan()
    def GetWifiCfg(num):
        return str(netscan[num][0].decode('utf-8')).replace("\r","")
    connect=False
    for i in wifilist[0]:
        for j in range(len(netscan)):
            if connect:break
            if str(i)==GetWifiCfg(j):
                try:
                    net.connectWiFi(wifilist[0][i],wifilist[1][i])
                    ntptime.settime(8,"time.windows.com")
                    connect=True
                except:
                    Log.Error("CONNECT WIFI FILLED")
                    Log.Message("USE SMARTWIFI NOW")
                    SmartWifi.main()
    del wifilist,net,netscan,connect;gc.collect()
elif info == "2":
    # 启动门户
    SmartWifi.main()
del info;gc.collect()
#-----------------
def _____():
    while True:gc.collect()
_thread.start_new_thread(_____,())
returnData=Pages.Home()
while not returnData:
    returnData=Pages.Home()