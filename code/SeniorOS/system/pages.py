from SeniorOS.apps.port import *
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import SeniorOS.system.typer as Typer
import urequests
import ntptime
import network
from SeniorOS.system.devlib import wifi,oled
from SeniorOS.system.devlib import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from SeniorOS.system.devlib import button_a,button_b
import gc
import time,uos
import machine,_thread
import SeniorOS.system.log_manager as LogManager
import SeniorOS.system.pages_manager as PagesManager
LogManager.Output("system/pages.mpy", "INFO")

# Gxxk留言：
# 以后写设置面板记得注意 有关 SeniorOS/data/light.fos 的部分 1是开（也就是每次会触发一个oled.invert(1)的那个） 0是关
# PS: 这是我改的 毕竟cfgfile又不给用户看
# 你写了忘记改了是吧 - LP    Gxxk/Reply:emm 实际上是改了内置逻辑忘记改配置文件
wifi=wifi()

def ConfigureWLAN(ssid, password):
    oled.fill(0)
    oled.Bitmap(16, 20, bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X3C,0X00,0X00,0X00,0X30, 0X00,0X00,0X00,0X70,0X00,0X78,0X00,0X03,0XFE,0X00,0X00,0X00,0X70,0X00,0X00,0X03, 0XFE,0X03,0XFE,0X00,0X07,0XFC,0X00,0X00,0X00,0X30,0X00,0X00,0X07,0X8F,0X07,0XFE, 0X00,0X06,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X0E,0X03,0X86,0X00,0X00,0X06,0X00, 0X0E,0X03,0XE0,0X20,0X38,0X01,0X8C,0X01,0X8E,0X00,0X00,0X0E,0X00,0X3F,0X87,0XF8, 0X71,0XFE,0X0F,0X98,0X00,0XCE,0X00,0X00,0X0F,0X00,0X7B,0XC7,0XFC,0X71,0XFF,0X1F, 0X98,0X00,0XCE,0X00,0X00,0X07,0XF0,0X60,0XCE,0X0C,0X63,0X83,0X18,0X18,0X00,0XC7, 0XF0,0X00,0X03,0XFC,0XE0,0XCE,0X0C,0X63,0X03,0X38,0X18,0X00,0XC3,0XFC,0X00,0X00, 0X1C,0XFF,0XCE,0X0C,0X63,0X03,0X38,0X18,0X00,0XC0,0X1C,0X00,0X00,0X0C,0XFF,0XCC, 0X0C,0X67,0X03,0X30,0X18,0X00,0XC0,0X0C,0X00,0X00,0X0C,0XC0,0X0C,0X0C,0X67,0X03, 0X30,0X0C,0X01,0XC0,0X0C,0X00,0X00,0X1C,0XC0,0X0C,0X1C,0XE7,0X07,0X30,0X0E,0X03, 0X80,0X1C,0X00,0X00,0X3C,0XE0,0X0C,0X1C,0XE7,0X8E,0X30,0X07,0X8F,0X00,0X3C,0X00, 0X1F,0XF8,0X7F,0X8C,0X1C,0XE3,0XFE,0X30,0X03,0XFE,0X1F,0XF8,0X00,0X1F,0XE0,0X3F, 0X8C,0X18,0XC1,0XF8,0X30,0X00,0XF8,0X1F,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
    oled.show()
    try:
        wifi.connectWiFi(ssid, password)
        ntptime.settime(8, Core.Data.Get("text", "timingServer"))
        time.sleep(2)
        return True
    except:
        time.sleep(2)
        return False

def WifiPages():
    oled.fill(0)
    DayLight.VastSea.Off()
    wifiNum = DayLight.ListOptions(Core.Data.Get("list", "wifiName"), 18, False, eval("[/Language('请选择配置')/]"))
    oled.show()
    ConfigureWLAN((Core.Data.Get("list", "wifiName")[wifiNum]), (Core.Data.Get("list", "wifiPassword")[wifiNum]))

def CloudNotification():
    time.sleep(0.2)
    DayLight.App.Style1(eval("[/Language('云端通知')/]"))
    try:
        oled.DispChar(eval("[/Language('请稍等')/]"), 5, 18, 2)
        oled.show()
        _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/Notifications.fos', headers={})
        if _response.status_code != 200:
            oled.DispChar('ERR HTTP CODE '+str(_response.status_code), 5, 18, 2)
            oled.show()
            return
        notifications = (_response.text.split(';'))
    except IndexError as error:
        print(error)
        oled.DispChar(eval("[/Language('加载失败')/]"), 5, 18, 2)
        oled.show()
        return
    while not button_a.is_pressed():
        DayLight.App.Style1(eval("[/Language('云端通知')/]"))
        oled.DispChar(notifications[1], 5, 18)
        oled.DispChar(notifications[2], 5, 32)
        oled.DispChar(notifications[3], 5, 45)
        oled.show()
    return

def SettingPanel(): 
    def HS_CPU():
        while not button_a.is_pressed():
            oled.fill(0)
            oled.DispChar(f"{str(machine.freq)/10000000} MHZ",0,16)
            oled.DispChar("CPU - ESP32 @ 160MHZ",0,0)
            oled.show()
        return
    def HS_Ram():
        while not button_a.is_pressed():
            oled.fill(0)
            oled.DispChar("Ram - total:520kb",0,0)
            oled.DispChar(f"内存可用:{gc.mem_free()}",0,16)
            oled.DispChar("触摸键释放内存",0,32)
            oled.show()
            if eval("[/GetButtonExpr('python')/]"):
                _thread.start_new_thread(Core.FullCollect())
        return 0
    def HS_flash():
        while not button_a.is_pressed():
            oled.fill(0)
            oled.DispChar("Flash - total:8MB",0,0)
            oled.DispChar("可用:")
    ListOperation = {#这里填对应的函数名（不加括号）#ok,哪里学的(
    0: HS_CPU,
    1: HS_Ram,
    2: HS_flash,
    3: HS_RGB,
    }
    hardware=["CPU","Ram","flash","RGB灯","麦克风","OLED"]
    def hardwareSettings():
        while not button_a.is_pressed():
            options = DayLight.ListOptions(hardware, 8, True, "None")
            ListOperation.get(options)()# 这么用，就可以省略大量的 if
    while not button_a.is_pressed():
        oled.fill(0)
        oled.DispChar("PY-板载硬件",0,0)
        oled.DispChar("ON-外设",0,16)
        oled.show()
        while not button_a.is_pressed():
            if touchpad_p.is_pressed() or touchpad_y.is_pressed():
                hardwareSettings()
                break
            elif touchpad_o.is_pressed() or touchpad_n.is_pressed():
                pass
                break
        # 剩下的交给你


def Home():
    PagesManager.Main.Import('SeniorOS.style.home', 'Style' + Core.Data.Get("text", "homeStyleNum"))
    if button_a.is_pressed():
        DayLight.VastSea.SeniorMove.Text(eval("[/Language('云端通知')/]"),-10,-20,15,-20)
        Core.Load('system.pages', 'CloudNotification')
        DayLight.VastSea.SeniorMove.Text(eval("[/Language('云端通知')/]"),5,4,-20,50)
    elif button_b.is_pressed():
        DayLight.VastSea.SeniorMove.Text(eval("[/Language('控制面板')/]"),148,-50,-50,-50)
        SettingPanel()
        DayLight.VastSea.SeniorMove.Text(eval("[/Language('控制面板')/]"),5,4,120,50)
    elif eval("[/GetButtonExpr('th')/]"):
        DayLight.VastSea.SeniorMove.Line(0, 0, 128, 0, 0, -128, 128, -128)
        App()
        DayLight.VastSea.SeniorMove.Line(0, 46, 128, 46, 0, 46, 128, 46)
    elif eval("[/GetButtonExpr('ab')/]"):
        pass
    del sys.modules['SeniorOS.style.home']

def About():
    oled.fill(0)
    while not button_a.is_pressed():
        oled.Bitmap(16, 20, bytearray(Core.Data.Get("text", "SeniorLogo")), 98, 20, 1)
        oled.show()

def Wlanscan():#定义扫描wifi函数
    import network
    wlan = network.WLAN()#定义类
    wlan.active(True)#打开
    return [i[0].decode() for i in network.WLAN().scan()]#返回

def Choosewifi():
    oled.fill(0)
    oled.DispChar(eval("[/Language('请稍等')/]"),0,0)
    oled.show()
    wifilist = Wlanscan()
    num=0
    num = DayLight.ListOptions(wifilist, 8, True, "None")
    oled.fill(0)
    oled.DispChar(eval("[/Language('请稍等')/]"),0,0)
    oled.show()
    time.sleep(2)#经典
    oled.fill(0)
    import network
    wifi=network.WLAN()
    pwd=Typer.main()
    try:
        wifi.connectWiFi(wifilist[num],pwd)
        oled.fill(0)
        oled.DispChar(eval("[/Language('加载成功')/]"), 0, 0)
        oled.show()
        # open("/SeniorOS/data/userWifi.sros",'a+').write("\n{},{}".format(wifilist[num],pwd))
        return True
    except:
        oled.fill(0)
        oled.DispChar(eval("[/Language('加载失败')/]"), 0, 0)
        oled.show()
        return False
    
def Collect():
    oled.fill(0)
    DayLight.UITools()
    try:
        oled.DispChar(eval("[/Language('请稍等')/]"), 5, 5, 1)
        time.sleep_ms(5)
        oled.DispChar(eval("[/Language('正在进行操作')/]"), 5, 18, 1)
        oled.show()
        Core.FullCollect()
        oled.DispChar(eval("[/Language('加载成功')/]"), 5, 45, 1)
        time.sleep_ms(5)
        oled.show()
        return True
    except:
        oled.DispChar(eval("[/Language('加载失败')/]"), 5, 45, 1)
        oled.show()

def Time():
    DayLight.UITools()
    try:
        oled.fill(0)
        oled.DispChar(eval("[/Language('请稍等')/]"), 5, 5, 1)
        time.sleep_ms(5)
        oled.DispChar(eval("[/Language('正在进行操作')/]"), 5, 18, 1)
        oled.show()
        ntptime.settime(8, Core.Data.Get("text", "timingServer"))
        oled.DispChar(eval("[/Language('加载成功')/]"), 5, 45, 1)
        time.sleep_ms(5)
        oled.show()
        return True
    except:
        oled.DispChar(eval("[/Language('加载失败')/]"), 5, 45, 1)
        oled.show()

def AutoConnectWifi():
    info=Core.Data.Get("text","autoConnectWifi")
    while not button_a.is_pressed():
        oled.fill(0)
        DayLight.App.Style2("自动连接 WiFi")#哥们这样塞不下( 我完成了,有事钉钉说
        oled.hline(0,16,128,1)
        if info==1:
            oled.DispChar("状态:开",0,16)
        else:
            oled.DispChar("状态:关",0,16)
        oled.DispChar("A-退出 B-切换",0,32)
        oled.DispChar("触摸键确认修改",0,48)
        oled.show()
        while not button_a.is_pressed():
            if button_b.is_pressed():
                if info==1:info=0
                else:info=1
                break
            if eval("[/GetButtonExpr('python')/]"):
                Core.Data.Write("text","autoConnectWifi",info)
                return 0