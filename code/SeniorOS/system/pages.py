from SeniorOS.apps.port import *
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import SeniorOS.system.typer as Typer
import urequests
import ntptime
import network
from mpython import wifi,oled
from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from mpython import button_a,button_b
import gc
import time,uos
import machine

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
        ntptime.settime(8, "time.windows.com")
        DayLight.message("Welcome to SeniorOS")
        time.sleep(2)
        return True
    except:
        time.sleep(2)
        return True

def WifiPages():
    oled.fill(0)
    DayLight.VastSea.Off()
    wifiNum = DayLight.ListOptions(Core.Data.Get("list", "wifiName"), 18, False, '请选择配置')
    oled.show()
    ConfigureWLAN((Core.Data.Get("list", "wifiName")[wifiNum]), (Core.Data.Get("list", "wifiPassword")[wifiNum]))

def CloudNotification():
    time.sleep(0.2)
    DayLight.app('云端通知')
    try:
        oled.DispChar(str('正在从云端获取'), 5, 18, 2)
        oled.show()
        _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/Notifications.fos', headers={})
        if _response.status_code != 200:
            oled.DispChar('ERR HTTP CODE '+str(_response.status_code), 5, 18, 2)
            oled.show()
            return
        notifications = (_response.text.split(';'))
    except OSError as e:
        oled.DispChar('连接超时' if e.args[0]==113 else "发生了未知错误", 5, 18, 2)
        oled.show()
        return
    except Exception as e:
        print(e)
        while not button_a.is_pressed():
            oled.DispChar('发生了未知错误', 5, 18, 2)
            oled.DispChar(str(e), 5, 34,auto_return=True)
            oled.show()
        return
    while not button_a.is_pressed():
        DayLight.app('云端通知')
        oled.DispChar(notifications[1], 5, 18)
        oled.DispChar(notifications[2], 5, 32)
        oled.DispChar(notifications[3], 5, 45)
        oled.show()
    return

def SettingPanel():
    import SeniorOS.data.map as Map
    time.sleep(0.2)
    while not button_a.is_pressed():
        options = DayLight.Select.Style1(['桌面风格', '电源选项', '日光模式','亮度调节', '释放内存'], 28, True, "设置面板")
        DayLight.VastSea.Off()
        if options == None:
            pass
        else:
            Map.SettingPanel.get(options)()
        return
    return

def Home():
    import SeniorOS.data.map as Map
    while not eval("[/GetButtonExpr('thab')/]"):
        Map.HomePage.get(int(Core.Data.Get("text", "homeStyleNum")))()
        
    
    if eval("[/GetButtonExpr('ab',connector='and')/]"):
        oled.fill(0)
        DayLight.app('退出确认')
        oled.DispChar("你同时按下了AB",5,18)
        oled.DispChar("将回到启动选择器",5,32)
        oled.DispChar("同时按下PN确认",0,45)
        oled.show()
        while not eval("[/GetButtonExpr('pythonab')/]"):pass
        if eval("[/GetButtonExpr('pn')/]"):
            return True

    if button_a.is_pressed():
        DayLight.VastSea.SeniorMove.Text("云端通知",-10,-20,15,-20)
        CloudNotification()
        DayLight.VastSea.SeniorMove.Text("云端通知",5,4,-20,50)
    elif button_b.is_pressed():
        DayLight.VastSea.SeniorMove.Text("设置面板",148,-50,-50,-50)
        SettingPanel()
        DayLight.VastSea.SeniorMove.Text("设置面板",5,4,120,50)
    elif touchPad_T.is_pressed() and touchPad_H.is_pressed():
        DayLight.VastSea.SeniorMove.Line(0, 0, 128, 0, 0, -128, 128, -128)
        App()
        DayLight.VastSea.SeniorMove.Line(0, 46, 128, 46, 0, 46, 128, 46)

def select(options:list)->tuple:
    print("SeniorOS-[GxxkAPI]进入选择器界面")
    target = 0
    # 主循环
    while True:
        print("SeniorOS-[GxxkAPI]Target"+str(target))
        # 绘制UI
        oled.DispChar(options[target], 0, 16, reverse=True) # 反色模式绘制选中内容
        try:
            oled.DispChar(options[target+1], 0, 32)
            oled.DispChar(options[target+2], 0, 48) 
        except:pass  
        oled.show()
        # 等待操作
        while not eval("[/GetButtonExpr('pnab')/]"):pass
        # 做出决策
        if button_a.value()==0:
            return target, "A"
        elif button_b.value()==0:
            return target, "B"
        elif touchPad_P.read() < 100:
            target -= 1  # 向上（左）
        elif touchPad_N.read() < 100:
            target += 1  # 向下（右）
        if target == -1:
            target = len(options)-1
        elif target==len(options):
            target=0

def About():
    oled.fill(0)
    while not button_a.is_pressed():
        oled.Bitmap(16, 20, bytearray(Core.Data.Get("text", "SeniorLogo")), 98, 20, 1)
        oled.show()

def wlanscan():#定义扫描wifi函数
    import network
    wlan = network.WLAN()#定义类
    wlan.active(True)#打开
    return [i[0].decode() for i in network.WLAN().scan()]#返回

def choosewifi():
    oled.fill(0)
    oled.DispChar("扫描 Wifi 中,请稍等",0,0)
    oled.show()
    wifilist = wlanscan()
    num=0
    num = DayLight.ListOptions(wifilist, 8, True, "None")
    oled.fill(0)
    oled.DispChar("请稍等",0,0)
    oled.show()
    time.sleep(2)#经典
    oled.fill(0)
    oled.DispChar("请输入您的 WiFi 密码",0,0)
    oled.show()
    time.sleep(3)
    import network
    wifi=network.WLAN()
    pwd=Typer.main()
    try:
        wifi.connectWiFi(wifilist[num],pwd)
        oled.fill(0)
        oled.DispChar("连接成功",0,0)
        oled.show()
        open("/SeniorOS/data/userWifi.sros",'a+').write("\n{},{}".format(wifilist[num],pwd))
        return True
    except:
        oled.fill(0)
        oled.DispChar("连接失败",0,0)
        oled.show()
        return False