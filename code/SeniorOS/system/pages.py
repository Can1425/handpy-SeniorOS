import SeniorOS.system.ui as UI
import SeniorOS.system.core as Core
import SeniorOS.apps.logo as logo
#import framebuf
#import font.dvsmb_21
import urequests
#import json
#import math
#import gc
import ntptime
import SeniorOS.fonts.quantum
from mpython import wifi,oled
from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from mpython import button_a,button_b
import gc
import time,uos


# Gxxk留言：
# 以后写设置面板记得注意 有关 SeniorOS/data/light.fos 的部分 1是开（也就是每次会触发一个oled.invert(1)的那个） 0是关
# PS: 这是我改的 毕竟cfgfile又不给用户看
# 你写了忘记改了是吧 - LP    Gxxk/Reply:emm 实际上是改了内置逻辑忘记改配置文件
wifi=wifi()
plugins_list = []
plugins_tip = []
app_list = ['设置', '线上插件', '文件']
app_tip = ['设置', '线上拓展插件', '文件操作']
settingsPanelList = ['亮度', '音量', '日光模式']

def ConfigureWLAN(ssid, password):
    oled.fill(0)
    oled.Bitmap(16, 20, bytearray([0X07,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X00,0X7C,0X00,0X0F,0XFC,0X00, 0X00,0X00,0X00,0X00,0X00,0X01,0XFE,0X00,0XFE,0X00,0X1F,0XFC,0X00,0X00,0X00,0X00, 0X00,0X00,0X07,0XFF,0X01,0XFF,0X80,0X3C,0X00,0X00,0X00,0X01,0X00,0X00,0X00,0X0F, 0X07,0X83,0X83,0X80,0X38,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X1C,0X01,0XC3,0X81, 0X80,0X30,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X38,0X00,0XE3,0X00,0X00,0X30,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X38,0X00,0XE3,0X80,0X00,0X38,0X00,0X18,0X1F,0XE0, 0X0F,0XFC,0X3E,0X30,0X00,0X63,0XC0,0X00,0X3F,0X00,0X7E,0X1F,0XF1,0X9F,0XFC,0X7E, 0X70,0X00,0X71,0XF0,0X00,0X1F,0XF0,0XE7,0X1C,0X39,0X9C,0X0C,0XE0,0X70,0X00,0X70, 0XFE,0X00,0X07,0XF9,0XC3,0X18,0X19,0X98,0X0C,0XC0,0X70,0X00,0X70,0X1F,0X80,0X00, 0X79,0XC3,0X98,0X19,0X98,0X0C,0XC0,0X30,0X00,0X70,0X03,0X80,0X00,0X39,0XFF,0X98, 0X19,0X88,0X04,0XC0,0X30,0X00,0X60,0X01,0XC0,0X00,0X39,0XFF,0X18,0X19,0X80,0X00, 0XC0,0X38,0X00,0XE0,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X88,0X0C,0XC0,0X1C,0X01, 0XC2,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X8C,0X0C,0XC0,0X1E,0X03,0XC7,0X01,0XC0, 0X71,0XF0,0XC3,0X18,0X19,0X8E,0X0C,0XC0,0X0F,0XDF,0X83,0XC3,0X80,0XFF,0XE0,0X7F, 0X18,0X19,0X87,0XFC,0X40,0X07,0XFF,0X01,0XFF,0X00,0XFF,0XC0,0X3C,0X18,0X19,0X83, 0XFC,0X40,0X01,0XFC,0X00,0X7E,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
    oled.fill_rect(0, 48, 128, 16, 0)
    oled.DispChar(str('              请稍等...'), 0, 48, 1)
    oled.show()
    try:
        wifi.connectWiFi(ssid, password)
        ntptime.settime(8, "time.windows.com")
        oled.fill_rect(0, 48, 128, 16, 0)
        oled.DispChar(str('             配置成功'), 0, 48, 1)
        oled.show()
        time.sleep(2)
        return True
    except:
        oled.fill_rect(0, 48, 128, 16, 0)
        oled.DispChar(str('             配置失败'), 0, 48, 1)
        oled.show()
        while True:
            if button_a.is_pressed():
                return False
            if button_b.is_pressed():
                return True

def wifi_page():
    # Data=Core.DataCtrl("/SeniorOS/data/")
    wifiConfigRead=Core.Data.Get('wifi')#读wifi配置文件
    wifiConfig=wifiConfigRead.split('\n')#读WiFi配置，以\n分隔
    #例如这样:
    #原wifi配置文件:
    '''
    wifi1,wifi1pwd
    wifi2,wifi2pwd
    '''
    #解析后wifi配置文件
    #['wifi1,wifi1pwd','wifi2,wifi2pwd']
    wifiSSID=[]
    wifiPWD=[]
    for i in range(len(wifiConfig)):
        cfg=wifiConfig[i].split(',')
        wifiSSID.append(cfg[0])
        wifiPWD.append(cfg[1])

        #这里就是把解析后WiFi配置文件再解析一次
        #例如:
        #wificfg=['wifi1,wifi1pwd','wifi2,wifi2pwd']
        #解析后:
        #wifissid=['wifi1','wifi2']
        #wifipwd=['wifi1pwd','wifi2pwd']
        #对于这玩意是不是要写成单独的函数,待定#
        #对于是否要集合为字典,待定#
        #现在3行内会显示,但不能超过3行(按程序设定不会显示)
        #即将上线换页功能
    oled.fill(0)
    #oled.Bitmap(16, 20, bytearray([0X07,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X00,0X7C,0X00,0X0F,0XFC,0X00, 0X00,0X00,0X00,0X00,0X00,0X01,0XFE,0X00,0XFE,0X00,0X1F,0XFC,0X00,0X00,0X00,0X00, 0X00,0X00,0X07,0XFF,0X01,0XFF,0X80,0X3C,0X00,0X00,0X00,0X01,0X00,0X00,0X00,0X0F, 0X07,0X83,0X83,0X80,0X38,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X1C,0X01,0XC3,0X81, 0X80,0X30,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X38,0X00,0XE3,0X00,0X00,0X30,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X38,0X00,0XE3,0X80,0X00,0X38,0X00,0X18,0X1F,0XE0, 0X0F,0XFC,0X3E,0X30,0X00,0X63,0XC0,0X00,0X3F,0X00,0X7E,0X1F,0XF1,0X9F,0XFC,0X7E, 0X70,0X00,0X71,0XF0,0X00,0X1F,0XF0,0XE7,0X1C,0X39,0X9C,0X0C,0XE0,0X70,0X00,0X70, 0XFE,0X00,0X07,0XF9,0XC3,0X18,0X19,0X98,0X0C,0XC0,0X70,0X00,0X70,0X1F,0X80,0X00, 0X79,0XC3,0X98,0X19,0X98,0X0C,0XC0,0X30,0X00,0X70,0X03,0X80,0X00,0X39,0XFF,0X98, 0X19,0X88,0X04,0XC0,0X30,0X00,0X60,0X01,0XC0,0X00,0X39,0XFF,0X18,0X19,0X80,0X00, 0XC0,0X38,0X00,0XE0,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X88,0X0C,0XC0,0X1C,0X01, 0XC2,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X8C,0X0C,0XC0,0X1E,0X03,0XC7,0X01,0XC0, 0X71,0XF0,0XC3,0X18,0X19,0X8E,0X0C,0XC0,0X0F,0XDF,0X83,0XC3,0X80,0XFF,0XE0,0X7F, 0X18,0X19,0X87,0XFC,0X40,0X07,0XFF,0X01,0XFF,0X00,0XFF,0XC0,0X3C,0X18,0X19,0X83, 0XFC,0X40,0X01,0XFC,0X00,0X7E,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
    for i in range(len(wifiSSID)):
        if i<4:oled.DispChar(wifiSSID[i],0,i*16)
    #oled.Bitmap(16, 20, bytearray([0X07,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X00,0X7C,0X00,0X0F,0XFC,0X00, 0X00,0X00,0X00,0X00,0X00,0X01,0XFE,0X00,0XFE,0X00,0X1F,0XFC,0X00,0X00,0X00,0X00, 0X00,0X00,0X07,0XFF,0X01,0XFF,0X80,0X3C,0X00,0X00,0X00,0X01,0X00,0X00,0X00,0X0F, 0X07,0X83,0X83,0X80,0X38,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X1C,0X01,0XC3,0X81, 0X80,0X30,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X38,0X00,0XE3,0X00,0X00,0X30,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X38,0X00,0XE3,0X80,0X00,0X38,0X00,0X18,0X1F,0XE0, 0X0F,0XFC,0X3E,0X30,0X00,0X63,0XC0,0X00,0X3F,0X00,0X7E,0X1F,0XF1,0X9F,0XFC,0X7E, 0X70,0X00,0X71,0XF0,0X00,0X1F,0XF0,0XE7,0X1C,0X39,0X9C,0X0C,0XE0,0X70,0X00,0X70, 0XFE,0X00,0X07,0XF9,0XC3,0X18,0X19,0X98,0X0C,0XC0,0X70,0X00,0X70,0X1F,0X80,0X00, 0X79,0XC3,0X98,0X19,0X98,0X0C,0XC0,0X30,0X00,0X70,0X03,0X80,0X00,0X39,0XFF,0X98, 0X19,0X88,0X04,0XC0,0X30,0X00,0X60,0X01,0XC0,0X00,0X39,0XFF,0X18,0X19,0X80,0X00, 0XC0,0X38,0X00,0XE0,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X88,0X0C,0XC0,0X1C,0X01, 0XC2,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X8C,0X0C,0XC0,0X1E,0X03,0XC7,0X01,0XC0, 0X71,0XF0,0XC3,0X18,0X19,0X8E,0X0C,0XC0,0X0F,0XDF,0X83,0XC3,0X80,0XFF,0XE0,0X7F, 0X18,0X19,0X87,0XFC,0X40,0X07,0XFF,0X01,0XFF,0X00,0XFF,0XC0,0X3C,0X18,0X19,0X83, 0XFC,0X40,0X01,0XFC,0X00,0X7E,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
    oled.DispChar('       请选择 WiFi 配置', 0, 48, 1)
    oled.show()
    while True:
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            if ConfigureWLAN(wifiSSID[0],wifiPWD[0]):#保证至少有1个配置文件
                return
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            try:
                if ConfigureWLAN(wifiSSID[1],wifiPWD[1]):
                    return
            except:
                return
        if touchPad_O.is_pressed() and touchPad_N.is_pressed():
            try:
                if ConfigureWLAN(wifiSSID[2],wifiPWD[2]):
                    return
            except:
                return

def CloudNotification():
    time.sleep(0.2)
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
    UI.app('云端通知')
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
        oled.DispChar("OSError "+e.args[0], 5, 34, 2)
        oled.show()
        return
    except Exception as e:
        print(e)
        while not button_a.is_pressed():
            oled.DispChar('发生了未知错误', 5, 18, 2)
            oled.DispChar(str(e), 5, 34,auto_return=True)
            oled.show()
        UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
        return
    while not button_a.is_pressed():
        UI.app('云端通知')
        oled.DispChar(notifications[1], 5, 18)
        oled.DispChar(notifications[2], 5, 32)
        oled.DispChar(notifications[3], 5, 45)
        oled.show()
    UI.Tti()
    return home()

# TODO.
def SettingPanel():
    pass

def home():
    time.sleep_ms(20)
    while not eval("[/GetButtonExpr('thab')/]"):
        oled.fill(0)
        UI.DisplayFont(SeniorOS.fonts.quantum, Core.sys_hour, 30, 18, False)
        UI.DisplayFont(SeniorOS.fonts.quantum, Core.sys_min, 64, 18, False)
        oled.hline(50, 62, 30, 1)
        oled.show()
    
    if eval("[/GetButtonExpr('ab',connector='and')/]"):
        oled.fill(0)
        UI.app('退出确认')
        oled.DispChar("你同时按下了AB",5,18)
        oled.DispChar("将回到启动选择器",5,32)
        oled.DispChar("同时按下PN确认",0,45)
        oled.show()
        while not eval("[/GetButtonExpr('pythonab')/]"):pass
        if eval("[/GetButtonExpr('pn')/]"):
            return True
        

    if button_a.is_pressed():
        CloudNotification()
    elif button_b.is_pressed():
        UI.consani(128, 0, 128, 0, 0, 0, 128, 64)
        SettingPanel()
    elif touchPad_T.is_pressed() and touchPad_H.is_pressed():
        UI.consani(0, 64, 128, 64, 0, 0, 128, 64)
        app()

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


def app():
    global app_list, app_num
    home_movement_x = 40
    app_num = 0
    time.sleep_ms(5)
    while not button_a.is_pressed():
        try:
          oled.invert(int(Core.Data.Get('light')))
        except:
            pass
        if home_movement_x >= 0 and home_movement_x <= 118:
            if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
                home_movement_x = home_movement_x + 10
            elif touchPad_O.is_pressed() and touchPad_N.is_pressed():
                home_movement_x = home_movement_x + -10
        else:
            if home_movement_x <= 0:
                home_movement_x = 4
            elif home_movement_x >= 118:
                home_movement_x = 114
        oled.fill(0)
        oled.RoundRect(home_movement_x, 6, 36, 36, 3, 1)
        oled.RoundRect((home_movement_x - 40), 6, 36, 36, 3, 1)
        oled.RoundRect((home_movement_x - 80), 6, 36, 36, 3, 1)
        oled.Bitmap(home_movement_x + 5, 12, logo.app_0, 25, 25, 1)
        oled.Bitmap(home_movement_x - 40 + 5, 12, logo.app_1, 25, 25, 1)
        oled.DispChar(app_list[app_num],UI.AutoCenter(app_list[app_num]),45)
        oled.hline(50, 62, 30, 1)
        if home_movement_x >= 0 and home_movement_x <= 46:
            app_num = 0
            app_logo = logo.app_0
        elif home_movement_x >= 47 and home_movement_x <= 90:
            app_num = 1
            app_logo = logo.app_1
        elif home_movement_x >= 90 and home_movement_x <= 118:
            app_num = 2
        oled.show()
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            UI.ConsaniApp(home_movement_x, 6, 36, 36, 0, 0, 128, 64, app_logo, home_movement_x + 5)
            class SeniorOSAPI:
                Core=Core
                UI=UI
            __import__("SeniorOS.apps.app_" + str(app_num) + ".main",{
                "SeniorOSAPI":SeniorOSAPI,
                    "touchPad_P":touchPad_P,
                    "touchPad_Y":touchPad_Y,
                    "touchPad_T":touchPad_T,
                    "touchPad_H":touchPad_H,
                    "touchPad_O":touchPad_O,
                    "touchPad_N":touchPad_N,
                    "button_a":button_a,
                    "button_b":button_b,
            })
    UI.Tti()
    return home()

def about():
    oled.fill(0)
    while not button_a.is_pressed():
        oled.Bitmap(16, 20, bytearray([0X07,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X00,0X7C,0X00,0X0F,0XFC,0X00, 0X00,0X00,0X00,0X00,0X00,0X01,0XFE,0X00,0XFE,0X00,0X1F,0XFC,0X00,0X00,0X00,0X00, 0X00,0X00,0X07,0XFF,0X01,0XFF,0X80,0X3C,0X00,0X00,0X00,0X01,0X00,0X00,0X00,0X0F, 0X07,0X83,0X83,0X80,0X38,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X1C,0X01,0XC3,0X81, 0X80,0X30,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X38,0X00,0XE3,0X00,0X00,0X30,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X38,0X00,0XE3,0X80,0X00,0X38,0X00,0X18,0X1F,0XE0, 0X0F,0XFC,0X3E,0X30,0X00,0X63,0XC0,0X00,0X3F,0X00,0X7E,0X1F,0XF1,0X9F,0XFC,0X7E, 0X70,0X00,0X71,0XF0,0X00,0X1F,0XF0,0XE7,0X1C,0X39,0X9C,0X0C,0XE0,0X70,0X00,0X70, 0XFE,0X00,0X07,0XF9,0XC3,0X18,0X19,0X98,0X0C,0XC0,0X70,0X00,0X70,0X1F,0X80,0X00, 0X79,0XC3,0X98,0X19,0X98,0X0C,0XC0,0X30,0X00,0X70,0X03,0X80,0X00,0X39,0XFF,0X98, 0X19,0X88,0X04,0XC0,0X30,0X00,0X60,0X01,0XC0,0X00,0X39,0XFF,0X18,0X19,0X80,0X00, 0XC0,0X38,0X00,0XE0,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X88,0X0C,0XC0,0X1C,0X01, 0XC2,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X8C,0X0C,0XC0,0X1E,0X03,0XC7,0X01,0XC0, 0X71,0XF0,0XC3,0X18,0X19,0X8E,0X0C,0XC0,0X0F,0XDF,0X83,0XC3,0X80,0XFF,0XE0,0X7F, 0X18,0X19,0X87,0XFC,0X40,0X07,0XFF,0X01,0XFF,0X00,0XFF,0XC0,0X3C,0X18,0X19,0X83, 0XFC,0X40,0X01,0XFC,0X00,0X7E,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 64, 18, 1)
        oled.DispChar("SeniorOS-by Can1425",5,45)
        oled.show()
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)

def wlanscan():#定义扫描wifi函数
    wlan = network.WLAN()#定义类
    wlan.active(True)#打开
    return [i[0].decode() for i in network.WLAN().scan()]#返回