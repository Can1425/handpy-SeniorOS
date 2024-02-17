from mpython import oled,wifi
from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from mpython import button_a,button_b
import Flag_OS.system.ui as UI
import Flag_OS.system.core as Core
import Flag_OS.apps.logo as logo
import ntptime
#import network
import time
#import framebuf
#import font.dvsmb_21
import urequests
#import json
#import math
#import gc
import Flag_OS.fonts.quantum

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
            if ConfigureWLAN('TP-LINK_CD4A', '13697295123'):
                return
        elif touchPad_T.is_pressed() and touchPad_H.is_pressed():
            if ConfigureWLAN('Redmi Note 12 Turbo', '12345678910'):
                return
        elif touchPad_O.is_pressed() and touchPad_N.is_pressed():
            if ConfigureWLAN('Xiaomi_2A7A', 'menghan116118'):
                return

def CloudNotification():
    time.sleep(0.2)
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
    UI.app('Flag 云端通知')
    try:
        oled.DispChar(str('正在从云端获取'), 5, 18, 2)
        oled.show()
        _response = urequests.get('https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/Notifications.fos', headers={})
        notifications = (_response.text.split(';'))
    except:
        while not button_a.is_pressed():
            oled.DispChar('获取失败，请重试', 5, 18, 2)
            oled.show()
        UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
        return
    while not button_a.is_pressed():
        UI.app('Flag 云端通知')
        oled.DispChar(str(notifications[1]), 5, 18, 1)
        oled.DispChar(str(notifications[2]), 5, 32, 1)
        oled.DispChar(str(notifications[3]), 5, 45, 1)
        oled.show()
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)

# TODO.
def SettingPanel():
    pass

def home():
    time.sleep_ms(20)
    while not (touchPad_T.is_pressed() and touchPad_H.is_pressed() or button_a.is_pressed() or button_b.is_pressed()):
        oled.fill(0)
        UI.display_font(Flag_OS.fonts.quantum, (str(Core.GetTime.Hour())), 30, 18, False)
        UI.display_font(Flag_OS.fonts.quantum, (str(Core.GetTime.Min())), 64, 18, False)
        oled.hline(50, 62, 30, 1)
        oled.show()
    
    if button_a.is_pressed():
        CloudNotification()
    elif button_b.is_pressed():
        UI.consani(128, 0, 128, 0, 0, 0, 128, 64)
        SettingPanel()
    elif touchPad_T.is_pressed() and touchPad_H.is_pressed():
        UI.consani(64, 64, 0, 0, 0, 0, 128, 64)
        app()

def app():
    global app_list, app_num
    home_movement_x = 40
    app_num = 0
    time.sleep_ms(5)
    while not button_a.is_pressed():
        oled.fill(0)
        oled.invert(int(Core.DataCtrl.Get('light')))
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
        oled.Bitmap(home_movement_x + 5, 12, logo.app_1, 25, 25, 1)
        oled.Bitmap(home_movement_x - 40 + 5, 12, logo.app_2, 25, 25, 1)
        oled.DispChar(str(app_list[app_num]), 35, 45, 3)
        oled.hline(50, 62, 30, 1)
        if home_movement_x >= 0 and home_movement_x <= 46:
            app_num = 0
            app_logo = logo.app_1
        elif home_movement_x >= 47 and home_movement_x <= 85:
            app_num = 1
            app_logo = logo.app_2
        elif home_movement_x >= 85 and home_movement_x <= 118:
            app_num = 2
        oled.show()
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            UI.consani_app(home_movement_x, 6, 36, 36, 0, 0, 128, 64, app_logo, home_movement_x + 5)
            __import__("Flag_OS.apps.app_" + str(app_num) + ".main",{
                "FlagAPI.core":Core
            })
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
    home()

def about():
    oled.fill(0)
    while not button_a.is_pressed():
        oled.Bitmap(32, 12, logo_FlagOS, 64, 18, 1)
        oled.show()
    UI.consani(0, 0, 0, 0, 0, 0, 128, 64)
#PR函数如下：
def wlanscan():#定义扫描wifi函数
    wlan = network.WLAN()#定义类
    wlan.active(True)#打开
    return [i[0].decode() for i in network.WLAN().scan()]#返回
    #注意，此函数从LP OS移植
def read_wifi_config(file_path):#定义读配置文件函数，参数：wifi配置文件路径
    with open(file_path,'r') as f:#读文件
        config=f.read().split('\n')#读配置，以\n换行
        wifi_ssid=config[0]
        wifi_pwd=config[1]
        w=[wifi_ssid,wifi_pwd]
        return w