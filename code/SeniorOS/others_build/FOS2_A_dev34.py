#mPythonType:0
import _thread

import gc

# 此程序使用了GxxkSystemBlockAPI（缩写GSBlockAPI）或此模块（插件）的修改版

import urequests

import json

import radio

from mpython import *

Flag_File_list_start = None

Flag_App_list = None

Flag_App_author = None

Daylight_engine_start_x = None

Daylight_engine_start_y = None

Daylight_engine_start_wide = None

Daylight_engine_start_height = None

Daylight_engine_start_fillet = None

Daylight_engine_next_app = None

Daylight_engine_app_back_button = None

Daylight_engine_open_button = None

home_icon_edge = None

home_movement_y = None

home_icon_choosen_name = None

home_movement_x = None

Daylight_engine_dome_x = None

Daylight_engine_dome_y = None

Daylight_engine_dome_wide = None

Daylight_engine_dome_height = None

def initialize():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    radio.on()
    radio.config(channel=13)
    oled.fill(0)
    Start = [0XFF,0X38,0X00,0X00,0X00,0X03,0X80,0X38,0XFF,0X38,0X00,0X00,0X00,0X0F,0XE0,0XFE, 0XFF,0X38,0X00,0X00,0X00,0X1E,0XF1,0XEF,0XE0,0X38,0X00,0X00,0X00,0X38,0X71,0X86, 0XE0,0X38,0XFC,0X3D,0X80,0X30,0X39,0X80,0XE0,0X38,0XFC,0X7F,0X80,0X30,0X39,0XE0, 0XFF,0X38,0X0E,0X63,0X80,0X30,0X38,0XFC,0XFF,0X38,0X3E,0X61,0X80,0X30,0X38,0X1E, 0XE0,0X38,0XFE,0X61,0X80,0X30,0X38,0X07,0XE0,0X39,0XCE,0X61,0X80,0X38,0X30,0X87, 0XE0,0X39,0X8E,0X73,0X80,0X3C,0XF1,0XC7,0XE0,0X3D,0XFE,0X3F,0X80,0X1F,0XE1,0XFE, 0XE0,0X1C,0XEE,0X1D,0X80,0X07,0XC0,0X78,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X73,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X3F,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X1C,0X00,0X00,0X00,0X00,]
    oled.Bitmap(32, 23, bytearray(Start), 64, 18, 1)
    oled.DispChar(str('Dev34'), 0, 48, 1)
    oled.show()
    Flag_File_list_start = '1'
    Flag_App_list = ' '
    Flag_App_author = ' '
    Daylight_engine_start_x = 0
    Daylight_engine_start_y = 0
    Daylight_engine_start_wide = 128
    Daylight_engine_start_height = 64
    Daylight_engine_start_fillet = 0
    Daylight_engine_next_app = 'null'
    # 返回按钮文案
    Daylight_engine_app_back_button = 'PY-'
    # 打开按钮文案
    Daylight_engine_open_button = 'TH-'
    # 图标大小变量
    home_icon_edge = 35
    # 桌面图标的y轴基准位置
    home_movement_y = 9
    # 选中app的名称（此变量是为了防止系统启动失败）
    home_icon_choosen_name = '暂未选择'
    # 桌面图标的x轴基准位置
    home_movement_x = 40
    Daylight_engine_dome_x = 0
    Daylight_engine_dome_y = 0
    Daylight_engine_dome_wide = 0
    Daylight_engine_dome_height = 0
    Daylight_engine_next_app = 'null'
    Daylight_engine_execute()
    WiFi()

wifi=wifi()

import network

import ntptime

import time

def WiFi():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    oled.fill(0)
    oled.Bitmap(32, 23, bytearray(Start), 64, 18, 1)
    oled.DispChar(str('       请选择 WiFi 配置'), 0, 48, 1)
    oled.show()
    while not Daylight_engine_next_app == 'lockscreen':
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            Daylight_engine_dome_x = 0
            Daylight_engine_dome_y = 64
            Daylight_engine_dome_wide = 0
            Daylight_engine_dome_height = 0
            Daylight_engine_next_app = 'null'
            for count in range(6):
                Daylight_engine_execute()
            oled.fill(0)
            try:
                oled.Bitmap(32, 23, bytearray(Start), 64, 18, 1)
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('            请稍等...'), 0, 48, 1)
                oled.show()
                wifi.connectWiFi('WiFiName','WiFiPassword')
                ntptime.settime(8, "time.windows.com")
                _thread.start_new_thread(thread_1, ())
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('            配置成功'), 0, 48, 1)
                oled.show()
                time.sleep(2)
                Daylight_engine_dome_x = 0
                Daylight_engine_dome_y = 0
                Daylight_engine_dome_wide = 0
                Daylight_engine_dome_height = 0
                Daylight_engine_next_app = 'lockscreen'
            except:
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('            配置失败'), 0, 48, 1)
                oled.show()
                while True:
                    if button_a.is_pressed():
                        initialize()
                    elif button_b.is_pressed():
                        Daylight_engine_dome_x = 128
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_next_app = 'lockscreen'
        elif touchpad_o.is_pressed() and touchpad_n.is_pressed():
            Daylight_engine_dome_x = 128
            Daylight_engine_dome_y = 64
            Daylight_engine_dome_wide = 0
            Daylight_engine_dome_height = 0
            Daylight_engine_next_app = 'null'
            Daylight_engine_execute()
            oled.fill(0)
            try:
                oled.Bitmap(32, 23, bytearray(Start), 64, 18, 1)
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('              请稍等...'), 0, 48, 1)
                oled.show()
                wifi.connectWiFi('CYSYXX','cysyxx@5322784')
                ntptime.settime(8, "time.windows.com")
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('             配置成功'), 0, 48, 1)
                oled.show()
                time.sleep(2)
                Daylight_engine_dome_x = 0
                Daylight_engine_dome_y = 0
                Daylight_engine_dome_wide = 0
                Daylight_engine_dome_height = 0
                Daylight_engine_next_app = 'lockscreen'
            except:
                oled.fill_rect(0, 48, 128, 16, 0)
                oled.DispChar(str('             配置失败'), 0, 48, 1)
                oled.show()
                while True:
                    if button_a.is_pressed():
                        initialize()
                    elif button_b.is_pressed():
                        Daylight_engine_dome_x = 128
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_next_app = 'lockscreen'
    Daylight_engine_execute()

import framebuf

import font.dvsmb_21

import font.dvsmb_12

def lockscreen():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    while not (touchpad_t.is_pressed() and touchpad_h.is_pressed()):
        Flag_Time()
        oled.fill(0)
        display_font(font.dvsmb_21, (str(Flag_H)), 35, 17, False)
        display_font(font.dvsmb_21, (':'), 65, 17, False)
        display_font(font.dvsmb_21, (str(Flag_Min)), 75, 17, False)
        display_font(font.dvsmb_12, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 50, 40, False)
        oled.hline(50, 60, 30, 1)
        oled.show()
    Daylight_engine_dome_x = 64
    Daylight_engine_dome_y = 63
    Daylight_engine_dome_wide = 0
    Daylight_engine_dome_height = 0
    Daylight_engine_next_app = 'app'
    Daylight_engine_execute()

Daylight_engine_dome_wait = None

def Daylight_engine_execute():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    gc.enable()
    gc.collect()
    Daylight_engine_dome_wait = 5
    for count in range(7):
        oled.fill_rect(Daylight_engine_dome_x, Daylight_engine_dome_y, Daylight_engine_dome_wide, Daylight_engine_dome_height, 0)
        Daylight_engine_dome_x = (Daylight_engine_dome_x - Daylight_engine_start_x) // 2
        Daylight_engine_dome_y = (Daylight_engine_dome_y - Daylight_engine_start_y) // 2
        Daylight_engine_dome_wide = (Daylight_engine_start_wide + Daylight_engine_dome_wide) // 2
        Daylight_engine_dome_height = (Daylight_engine_start_height + Daylight_engine_dome_height) // 2
        Daylight_engine_dome_wait = Daylight_engine_dome_wait + 3
        oled.rect(Daylight_engine_dome_x, Daylight_engine_dome_y, Daylight_engine_dome_wide, Daylight_engine_dome_height, 1)
        oled.show()
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            break
        time.sleep_ms(Daylight_engine_dome_wait)
    if Daylight_engine_next_app == 'app':
        app()
    elif Daylight_engine_next_app == 'lockscreen':
        lockscreen()
    elif Daylight_engine_next_app == 'WiFi':
        WiFi()
    elif Daylight_engine_next_app == 'Flag_App_ok':
        Flag_App()
    elif Daylight_engine_next_app == 'Flag_App':
        Flag_App_start()
    elif Daylight_engine_next_app == 'Flag_App_local':
        pass
    elif Daylight_engine_next_app == 'Flag_Settings':
        Flag_Settings()
    elif Daylight_engine_next_app == 'Flag_File':
        Flag_File_start()
        Flag_File()

Flag_H = None

Flag_Min = None

Flag_S = None

Flag_Time_H = None

Flag_Time_Min = None

Flag_Time_S = None

def Flag_Time():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    Flag_H = str(time.localtime()[3])
    Flag_Min = str(time.localtime()[4])
    Flag_S = str(time.localtime()[5])
    Flag_Time_H = str(time.localtime()[3])
    Flag_Time_Min = str(time.localtime()[4])
    Flag_Time_S = str(time.localtime()[5])
    if len(Flag_Time_H) < 2:
        Flag_H = '0' + str(Flag_Time_H)
    else:
        Flag_H = Flag_Time_H
    if len(Flag_Time_Min) < 2:
        Flag_Min = '0' + str(Flag_Time_Min)
    else:
        Flag_Min = Flag_Time_Min
    if len(Flag_Time_S) < 2:
        Flag_S = '0' + str(Flag_Time_S)
    else:
        Flag_S = Flag_Time_S

select_app = None

chajian_ui = None

def app():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    select_app = 'Flag'
    chajian_ui = 1
    while not (button_a.is_pressed() or Daylight_engine_app_start == 1):
        # 系统操作识别基础框架。
        # 请谨慎更改。
        if home_movement_x >= 0 and home_movement_x <= 158:
            if touchpad_y.is_pressed():
                home_movement_x = home_movement_x + 7
            elif touchpad_o.is_pressed():
                home_movement_x = home_movement_x + -7
        else:
            if home_movement_x <= 0:
                home_movement_x = 4
            elif home_movement_x >= 158:
                home_movement_x = 157
        oled.fill(0)
        oled.RoundRect(home_movement_x, home_movement_y, home_icon_edge, home_icon_edge, 7, 1)
        oled.RoundRect((home_movement_x - 40), home_movement_y, home_icon_edge, home_icon_edge, 7, 1)
        oled.RoundRect((home_movement_x - 80), home_movement_y, home_icon_edge, home_icon_edge, 7, 1)
        oled.RoundRect((home_movement_x - 120), home_movement_y, home_icon_edge, home_icon_edge, 7, 1)
        oled.DispChar(str(home_icon_choosen_name), 35, 49, 3)
        # 判断app1所处位置
        # 判断app1所处位置
        # 判断app2所处位置
        # 判断app3所处位置
        if home_movement_x >= 0 and home_movement_x <= 46:
            home_icon_choosen_name = '拓展插件'
            select_app = '拓展插件'
            # 检测手指按下的模块
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                Daylight_engine_dome_x = 64
                Daylight_engine_dome_y = 63
                Daylight_engine_dome_wide = 0
                Daylight_engine_dome_height = 0
                Daylight_engine_next_app = 'Flag_App'
                gc.enable()
                gc.collect()
                Daylight_engine_execute()
        elif home_movement_x >= 47 and home_movement_x <= 75:
            # 检测手指按下的模块
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                home_icon_choosen_name = '本地插件'
                select_app = '本地插件'
                Daylight_engine_dome_x = 64
                Daylight_engine_dome_y = 63
                Daylight_engine_dome_wide = 0
                Daylight_engine_dome_height = 0
                Daylight_engine_next_app = 'Flag_App_local'
                Daylight_engine_execute()
        elif home_movement_x >= 75 and home_movement_x <= 118:
            home_icon_choosen_name = 'Flag 文件'
            select_app = 'Flag 文件'
            # 检测手指按下的模块
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                Daylight_engine_dome_x = 64
                Daylight_engine_dome_y = 63
                Daylight_engine_dome_wide = 0
                Daylight_engine_dome_height = 0
                Daylight_engine_next_app = 'Flag_File'
                Daylight_engine_execute()
        elif home_movement_x >= 118 and home_movement_x <= 158:
            home_icon_choosen_name = '设置'
            select_app = '设置'
            # 检测手指按下的模块
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                Daylight_engine_dome_x = 64
                Daylight_engine_dome_y = 63
                Daylight_engine_dome_wide = 0
                Daylight_engine_dome_height = 0
                Daylight_engine_next_app = 'Flag_Settings'
                Daylight_engine_execute()
        oled.show()
    Daylight_engine_dome_x = 0
    Daylight_engine_dome_y = 0
    Daylight_engine_dome_wide = 0
    Daylight_engine_dome_height = 0
    Daylight_engine_next_app = 'lockscreen'
    Daylight_engine_execute()

from machine import Timer

import ubinascii

_radio_msg_list = []
def radio_callback(_msg):
    global _radio_msg_list
    try: radio_recv(_msg)
    except: pass
    if _msg in _radio_msg_list:
        eval('radio_recv_' + bytes.decode(ubinascii.hexlify(_msg)) + '()')

tim13 = Timer(13)

def timer13_tick(_):
    _msg = radio.receive()
    if not _msg: return
    radio_callback(_msg)

tim13.init(period=20, mode=Timer.PERIODIC, callback=timer13_tick)

Daylight_engine_app_start = None

def Flag_File_start():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    import os
    file = os.listdir()

def Flag_File():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    oled.fill(0)
    for count in range(4):
        oled.DispChar(str(file[Flag_File_list_start]), 0, (Flag_File_list_start-1)*16, 1)
        oled.show()
        Flag_File_list_start = Flag_File_list_start + 1
    Flag_File_list_start = 1
    oled.fill_rect(0, (Flag_File_list_start-1)*16, 128, 16, 0)
    oled.DispChar(str(file[Flag_File_list_start]), 0, (Flag_File_list_start-1)*16, 2)
    oled.show()
    while not button_a.is_pressed():
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            Flag_File_list_start = Flag_File_list_start + -1
            oled.fill_rect(0, (Flag_File_list_start-1)*16, 128, 16, 0)
            oled.DispChar(str(file[Flag_File_list_start]), 0, (Flag_File_list_start-1)*16, 2)
            oled.show()
        if Flag_File_list_start < 1:
            Flag_File_list_start = 1
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            Flag_File_list_start = Flag_File_list_start + 1
            oled.fill_rect(0, (Flag_File_list_start-1)*16, 128, 16, 0)
            oled.DispChar(str(file[Flag_File_list_start]), 0, (Flag_File_list_start-1)*16, 2)
            oled.show()
        if Flag_File_list_start > 4 and Flag_File_list_start < len(file):
            Flag_File()

Flag_App_list_start = None

def Flag_App_start():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    try:
        if len(Flag_App_list) > 1 and len(Flag_App_author) > 1:
            Flag_App()
        else:
            gc.enable()
            gc.collect()
            Flag_App_list_start = 0
            oled.fill(0)
            oled.DispChar(str('               插件库'), 0, 0, 1)
            oled.RoundRect(0, 15, 128, 100, 10, 1)
            oled.DispChar(str('正在获取'), 5, 25, 1)
            oled.show()
            _response = urequests.get('https://can1425.pemc.cn/Flag_App_list.txt', headers={})
            Flag_App_list = (_response.text.split(';'))
            gc.enable()
            gc.collect()
            _response = urequests.get('https://can1425.pemc.cn/Flag_App_author.txt', headers={})
            Flag_App_author = (_response.text.split(';'))
            Flag_App()
    except:
        oled.fill(0)
        oled.DispChar(str('               插件库'), 0, 0, 1)
        oled.RoundRect(0, 15, 128, 100, 10, 1)
        oled.DispChar(str(' :( 我们遇到了一些问题，将在 3 秒后返回'), 5, 25, 1, True)
        oled.show()
        time.sleep(4)
        Daylight_engine_dome_x = 0
        Daylight_engine_dome_y = 0
        Daylight_engine_dome_wide = 0
        Daylight_engine_dome_height = 0
        Daylight_engine_next_app = 'app'
        Daylight_engine_execute()

def init_text_file(_path):
    f = open(_path, 'w')
    f.close()

def write_data_to_file(_path, _data, _sep):
    f = open(_path, 'a')
    f.write(_data + _sep)
    f.close()

def Flag_App():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    try:
        print(Flag_App_list)
        print(Flag_App_author)
        while not button_a.is_pressed():
            gc.enable()
            gc.collect()
            oled.fill(0)
            oled.DispChar(str('               插件库'), 0, 0, 1)
            oled.RoundRect(0, 15, 128, 100, 10, 1)
            oled.DispChar(str(Flag_App_list[Flag_App_list_start]), 5, 25, 1)
            oled.DispChar(str(str('作者：') + str(Flag_App_author[Flag_App_list_start])), 5, 40, 1)
            oled.show()
            if button_b.is_pressed():
                init_text_file('app.txt')
                try:
                    gc.enable()
                    gc.collect()
                    _response = urequests.get(str('https://can1425.pemc.cn/Flag_App/') + str(str(Flag_App_list_start) + str('.txt')), headers={})
                    write_data_to_file('app.txt', _response.text, '\r\n')
                    Daylight_engine_dome_x = 64
                    Daylight_engine_dome_y = 63
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_dome_height = 0
                    Daylight_engine_next_app = 'null'
                    Daylight_engine_execute()
                    oled.fill(0)
                    oled.DispChar(str('               插件库'), 0, 0, 1)
                    oled.RoundRect(0, 15, 128, 100, 10, 1)
                    oled.DispChar(str('已将此程序缓存'), 5, 25, 1, True)
                    oled.show()
                    time.sleep(4)
                    Daylight_engine_dome_x = 0
                    Daylight_engine_dome_y = 0
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_dome_height = 0
                    Daylight_engine_next_app = 'Flag_App_ok'
                    Daylight_engine_execute()
                except:
                    oled.fill(0)
                    oled.DispChar(str('               插件库'), 0, 0, 1)
                    oled.RoundRect(0, 15, 128, 100, 10, 1)
                    oled.DispChar(str(' :( 我们遇到了一些问题，将在 3 秒后返回'), 5, 25, 1, True)
                    oled.show()
                    time.sleep(4)
                    Daylight_engine_dome_x = 0
                    Daylight_engine_dome_y = 0
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_dome_height = 0
                    Daylight_engine_next_app = 'Flag_App_ok'
                    Daylight_engine_execute()
            if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                Flag_App_list_start = Flag_App_list_start - 1
                time.sleep_ms(1)
            if touchpad_o.is_pressed() and touchpad_n.is_pressed():
                Flag_App_list_start = Flag_App_list_start + 1
                time.sleep_ms(1)
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                gc.enable()
                gc.collect()
                oled.fill(0)
                oled.DispChar(str('               插件库'), 0, 0, 1)
                oled.RoundRect(0, 15, 128, 100, 10, 1)
                oled.DispChar(str('正在获取'), 5, 25, 1)
                oled.show()
                print(Flag_App_list_start)
                try:
                    gc.enable()
                    gc.collect()
                    _response = urequests.get(str('https://can1425.pemc.cn/Flag_App/') + str(str(Flag_App_list_start) + str('.txt')), headers={})
                    Daylight_engine_dome_x = 64
                    Daylight_engine_dome_y = 63
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_dome_height = 0
                    Daylight_engine_next_app = 'null'
                    Daylight_engine_execute()
                    oled.fill(0)
                    gc.enable()
                    gc.collect()
                    radio.send('app start')
                    _thread.start_new_thread(thread_2, ())
                    exec(_response.text)
                except:
                    oled.fill(0)
                    oled.DispChar(str('               插件库'), 0, 0, 1)
                    oled.RoundRect(0, 15, 128, 100, 10, 1)
                    oled.DispChar(str(' :( 我们遇到了一些问题，将在 3 秒后返回'), 5, 25, 1, True)
                    oled.show()
                    time.sleep(4)
                    Daylight_engine_dome_x = 0
                    Daylight_engine_dome_y = 0
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_dome_height = 0
                    Daylight_engine_next_app = 'Flag_App_ok'
                    Daylight_engine_execute()
            if Flag_App_list_start < 1:
                Flag_App_list_start = 1
                time.sleep(0.5)
            if Flag_App_list_start > len(Flag_App_list):
                Flag_App_list_start = len(Flag_App_list)
                time.sleep(0.5)
        Daylight_engine_dome_x = 0
        Daylight_engine_dome_y = 0
        Daylight_engine_dome_height = 0
        Daylight_engine_dome_wide = 0
        Daylight_engine_next_app = 'app'
        Daylight_engine_execute()
    except:
        Flag_App_list_start = 0

Flag_Settings_list_start = None

def Flag_Settings():
    global Flag_H, select_app, Daylight_engine_app_start, Daylight_engine_dome_x, Flag_Min, chajian_ui, Daylight_engine_dome_y, Flag_App_list_start, Flag_Settings_list, Start, Daylight_engine_dome_wait, Flag_S, Daylight_engine_dome_wide, Flag_File_list_start, Flag_App_list, Flag_Time_H, Daylight_engine_dome_height, Flag_App_author, Flag_Settings_list_start, Flag_Time_Min, Daylight_engine_next_app, file, Flag_Time_S, home_movement_x, home_movement_y, home_icon_edge, Daylight_engine_start_x, Daylight_engine_start_y, Daylight_engine_start_wide, home_icon_choosen_name, Daylight_engine_start_height, Daylight_engine_start_fillet, Daylight_engine_app_back_button, Daylight_engine_open_button
    Flag_Settings_list = [' ', '重连网络', '同步时间', '清理内存', '系统信息', ' ']
    print(Flag_Settings_list)
    try:
        while not button_a.is_pressed():
            oled.fill(0)
            oled.DispChar(str('                 设置'), 0, 0, 1)
            oled.RoundRect(0, 15, 128, 100, 10, 1)
            oled.DispChar(str(Flag_Settings_list[Flag_Settings_list_start]), 35, 30, 1)
            oled.show()
            if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                Flag_Settings_list_start = Flag_Settings_list_start - 1
                time.sleep(0.5)
            if touchpad_o.is_pressed() and touchpad_n.is_pressed():
                Flag_Settings_list_start = Flag_Settings_list_start + 1
                time.sleep(0.5)
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                if Flag_Settings_list_start == 1:
                    Daylight_engine_dome_x = 64
                    Daylight_engine_dome_y = 63
                    Daylight_engine_dome_height = 0
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_next_app = 'WiFi'
                    Daylight_engine_execute()
                elif Flag_Settings_list_start == 2:
                    try:
                        Daylight_engine_dome_x = 64
                        Daylight_engine_dome_y = 63
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'null'
                        Daylight_engine_execute()
                        oled.fill(0)
                        oled.DispChar(str('请稍等...'), 0, 0, 1)
                        oled.show()
                        ntptime.settime(8, "time.windows.com")
                        oled.fill(0)
                        oled.DispChar(str('成功'), 0, 0, 1)
                        oled.show()
                        Daylight_engine_dome_x = 0
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'Flag_Settings'
                        Daylight_engine_execute()
                    except:
                        oled.fill(0)
                        oled.DispChar(str('失败'), 0, 0, 1)
                        oled.show()
                        Daylight_engine_dome_x = 0
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'Flag_Settings'
                        Daylight_engine_execute()
                elif Flag_Settings_list_start == 3:
                    try:
                        Daylight_engine_dome_x = 64
                        Daylight_engine_dome_y = 63
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'null'
                        Daylight_engine_execute()
                        oled.fill(0)
                        oled.DispChar(str('请稍等...'), 0, 0, 1)
                        oled.show()
                        gc.enable()
                        gc.collect()
                        oled.fill(0)
                        oled.DispChar(str('成功'), 0, 0, 1)
                        oled.show()
                        Daylight_engine_dome_x = 0
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'Flag_Settings'
                        Daylight_engine_execute()
                    except:
                        oled.fill(0)
                        oled.DispChar(str('失败'), 0, 0, 1)
                        oled.show()
                        Daylight_engine_dome_x = 0
                        Daylight_engine_dome_y = 0
                        Daylight_engine_dome_height = 0
                        Daylight_engine_dome_wide = 0
                        Daylight_engine_next_app = 'Flag_Settings'
                        Daylight_engine_execute()
                elif Flag_Settings_list_start == 4:
                    Daylight_engine_dome_x = 64
                    Daylight_engine_dome_y = 63
                    Daylight_engine_dome_height = 0
                    Daylight_engine_dome_wide = 0
                    Daylight_engine_next_app = 'null'
                    Daylight_engine_execute()
                    oled.fill(0)
                    while not button_a.is_pressed():
                        oled.Bitmap(32, 12, bytearray(Start), 44.8, 12.6, 1)
                        oled.DispChar(str('Version：2.0 Stable'), 0, 32, 1)
                        oled.DispChar(str('By Can1425'), 0, 48, 1)
                        oled.show()
                    Daylight_engine_dome_x = 0
                    Daylight_engine_dome_y = 0
                    Daylight_engine_dome_height = 0
                    Daylight_engine_dome_y = 0
                    Daylight_engine_next_app = 'Flag_Settings'
                    Daylight_engine_execute()
            if Flag_Settings_list_start < 1:
                Flag_Settings_list_start = 1
            if Flag_Settings_list_start > 4:
                Flag_Settings()
        Daylight_engine_dome_x = 0
        Daylight_engine_dome_y = 0
        Daylight_engine_dome_height = 0
        Daylight_engine_dome_wide = 0
        Daylight_engine_next_app = 'app'
        Daylight_engine_execute()
    except:
        Flag_Settings_list_start = 0
        Flag_Settings()

def thread_1():
    global Daylight_engine_open_button, Daylight_engine_app_back_button, Daylight_engine_start_fillet, Daylight_engine_start_height, home_icon_choosen_name, Daylight_engine_start_wide, Daylight_engine_start_y, Daylight_engine_start_x, home_icon_edge, home_movement_y, home_movement_x, Flag_Time_S, file, Daylight_engine_next_app, Flag_Time_Min, Flag_Settings_list_start, Flag_App_author, Daylight_engine_dome_height, Flag_Time_H, Flag_App_list, Flag_File_list_start, Daylight_engine_dome_wide, Flag_S, Daylight_engine_dome_wait, Start, Flag_Settings_list, Flag_App_list_start, Daylight_engine_dome_y, chajian_ui, Flag_Min, Daylight_engine_dome_x, Daylight_engine_app_start, select_app, Flag_H
    try:
        gc.enable()
        gc.collect()
        _response = urequests.get('https://flagos.pemc.cn/Flag_App_list.txt', headers={})
        Flag_App_list = (_response.text.split(';'))
        gc.enable()
        gc.collect()
        _response = urequests.get('https://flagos.pemc.cn/Flag_App_author.txt', headers={})
        Flag_App_author = (_response.text.split(';'))
    except:
        try:
            gc.enable()
            gc.collect()
            _response = urequests.get('https://flagos.pemc.cn/Flag_App_list.txt', headers={})
            Flag_App_list = (_response.text.split(';'))
            gc.enable()
            gc.collect()
            _response = urequests.get('https://flagos.pemc.cn/Flag_App_author.txt', headers={})
            Flag_App_author = (_response.text.split(';'))
        except:
            pass

def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

_radio_msg_list.append('app start')
def radio_recv_617070207374617274():
    global Daylight_engine_open_button, Daylight_engine_app_back_button, Daylight_engine_start_fillet, Daylight_engine_start_height, home_icon_choosen_name, Daylight_engine_start_wide, Daylight_engine_start_y, Daylight_engine_start_x, home_icon_edge, home_movement_y, home_movement_x, Flag_Time_S, file, Daylight_engine_next_app, Flag_Time_Min, Flag_Settings_list_start, Flag_App_author, Daylight_engine_dome_height, Flag_Time_H, Flag_App_list, Flag_File_list_start, Daylight_engine_dome_wide, Flag_S, Daylight_engine_dome_wait, Start, Flag_Settings_list, Flag_App_list_start, Daylight_engine_dome_y, chajian_ui, Flag_Min, Daylight_engine_dome_x, Daylight_engine_app_start, select_app, Flag_H
    Daylight_engine_app_start = 1

def thread_2():
    global Daylight_engine_open_button, Daylight_engine_app_back_button, Daylight_engine_start_fillet, Daylight_engine_start_height, home_icon_choosen_name, Daylight_engine_start_wide, Daylight_engine_start_y, Daylight_engine_start_x, home_icon_edge, home_movement_y, home_movement_x, Flag_Time_S, file, Daylight_engine_next_app, Flag_Time_Min, Flag_Settings_list_start, Flag_App_author, Daylight_engine_dome_height, Flag_Time_H, Flag_App_list, Flag_File_list_start, Daylight_engine_dome_wide, Flag_S, Daylight_engine_dome_wait, Start, Flag_Settings_list, Flag_App_list_start, Daylight_engine_dome_y, chajian_ui, Flag_Min, Daylight_engine_dome_x, Daylight_engine_app_start, select_app, Flag_H
    while True:
        if button_a.is_pressed():
            radio.send('app no')
            Daylight_engine_dome_x = 0
            Daylight_engine_dome_y = 0
            Daylight_engine_dome_wide = 0
            Daylight_engine_dome_height = 0
            import threading
            exec('thread = threading.Thread(target = doWaiting1)\\nthread.join()')
            Daylight_engine_next_app = 'Flag_App_ok'
            Daylight_engine_execute()

_radio_msg_list.append('app no')
def radio_recv_617070206e6f():
    global Daylight_engine_open_button, Daylight_engine_app_back_button, Daylight_engine_start_fillet, Daylight_engine_start_height, home_icon_choosen_name, Daylight_engine_start_wide, Daylight_engine_start_y, Daylight_engine_start_x, home_icon_edge, home_movement_y, home_movement_x, Flag_Time_S, file, Daylight_engine_next_app, Flag_Time_Min, Flag_Settings_list_start, Flag_App_author, Daylight_engine_dome_height, Flag_Time_H, Flag_App_list, Flag_File_list_start, Daylight_engine_dome_wide, Flag_S, Daylight_engine_dome_wait, Start, Flag_Settings_list, Flag_App_list_start, Daylight_engine_dome_y, chajian_ui, Flag_Min, Daylight_engine_dome_x, Daylight_engine_app_start, select_app, Flag_H
    Daylight_engine_dome_x = 0
    Daylight_engine_dome_y = 0
    Daylight_engine_dome_wide = 0
    Daylight_engine_dome_height = 0
    Daylight_engine_next_app = 'Flag_App_ok'
    Daylight_engine_execute()
initialize()
