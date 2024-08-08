import SeniorOS.system.log_manager as LogManager
LogManager.Output("system/main.mpy", "INFO")
import uos as os;os.chdir('/')
import SeniorOS.system.pages as Pages
import SeniorOS.system.core as Core
import SeniorOS.system.smart_wifi as SmartWifi
import _thread
import network
import gc
info=Core.Data.Get("text","connectWifiMode")
wifilist=[]
if info == "0":
    Pages.WifiPages()
elif info == "1":
    wifilist=[Core.Data.Get("list","wifiName"),Core.Data.Get("list","wifiPassword")]
    net=network.WLAN(network.STA_IF)
    net.active(True)
    wlanconfig=net.scan()[0]
    connect=False
    for i in range(len(wifilist[0])):
        for j in wlanconfig:
            if str(j)==wifilist[0][i]:
                connect=Pages.ConfigureWLAN(wifilist[0][i],wifilist[1][i])
                if connect:
                    break
                else:continue
        if connect:
            break
        else:continue
elif info == "2":
    # 启动门户
    SmartWifi.main()
#清理所有变量------
del info, wifilist, net, wlanconfig, connect
#-----------------
def _____():
    while True:gc.collect()
_thread.start_new_thread(_____,())
returnData=Pages.Home()
while not returnData:
    returnData=Pages.Home()