from mpython import *
import flagos.system.core
import ntptime
import network
import time
import framebuf
import font.dvsmb_21
import urequests
import json
import math
import gc

time_hour = 0
time_min = 0
sys_hour = 0
sys_min = 0

def time_disposal():
    global time_hour, time_min
    time_hour = str(time.localtime()[3])
    time_min = str(time.localtime()[4])
    sys_hour = str(time.localtime()[3])
    sys_min = str(time.localtime()[4])
    if len(sys_hour) < 2:
        time_hour = '0' + str(sys_hour)
    else:
        time_hour = sys_hour
    if len(sys_min) < 2:
        time_min = '0' + str(sys_min)
    else:
        time_min = sys_min

wifi=wifi()
Flag_plugins_list = []
Flag_plugins_tip = []
Flag_app_list = [' ', 'Flag 设置', 'Flag 线上插件', 'Flag 文件']
Flag_app_tip = [' ', 'Flag OS 设置', '线上拓展插件', 'Flag OS 文件操作']
Flag_setings_panel_list = [' ', '亮度', '音量', '日光模式']

def WIFI(flag_wifi_name, flag_wifi_password):
    oled.fill(0)
    oled.show()
    oled.Bitmap(0, 0, bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X60,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X1F,0XFC,0XE0,0X00,0X00,0X00,0X01,0XFF,0X01,0XFF,0X00,0X00,0X00, 0X00,0X00,0X00,0X1F,0XFC,0XE0,0X00,0X00,0X00,0X03,0XFF,0X83,0XFF,0X00,0X00,0X00, 0X00,0X00,0X00,0X18,0X00,0XE0,0X00,0X00,0X00,0X07,0X83,0XC7,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XE0,0X00,0X00,0X00,0X0E,0X01,0XC6,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XE3,0XF0,0X0F,0XF0,0X0E,0X01,0XCE,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XC3,0XFC,0X1F,0XF0,0X0C,0X01,0XCE,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X38,0X00,0XC0,0X3C,0X3C,0X70,0X1C,0X01,0XC7,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC0,0X0E,0X70,0X70,0X1C,0X01,0XC7,0XF8,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC0,0X0E,0X70,0X70,0X1C,0X01,0XC1,0XFE,0X00,0X00,0X00, 0X00,0X00,0X00,0X3F,0XF1,0XC7,0XFC,0X70,0X70,0X1C,0X01,0XC0,0X1E,0X00,0X00,0X00, 0X00,0X00,0X00,0X30,0X01,0XCF,0XFC,0X60,0X60,0X1C,0X01,0XC0,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0XCC,0X0C,0X60,0X60,0X1C,0X01,0X80,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0XDC,0X1C,0X70,0XE0,0X1C,0X03,0X80,0X0E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X9C,0X1C,0X70,0XE0,0X1E,0X07,0X00,0X1E,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X8F,0XFC,0X7F,0XE0,0X0F,0XFF,0X1F,0XFC,0X00,0X00,0X00, 0X00,0X00,0X00,0X70,0X01,0X87,0XFC,0X3F,0XE0,0X07,0XFC,0X1F,0XF8,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XE0,0X00,0X40,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X01,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,]), 128, 64, 1)
    oled.show()
    wifi.connectWiFi(flag_wifi_name, flag_wifi_password)
    ntptime.settime(8, "ntp.aliyun.com")
    home()

def home():
    global time_hour, time_min
    time.sleep_ms(10)
    while not (touchpad_t.is_pressed() and touchpad_h.is_pressed() or button_a.is_pressed() or button_b.is_pressed()):
        time_disposal()
        oled.fill(0)
        flagos.system.core.display_font(font.dvsmb_21, (str(time_hour)), 34, 20, False)
        flagos.system.core.display_font(font.dvsmb_21, (':'), 61, 20, False)
        flagos.system.core.display_font(font.dvsmb_21, (str(time_min)), 68, 20, False)
        oled.hline(50, 62, 30, 1)
        oled.show()
    if button_a.is_pressed():
        time.sleep(0.2)
        flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
        flagos.system.core.ui_app('Flag 云端通知')
        try:
            oled.DispChar(str('正在从云端获取'), 5, 18, 2)
            oled.show()
            _response = urequests.get('https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/Notifications.fos', headers={})
            Flag_sys_notifications = (_response.text.split(';'))
        except:
            while not button_a.is_pressed():
                oled.DispChar(str('获取失败，请重试'), 5, 18, 2)
                oled.show()
            flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
        while not button_a.is_pressed():
            flagos.system.core.ui_app('Flag 云端通知')
            oled.DispChar(str(Flag_sys_notifications[1]), 5, 18, 1)
            oled.DispChar(str(Flag_sys_notifications[2]), 5, 32, 1)
            oled.DispChar(str(Flag_sys_notifications[3]), 5, 45, 1)
            oled.show()
        flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
        home()
    elif button_b.is_pressed():
        flagos.system.core.consani(128, 0, 128, 0, 0, 0, 128, 64)
        setings_panel()
    elif touchpad_t.is_pressed() and touchpad_h.is_pressed():
        flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
        app()

def setings_panel():
    Flag_setings_panel_tip = [' ', flagos.system.core.get_file('./flagos/data/Flag_sys_ui_brightness.fos', '\r\n'), flagos.system.core.get_file('./flagos/data/Flag_sys_ui_volume.fos', '\r\n'), flagos.system.core.get_file('./flagos/data/Flag_sys_ui_light.fos', '\r\n')]
    if Flag_settings_panel_num == 0:
        Flag_settings_panel_num = 1
    time.sleep_ms(5)
    while not button_a.is_pressed():
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            Flag_settings_panel_num = Flag_settings_panel_num + 1
            if Flag_settings_panel_num > len(Flag_setings_panel_list) - 1:
                Flag_settings_panel_num = len(Flag_setings_panel_list) - 1
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            Flag_settings_panel_num = Flag_settings_panel_num + -1
            if Flag_settings_panel_num < 1:
                Flag_settings_panel_num = 1
        flagos.system.core.ui_app('控制面板')
        oled.DispChar(str(Flag_setings_panel_tip[Flag_settings_panel_num]), 5, 18, 1, True)
        oled.DispChar(str(Flag_setings_panel_list[Flag_settings_panel_num]), 5, 45, 1)
        oled.DispChar(str((''.join([str(x) for x in [Flag_settings_panel_num, '/', len(Flag_setings_panel_list) - 1]]))), 105, 45, 1)
        oled.show()
        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
            if Flag_settings_panel_num == 1:
                Flag_setings_panel_brightness()
            if Flag_settings_panel_num == 2:
                Flag_setings_panel_volume()
            if Flag_settings_panel_num == 3:
                Flag_setings_panel_daylight()
            time.sleep(0.5)
    flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
    home()

def setings_panel_daylight():
    while button_a.is_pressed():
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            flagos.system.core.init_file('./flagos/data/Flag_sys_ui_light.fos')
            flagos.system.core.write_file('./flagos/data/Flag_sys_ui_light.fos', 'Open', '\r\n')
            oled.DispChar(str(('日光模式：' + str(flagos.system.core.get_file('./flagos/data/Flag_sys_ui_light.fos', '\r\n')))), 5, 45, 1)
            oled.invert(0)
            oled.show()
            time.sleep(0.5)
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            flagos.system.core.init_file('./flagos/data/Flag_sys_ui_light.fos')
            flagos.system.core.write_file('./flagos/data/Flag_sys_ui_light.fos', 'Close', '\r\n')
            oled.DispChar(str(('日光模式：' + str(flagos.system.core.get_file('./flagos/data/Flag_sys_ui_light.fos', '\r\n')))), 5, 45, 1)
            oled.invert(1)
            oled.show()
            time.sleep(0.5)
    time.sleep(0.5)

def setings_panel_volume():
    while button_a.is_pressed():
        Flag_sys_volume = int(flagos.system.core.get_file('./flagos/data/Flag_sys_volume.fos', '\r\n'))
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            flagos.system.core.init_file('./flagos/data/Flag_sys_volume.fos')
            flagos.system.core.write_file('./flagos/data/Flag_sys_volume.fos', 'Flag_sys_volume - 20', '\r\n')
            time.sleep(0.5)
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            flagos.system.core.init_file('./flagos/data/Flag_sys_volume.fos')
            flagos.system.core.write_file('./flagos/data/Flag_sys_volume.fos', 'Flag_sys_volume + 20', '\r\n')
            time.sleep(0.5)
        if Flag_sys_volume < 15:
            Flag_sys_volume = 15
            time.sleep(0.5)
        if Flag_sys_volume > 255:
            Flag_sys_volume = 255
            time.sleep(0.5)
        oled.DispChar(str((''.join([str(x) for x in ['音量', '：', round(((100 - 0) / (255 - 0)) * (Flag_sys_volume - 0) + 0), '%']]))), 5, 18, 1)
        oled.show()
    time.sleep(0.5)

def setings_panel_brightness():
    while button_a.is_pressed():
        Flag_sys_brightness = int(flagos.system.core.get_file('./flagos/data/Flag_sys_brightness.fos', '\r\n'))
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            flagos.system.core.init_file('./flagos/data/Flag_sys_brightness.fos')
            flagos.system.core.write_file('./flagos/data/Flag_sys_brightness.fos', 'Flag_sys_brightness - 20', '\r\n')
            time.sleep(0.5)
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            flagos.system.core.init_file('./flagos/data/Flag_sys_brightness.fos')
            flagos.system.core.write_file('./flagos/data/Flag_sys_brightness.fos', 'Flag_sys_brightness + 20', '\r\n')
            time.sleep(0.5)
        if Flag_sys_brightness < 15:
            Flag_sys_brightness = 15
            time.sleep(0.5)
        if Flag_sys_brightness > 255:
            Flag_sys_brightness = 255
            time.sleep(0.5)
        oled.contrast(Flag_sys_brightness)
        oled.DispChar(str((''.join([str(x) for x in ['亮度', '：', round(((100 - 0) / (255 - 0)) * (Flag_sys_brightness - 0) + 0), '%']]))), 5, 18, 1)
        oled.show()

def app():
    global Flag_app_list, Flag_app_num
    home_movement_x = 40
    Flag_app_num = 1
    time.sleep_ms(5)
    while not button_a.is_pressed():
        oled.fill(0)
        if str(flagos.system.core.get_file('./flagos/data/Flag_sys_ui_light.fos', '\r\n')) == 'Open':
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
        oled.DispChar(str(Flag_app_list[Flag_app_num]), 35, 45, 3)
        oled.hline(50, 62, 30, 1)
        if home_movement_x >= 0 and home_movement_x <= 46:
            Flag_app_num = 1
        elif home_movement_x >= 47 and home_movement_x <= 85:
            Flag_app_num = 2
        elif home_movement_x >= 85 and home_movement_x <= 118:
            Flag_app_num = 3
        oled.show()
        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
            flagos.system.core.consani(home_movement_x, 6, 36, 36, 0, 0, 128, 64)
            exec((str(flagos.system.core.get_file('./flagos/apps/app_' + str(Flag_app_num) + '.main.py', '\r\n'))))
    flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
    home()

    def about():
        oled.fill(0)
        while not button_a.is_pressed():
            oled.Bitmap(32, 12, bytearray([0XFF,0X38,0X00,0X00,0X00,0X03,0X80,0X38,0XFF,0X38,0X00,0X00,0X00,0X0F,0XE0,0XFE, 0XFF,0X38,0X00,0X00,0X00,0X1E,0XF1,0XEF,0XE0,0X38,0X00,0X00,0X00,0X38,0X71,0X86, 0XE0,0X38,0XFC,0X3D,0X80,0X30,0X39,0X80,0XE0,0X38,0XFC,0X7F,0X80,0X30,0X39,0XE0, 0XFF,0X38,0X0E,0X63,0X80,0X30,0X38,0XFC,0XFF,0X38,0X3E,0X61,0X80,0X30,0X38,0X1E, 0XE0,0X38,0XFE,0X61,0X80,0X30,0X38,0X07,0XE0,0X39,0XCE,0X61,0X80,0X38,0X30,0X87, 0XE0,0X39,0X8E,0X73,0X80,0X3C,0XF1,0XC7,0XE0,0X3D,0XFE,0X3F,0X80,0X1F,0XE1,0XFE, 0XE0,0X1C,0XEE,0X1D,0X80,0X07,0XC0,0X78,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X73,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X3F,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X1C,0X00,0X00,0X00,0X00,]), 64, 18, 1)
            oled.DispChar(str('Flag OS 2.0 (240202006[mXDF])'), 0, 32, 1, True)
            oled.show()
        flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)