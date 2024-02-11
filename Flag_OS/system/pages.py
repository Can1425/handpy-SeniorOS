from mpython import *
import Flag_OS.system.ui as ui
import Flag_OS.system.core as core
import Flag_OS.apps.logo as logo
import ntptime
import network
import time
import framebuf
import font.dvsmb_21
import urequests
import json
import math
import gc
import Flag_OS.fonts.quantum

wifi=wifi()
plugins_list = []
plugins_tip = []
app_list = ['Flag 设置', 'Flag 线上插件', 'Flag 文件']
app_tip = ['Flag OS 设置', '线上拓展插件', 'Flag OS 文件操作']
setings_panel_list = ['亮度', '音量', '日光模式']
Flag_OS_logo = bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X60,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X1F,0XFC,0XE0,0X00,0X00,0X00,0X01,0XFF,0X01,0XFF,0X00,0X00,0X00, 0X00,0X00,0X00,0X1F,0XFC,0XE0,0X00,0X00,0X00,0X03,0XFF,0X83,0XFF,0X00,0X00,0X00, 0X00,0X00,0X00,0X18,0X00,0XE0,0X00,0X00,0X00,0X07,0X83,0XC7,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XE0,0X00,0X00,0X00,0X0E,0X01,0XC6,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XE3,0XF0,0X0F,0XF0,0X0E,0X01,0XCE,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XC3,0XFC,0X1F,0XF0,0X0C,0X01,0XCE,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XC0,0X3C,0X3C,0X70,0X1C,0X01,0XC7,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC0,0X0E,0X70,0X70,0X1C,0X01,0XC7,0XF8,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC0,0X0E,0X70,0X70,0X1C,0X01,0XC1,0XFE,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC7,0XFC,0X70,0X70,0X1C,0X01,0XC0,0X1E,0X00,0X00,0X00, 0X00,0X00,0X00,0X30,0X01,0XCF,0XFC,0X60,0X60,0X1C,0X01,0XC0,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0XCC,0X0C,0X60,0X60,0X1C,0X01,0X80,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0XDC,0X1C,0X70,0XE0,0X1C,0X03,0X80,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X9C,0X1C,0X70,0XE0,0X1E,0X07,0X00,0X1E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X8F,0XFC,0X7F,0XE0,0X0F,0XFF,0X1F,0XFC,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X87,0XFC,0X3F,0XE0,0X07,0XFC,0X1F,0XF8,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XE0,0X00,0X40,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X01,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,])
def wifi_page():
    oled.fill(0)
    oled.Bitmap(32, 23, Flag_OS_logo, 64, 18, 1)
    oled.DispChar(str('       请选择 WiFi 配置'), 0, 48, 1)
    oled.show()
    while True:
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            ui.consani(0, 64, 128, 64, 0 ,0 ,128 , 64)
            oled.fill(0)
            try:
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('            请稍等...'), 0, 48, 1)
                oled.show()
                wifi.connectWiFi('TP-LINK_CD4A','13697295123')
                ntptime.settime(8, "time.windows.com")
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('            配置成功'), 0, 48, 1)
                oled.show()
                time.sleep(2)
                return
            except:
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('            配置失败'), 0, 48, 1)
                oled.show()
                while True:
                    if button_a.is_pressed():
                        return
                    elif button_b.is_pressed():
                        return
        elif touchpad_t.is_pressed() and touchpad_h.is_pressed():
            ui.consani(0, 64, 128, 64, 0 ,0 ,128 , 64)
            oled.fill(0)
            try:
                oled.Bitmap(32, 23, Flag_OS_logo, 64, 18, 1)
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('              请稍等...'), 0, 48, 1)
                oled.show()
                wifi.connectWiFi('Redmi Note 12 Turbo','12345678910')
                ntptime.settime(8, "time.windows.com")
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('             配置成功'), 0, 48, 1)
                oled.show()
                time.sleep(2)
                return
            except:
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('             配置失败'), 0, 48, 1)
                oled.show()
                while True:
                    if button_a.is_pressed():
                        return
                    elif button_b.is_pressed():
                        return
        elif touchpad_o.is_pressed() and touchpad_n.is_pressed():
            ui.consani(0, 64, 128, 64, 0 ,0 ,128 , 64)
            oled.fill(0)
            try:
                oled.Bitmap(32, 23, Flag_OS_logo, 64, 18, 1)
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('              请稍等...'), 0, 48, 1)
                oled.show()
                wifi.connectWiFi('Xiaomi_2A7A','menghan116118')
                ntptime.settime(8, "time.windows.com")
                oled.fill(0)
                oled.DispChar(str('            配置成功'), 0, 48, 1)
                oled.show()
                time.sleep(2)
                return
            except:
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('            配置失败'), 0, 48, 1)
                oled.show()
                while True:
                    if button_a.is_pressed():
                        return
                    elif button_b.is_pressed():
                        return
                        
def home():
    time.sleep_ms(20)
    while not (touchpad_t.is_pressed() and touchpad_h.is_pressed() or button_a.is_pressed() or button_b.is_pressed()):
        core.time_disposal()
        oled.fill(0)
        ui.display_font(Flag_OS.fonts.quantum, (str(core.time_hour)), 30, 18, False)
        ui.display_font(Flag_OS.fonts.quantum, (str(core.time_min)), 64, 18, False)
        oled.hline(50, 62, 30, 1)
        oled.show()
    if button_a.is_pressed():
        time.sleep(0.2)
        ui.consani(0, 0, 0, 0, 0, 0, 128, 64)
        ui.app('Flag 云端通知')
        try:
            oled.DispChar(str('正在从云端获取'), 5, 18, 2)
            oled.show()
            _response = urequests.get('https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/Notifications.fos', headers={})
            notifications = (_response.text.split(';'))
        except:
            while not button_a.is_pressed():
                oled.DispChar(str('获取失败，请重试'), 5, 18, 2)
                oled.show()
            ui.consani(0, 0, 0, 0, 0, 0, 128, 64)
        while not button_a.is_pressed():
            ui.app('Flag 云端通知')
            oled.DispChar(str(Flag_sys_notifications[1]), 5, 18, 1)
            oled.DispChar(str(Flag_sys_notifications[2]), 5, 32, 1)
            oled.DispChar(str(Flag_sys_notifications[3]), 5, 45, 1)
            oled.show()
        ui.consani(0, 0, 0, 0, 0, 0, 128, 64)
        home()
    elif button_b.is_pressed():
        ui.consani(128, 0, 128, 0, 0, 0, 128, 64)
        setings_panel()
    elif touchpad_t.is_pressed() and touchpad_h.is_pressed():
        ui.consani(64, 64, 0, 0, 0, 0, 128, 64)
        app()

def app():
    global app_list, app_num
    home_movement_x = 40
    app_num = 0
    time.sleep_ms(5)
    while not button_a.is_pressed():
        oled.fill(0)
        if str(core.get_file('./Flag_OS/data/light.fos', '\r\n')) == 'Open':
            oled.invert(1)
        else:
            oled.invert(0)
        if home_movement_x >= 0 and home_movement_x <= 118:
            if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                home_movement_x = home_movement_x + 7
            elif touchpad_o.is_pressed() and touchpad_n.is_pressed():
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
        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
            ui.consani_app(home_movement_x, 6, 36, 36, 0, 0, 128, 64, app_logo, home_movement_x + 5)
            with open("Flag_OS/apps/app_" + str(app_num) + "/main.py", "r") as f:
                exec_code = f.read()
                exec(exec_code)
    ui.consani(0, 0, 0, 0, 0, 0, 128, 64)
    home()

def about():
    oled.fill(0)
    while not button_a.is_pressed():
        oled.Bitmap(32, 12, Flag_OS_logo, 64, 18, 1)
        oled.show()
    ui.consani(0, 0, 0, 0, 0, 0, 128, 64)