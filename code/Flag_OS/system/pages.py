import Flag_OS.system.ui as UI
import Flag_OS.system.core as Core
import Flag_OS.apps.logo as logo
#import framebuf
#import font.dvsmb_21
import urequests
#import json
#import math
#import gc
import ntptime
import Flag_OS.fonts.quantum
from mpython import wifi,oled
from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from mpython import button_a,button_b
import gc
import time,uos
runtimeDict={
        "oled":oled,"wifi":wifi(),
        "touchPad_P":touchPad_P,"touchPad_Y":touchPad_Y,"touchPad_H":touchPad_H,"touchPad_O":touchPad_O,"touchPad_N":touchPad_N,"touchPad_T":touchPad_T,
        "button_a":button_a,"button_b":button_b,
        "ntptime":__import__('ntptime'),
        "time":time,
        "gc":gc,
        "os":uos
}
# --SystemUniRuntime--
eval("[/hashtag/]");wifi=wifi;oled=oled;ntptime=ntptime;time=time
eval("[/hashtag/]");touchPad_P=touchPad_P;touchPad_Y=touchPad_Y;touchPad_N=touchPad_N;touchPad_O=touchPad_O;touchPad_T=touchPad_T;touchPad_H=touchPad_H
eval("[/hashtag/]");button_a=button_a;button_b=button_b

# --SystemUniRuntime--

# Gxxk留言：
# 以后写设置面板记得注意 有关Flag_OS/data/light.fos的部分 1是开（也就是每次会触发一个oled.invert(1)的那个） 0是关
# PS: 这是我改的 毕竟cfgfile又不给用户看

wifi=wifi()
plugins_list = []
plugins_tip = []
app_list = ['Flag 设置', 'Flag 线上插件', 'Flag 文件']
app_tip = ['Flag OS 设置', '线上拓展插件', 'Flag OS 文件操作']
settingsPanelList = ['亮度', '音量', '日光模式']

logo_FlagOS = bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X60,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X1F,0XFC,0XE0,0X00,0X00,0X00,0X01,0XFF,0X01,0XFF,0X00,0X00,0X00, 0X00,0X00,0X00,0X1F,0XFC,0XE0,0X00,0X00,0X00,0X03,0XFF,0X83,0XFF,0X00,0X00,0X00, 0X00,0X00,0X00,0X18,0X00,0XE0,0X00,0X00,0X00,0X07,0X83,0XC7,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XE0,0X00,0X00,0X00,0X0E,0X01,0XC6,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XE3,0XF0,0X0F,0XF0,0X0E,0X01,0XCE,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XC3,0XFC,0X1F,0XF0,0X0C,0X01,0XCE,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XC0,0X3C,0X3C,0X70,0X1C,0X01,0XC7,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC0,0X0E,0X70,0X70,0X1C,0X01,0XC7,0XF8,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC0,0X0E,0X70,0X70,0X1C,0X01,0XC1,0XFE,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC7,0XFC,0X70,0X70,0X1C,0X01,0XC0,0X1E,0X00,0X00,0X00, 0X00,0X00,0X00,0X30,0X01,0XCF,0XFC,0X60,0X60,0X1C,0X01,0XC0,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0XCC,0X0C,0X60,0X60,0X1C,0X01,0X80,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0XDC,0X1C,0X70,0XE0,0X1C,0X03,0X80,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X9C,0X1C,0X70,0XE0,0X1E,0X07,0X00,0X1E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X8F,0XFC,0X7F,0XE0,0X0F,0XFF,0X1F,0XFC,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X87,0XFC,0X3F,0XE0,0X07,0XFC,0X1F,0XF8,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XE0,0X00,0X40,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X01,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,])

def ConfigureWLAN(ssid, password):
    UI.consani(0, 64, 128, 64, 0, 0, 128, 64)
    oled.fill(0)
    oled.Bitmap(32, 23, logo_FlagOS, 64, 18, 1)
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
            if button_a.is_pressed() or button_b.is_pressed():
                return False

def wifi_page():
    oled.fill(0)
    oled.Bitmap(32, 23, logo_FlagOS, 64, 18, 1)
    oled.DispChar('       请选择 WiFi 配置', 0, 48, 1)
    oled.show()
    while True:
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            if ConfigureWLAN('ChinaNet-x6VA', '1145141919810'):
                return

def CloudNotification():
    time.sleep(0.2)
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
    UI.app('Flag 云端通知')
    try:
        oled.DispChar(str('正在从云端获取'), 5, 18, 2)
        oled.show()
        _response = urequests.get('https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/Notifications.fos', headers={})
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
        UI.app('Flag 云端通知')
        oled.DispChar(notifications[1], 5, 18)
        oled.DispChar(notifications[2], 5, 32)
        oled.DispChar(notifications[3], 5, 45)
        oled.show()
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)

# TODO.
def SettingPanel():
    pass

def home():
    time.sleep_ms(20)
    while not eval("[/GetButtonExpr('thab')/]"):
        oled.fill(0)
        UI.DisplayFont(Flag_OS.fonts.quantum, (str(Core.GetTime.Hour())), 30, 18, False)
        UI.DisplayFont(Flag_OS.fonts.quantum, (str(Core.GetTime.Min())), 64, 18, False)
        oled.hline(50, 62, 30, 1)
        oled.show()
    
    if eval("[/GetButtonExpr('ab',connector='and')/]"):
        oled.fill(0)
        oled.DispChar("退出确认",0,-1)
        oled.hline(0,15,128,1)
        oled.DispChar("你同时按下了AB",0,16)
        oled.DispChar("将回到启动选择器",0,32)
        oled.DispChar("同时按下PN确认",0,48)
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
        UI.consani(64, 64, 0, 0, 0, 0, 128, 64)
        app()

def select(options:list)->tuple:
    print("[GxxkAPI]进入选择器界面")
    target = 0
    # 主循环
    while True:
        print("[GxxkAPI]Target"+str(target))
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
    DataCtrl=Core.DataCtrl('/Flag_OS/data')
    while not button_a.is_pressed():
        oled.fill(0)
        oled.invert(int(DataCtrl.Get('light')))
        if home_movement_x >= 0 and home_movement_x <= 118:
            if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
                home_movement_x = home_movement_x + 7
            elif touchPad_O.is_pressed() and touchPad_N.is_pressed():
                home_movement_x = home_movement_x + -7
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
        oled.DispChar(str(app_list[app_num]), 35, 45, 3)
        oled.hline(50, 62, 30, 1)
        if home_movement_x >= 0 and home_movement_x <= 46:
            app_num = 0
            app_logo = logo.app_0
        elif home_movement_x >= 47 and home_movement_x <= 85:
            app_num = 1
            app_logo = logo.app_1
        elif home_movement_x >= 85 and home_movement_x <= 118:
            app_num = 2
        oled.show()
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            UI.ConsaniApp(home_movement_x, 6, 36, 36, 0, 0, 128, 64, app_logo, home_movement_x + 5)
            class FlagAPI:
                Core=Core
                UI=UI
            __import__("Flag_OS.apps.app_" + str(app_num) + ".main",{
                "FlagAPI":FlagAPI,
                    "touchPad_P":touchPad_P,
                    "touchPad_Y":touchPad_Y,
                    "touchPad_T":touchPad_T,
                    "touchPad_H":touchPad_H,
                    "touchPad_O":touchPad_O,
                    "touchPad_N":touchPad_N,
                    "button_a":button_a,
                    "button_b":button_b,
            })
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
    home()

def about():
    oled.fill(0)
    while not button_a.is_pressed():
        oled.Bitmap(32, 12, logo_FlagOS, 64, 18, 1)
        oled.show()
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
def wlanscan():#定义扫描wifi函数
    wlan = network.WLAN()#定义类
    wlan.active(True)#打开
    return [i[0].decode() for i in network.WLAN().scan()]#返回