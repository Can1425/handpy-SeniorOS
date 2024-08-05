import SeniorOS.system.log_manager as LogManager
LogManager.Output("system/main.mpy", "INFO")
import uos as os;os.chdir('/')
import SeniorOS.system.pages as Pages
import SeniorOS.system.core as Core
import SeniorOS.system.smart_wifi as SmartWifi
import _thread
info=Core.Data.Get("text","connectWifiMode")
if info == "0":
    Pages.WifiPages()
elif info == "1":
    wifilist=[Core.Data.Get("list","wifiName"),Core.Data.Get("list","wifiPassword")]
    for i in range(len(wifilist[0])):
        connect=Pages.ConfigureWLAN(wifilist[0][i],wifilist[1][i])
        if connect:
            break
        else:
            continue
elif info == "2":
    # 启动门户
    _thread.start_new_thread(SmartWifi.start_dns_server, ())
    _thread.start_new_thread(SmartWifi.start_web_server, ())

returnData=Pages.Home()

while not returnData:
    returnData=Pages.Home()
