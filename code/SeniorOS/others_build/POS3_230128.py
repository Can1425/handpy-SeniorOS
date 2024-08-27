#mPythonType:0
system_version = None

device_owner = None

from mpython import *

import network

my_wifi = wifi()

oled.fill(0)
oled.DispChar(str('POLA OS'), 0, 0, 4)
oled.DispChar(str('正在连接服务器'), 0, 16, 4)
oled.show()

my_wifi.connectWiFi("WiFiName", "WiFiPassword")

system_homemode = None

system_consani_start_x = None

system_consani_start_y = None

system_consani_start_wide = None

system_consani_start_height = None

syetem_consani_start_fillet = None

system_app_woodenfish_resetmode = None

system_app_timer_resetmode = None

home_movement_x = None

home_movement_y = None

home_icon_choosen_name = None

home_icon_edge = None

home_icon_fillet = None

app_mader_name = None

app_back_button = None

app_open_button = None

app_more_button = None

import ntptime

import time

from machine import Timer

_is_shaked = _is_thrown = False
_last_x = _last_y = _last_z = _count_shaked = _count_thrown = 0
def on_shaked():pass
def on_thrown():pass

tim11 = Timer(11)

def timer11_tick(_):
    global _is_shaked, _is_thrown, _last_x, _last_y, _last_z, _count_shaked, _count_thrown
    if _is_shaked:
        _count_shaked += 1
        if _count_shaked == 5: _count_shaked = 0
    if _is_thrown:
        _count_thrown += 1
        if _count_thrown == 10: _count_thrown = 0
        if _count_thrown > 0: return
    x=accelerometer.get_x(); y=accelerometer.get_y(); z=accelerometer.get_z()
    _is_thrown = (x * x + y * y + z * z < 0.25)
    if _is_thrown: on_thrown();return
    if _last_x == 0 and _last_y == 0 and _last_z == 0:
        _last_x = x; _last_y = y; _last_z = z; return
    diff_x = x - _last_x; diff_y = y - _last_y; diff_z = z - _last_z
    _last_x = x; _last_y = y; _last_z = z
    if _count_shaked > 0: return
    _is_shaked = (diff_x * diff_x + diff_y * diff_y + diff_z * diff_z > 1)
    if _is_shaked: on_shaked()

tim11.init(period=100, mode=Timer.PERIODIC, callback=timer11_tick)

import framebuf

import font.dvsm_21

system_consani_done_x = None

system_consani_done_y = None

system_consani_done_wide = None

system_consani_done_height = None

system_consani_done_fillet = None

import machine

import json

import urequests

app_timer_movement_x = None

app_timer_movement_y = None

app_timer_wide = None

app_timer_height = None

app_timer_fillet = None

app_timer_time_1 = None

app_timer_time_2 = None

app_timer_time_3 = None

app_timer_time_underway = None

import font.dvsmb_21

import music

def upRange(start, stop, step):
    while start <= stop:
        yield start
        start += abs(step)

def downRange(start, stop, step):
    while start >= stop:
        yield start
        start -= abs(step)

app_woodenfish_times = None

def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

def get_seni_weather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json

myUI = UI(oled)
system_version = 'Test 23.01.28'
device_owner = '将此替换为用户名'
system_homemode = 1
system_consani_start_x = 0
system_consani_start_y = 0
system_consani_start_wide = 128
system_consani_start_height = 49
syetem_consani_start_fillet = 0
system_app_woodenfish_resetmode = 0
system_app_timer_resetmode = 0
home_movement_x = 40
home_movement_y = 9
home_icon_choosen_name = '暂未选择'
home_icon_edge = 35
home_icon_fillet = 7
app_mader_name = '暂未选择'
app_back_button = 'PY-'
app_open_button = 'TH-'
app_more_button = 'ON-'
accelerometer.set_range(accelerometer.RANGE_4G)
accelerometer.set_resolution(accelerometer.RES_10_BIT)
ntptime.settime(8, "time.windows.com")
while True:
    if time.localtime()[0] > 2023 and time.localtime()[1] > 4 and time.localtime()[2] > 28:
        oled.fill(0)
        oled.DispChar(str((str(system_version) + '已停止支持')), 0, 0, 1)
        oled.DispChar(str('请升级系统'), 0, 16, 1)
        oled.DispChar(str('摇动以强制进入'), 0, 32, 1)
        oled.show()
        if _is_shaked:
            break
    elif time.localtime()[1] == 1 and time.localtime()[2] == 1:
        oled.fill(0)
        oled.DispChar(str((str(str(time.localtime()[0])) + '年')), 0, 0, 1)
        oled.DispChar(str('新年快乐！'), 0, 16, 1)
        oled.DispChar(str('摇动以进入系统'), 0, 32, 1)
        if _is_shaked:
            break
    elif time.localtime()[1] == 10 and time.localtime()[2] == 1:
        oled.fill(0)
        oled.DispChar(str((str(str(time.localtime()[0])) + '年')), 0, 0, 1)
        oled.DispChar(str('国庆快乐！'), 0, 16, 1)
        oled.DispChar(str('摇动以进入系统'), 0, 32, 1)
        oled.show()
        if _is_shaked:
            break
    else:
        break
oled.fill(0)
oled.DispChar(str('POLA OS 3'), 0, 0, 1)
oled.DispChar(str(system_version), 0, 16, 1)
oled.show()
while True:
    if system_homemode == 1:
        while True:
            oled.fill(0)
            if my_wifi.sta.isconnected():
                ntptime.settime(8, "time.windows.com")
                display_font(font.dvsm_21, (str(time.localtime()[3])), 2, 2, False)
                display_font(font.dvsm_21, (str(time.localtime()[4])), 2, 22, False)
                if time.localtime()[6]+1 == 1:
                    oled.DispChar(str(str(str(str((str(time.localtime()[1]))) + str('/')) + str((str(time.localtime()[2])))) + str(str('   ') + str('周一'))), 35, 2, 1)
                elif time.localtime()[6]+1 == 2:
                    oled.DispChar(str(str(str(str((str(time.localtime()[1]))) + str('/')) + str((str(time.localtime()[2])))) + str(str('   ') + str('周二'))), 35, 2, 1)
                elif time.localtime()[6]+1 == 3:
                    oled.DispChar(str(str(str(str((str(time.localtime()[1]))) + str('/')) + str((str(time.localtime()[2])))) + str(str('   ') + str('周三'))), 35, 2, 1)
                elif time.localtime()[6]+1 == 4:
                    oled.DispChar(str(str(str(str((str(time.localtime()[1]))) + str('/')) + str((str(time.localtime()[2])))) + str(str('   ') + str('周四'))), 35, 2, 1)
                elif time.localtime()[6]+1 == 5:
                    oled.DispChar(str(str(str(str((str(time.localtime()[1]))) + str('/')) + str((str(time.localtime()[2])))) + str(str('   ') + str('周五'))), 35, 2, 1)
                elif time.localtime()[6]+1 == 6:
                    oled.DispChar(str(str(str(str((str(time.localtime()[1]))) + str('/')) + str((str(time.localtime()[2])))) + str(str('   ') + str('周六'))), 35, 2, 1)
                elif time.localtime()[6]+1 == 7:
                    oled.DispChar(str(str(str(str((str(time.localtime()[1]))) + str('/')) + str((str(time.localtime()[2])))) + str(str('   ') + str('周日'))), 35, 2, 1)
            else:
                display_font(font.dvsm_21, '00', 2, 2, False)
                display_font(font.dvsm_21, '00', 2, 22, False)
                oled.DispChar(str('已断开WiFi'), 35, 2, 1, True)
            oled.DispChar(str((''.join([str(x) for x in [app_back_button, '重置', '|', app_open_button, '桌面']]))), 2, 49, 3)
            if device_owner == '将此替换为用户名':
                oled.DispChar(str('我的掌控板'), 35, 22, 1, True)
            else:
                if len(device_owner) <= 5:
                    oled.DispChar(str((str(device_owner) + '的掌控板')), 35, 22, 1)
                elif len(device_owner) > 5:
                    oled.DispChar(str('掌控板'), 35, 22, 1, True)
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                system_consani_done_x = 2
                system_consani_done_y = 49
                system_consani_done_wide = 126
                system_consani_done_height = 15
                system_consani_done_fillet = 0
                for count in range(7):
                    oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                    system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                    system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                    system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                    system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                    system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                    oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                    oled.show()
                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                        break
                    time.sleep_ms(7)
                system_homemode = 2
                break
            if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                while True:
                    oled.fill(0)
                    oled.DispChar(str('确认要重置吗？'), 0, 0, 1)
                    oled.DispChar(str('这将清除所有缓存。'), 0, 16, 1)
                    oled.DispChar(str('摇动以取消。'), 0, 32, 1)
                    oled.DispChar(str('PY-确认'), 2, 49, 3)
                    oled.show()
                    if _is_shaked:
                        oled.fill(0)
                        oled.DispChar(str('已取消重置。'), 0, 0, 1)
                        oled.show()
                        time.sleep(1)
                        break
                    if touchpad_p.read() + touchpad_y.read() <= 80:
                        oled.fill(0)
                        oled.DispChar(str('POLA OS 3'), 0, 0, 1)
                        oled.DispChar(str(system_version), 0, 16, 1)
                        oled.DispChar(str('正在重置'), 0, 32, 1)
                        oled.show()
                        time.sleep(1)
                        machine.reset()
            oled.show()
    if system_homemode == 2:
        while True:
            oled.fill(0)
            oled.RoundRect(home_movement_x, home_movement_y, home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 40), home_movement_y, home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 80), home_movement_y, home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 120), home_movement_y, home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 160), home_movement_y, home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 200), home_movement_y, home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.DispChar(str((''.join([str(x) for x in [app_open_button, home_icon_choosen_name, '|', app_more_button, '锁屏']]))), 35, 49, 3)
            oled.hline(0, 50, 126, 1)
            oled.show()
            if home_movement_x >= 0 and home_movement_x <= 236:
                if button_a.is_pressed():
                    home_movement_x = home_movement_x + 12
                elif button_b.is_pressed():
                    home_movement_x = home_movement_x + -12
            elif home_movement_x <= 0:
                home_movement_x = home_movement_x + 3
            elif home_movement_x >= 236:
                home_movement_x = home_movement_x + -3
            if home_movement_x >= 0 and home_movement_x <= 46:
                home_icon_choosen_name = '天气'
                app_mader_name = 'POLA'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    system_consani_done_x = home_movement_x - 0
                    system_consani_done_y = home_movement_y
                    system_consani_done_wide = home_icon_edge
                    system_consani_done_height = home_icon_edge
                    system_consani_done_fillet = home_icon_fillet
                    for count in range(7):
                        oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                        system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                        system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                        system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                        system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                        system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                        oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                        oled.show()
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        time.sleep_ms(7)
                    oled.DispChar(str((''.join([str(x) for x in [app_mader_name, ' ', home_icon_choosen_name]]))), 2, 2, 1)
                    oled.DispChar(str('可能出现兼容问题'), 2, 15, 1)
                    oled.show()
                    while True:
                        oled.fill(0)
                        oled.DispChar(str((''.join([str(x) for x in [app_back_button, '桌面', '|', home_icon_choosen_name]]))), 2, 49, 3, True)
                        oled.hline(0, 50, 126, 1)
                        if my_wifi.sta.isconnected():
                            WeatherKit = get_seni_weather("https://api.seniverse.com/v3/weather/daily.json?key=SMhSshUxuTL0GLVLS", "ip")
                            oled.DispChar(str(str(str((str(WeatherKit["results"][0]["location"]["name"]))) + str('，')) + str((str(WeatherKit["results"][0]["daily"][0]["text_day"])))), 2, 2, 1, True)
                            oled.DispChar(str(str(str(str((str(WeatherKit["results"][0]["daily"][0]["low"]))) + str('°C')) + str('~')) + str(str((str(WeatherKit["results"][0]["daily"][0]["high"]))) + str('°C'))), 2, 15, 1, True)
                        else:
                            oled.DispChar(str('已断开WiFi'), 2, 2, 1, True)
                            oled.show()
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        oled.show()
            elif home_movement_x >= 47 and home_movement_x <= 75:
                home_icon_choosen_name = '倒数'
                app_mader_name = 'POLA'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    system_consani_done_x = home_movement_x - 40
                    system_consani_done_y = home_movement_y
                    system_consani_done_wide = home_icon_edge
                    system_consani_done_height = home_icon_edge
                    system_consani_done_fillet = home_icon_fillet
                    for count in range(7):
                        oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                        system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                        system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                        system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                        system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                        system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                        oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                        oled.show()
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        time.sleep_ms(7)
                    oled.DispChar(str((''.join([str(x) for x in [app_mader_name, ' ', home_icon_choosen_name]]))), 2, 2, 1)
                    oled.DispChar(str('可能出现兼容问题'), 2, 15, 1)
                    oled.show()
                    if system_app_timer_resetmode == 0:
                        app_timer_movement_x = 0
                        app_timer_movement_y = 0
                        app_timer_wide = 48
                        app_timer_height = 35
                        app_timer_fillet = 7
                        app_timer_time_1 = 1
                        app_timer_time_2 = 3
                        app_timer_time_3 = 5
                        app_timer_time_underway = 0
                    elif system_app_timer_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        oled.DispChar(str((''.join([str(x) for x in [app_back_button, '桌面', '|', home_icon_choosen_name]]))), 2, 49, 3, True)
                        oled.hline(0, 50, 126, 1)
                        app_timer_time_underway = 0
                        oled.RoundRect((app_timer_movement_x + 0), (app_timer_movement_y + 10), app_timer_wide, app_timer_height, app_timer_fillet, 1)
                        display_font(font.dvsmb_21, (str(app_timer_time_1)), (app_timer_movement_x + 10), (app_timer_movement_y + 20), True)
                        oled.DispChar(str('min'), (app_timer_movement_x + 18), (app_timer_movement_y + 22), 1, True)
                        oled.RoundRect((app_timer_movement_x + 53), (app_timer_movement_y + 10), app_timer_wide, app_timer_height, app_timer_fillet, 1)
                        display_font(font.dvsmb_21, (str(app_timer_time_2)), (app_timer_movement_x + 63), (app_timer_movement_y + 20), True)
                        oled.DispChar(str('min'), (app_timer_movement_x + 71), (app_timer_movement_y + 22), 1, True)
                        oled.RoundRect((app_timer_movement_x + 106), (app_timer_movement_y + 10), app_timer_wide, app_timer_height, app_timer_fillet, 1)
                        display_font(font.dvsmb_21, (str(app_timer_time_3)), (app_timer_movement_x + 116), (app_timer_movement_y + 20), True)
                        oled.DispChar(str('min'), (app_timer_movement_x + 124), (app_timer_movement_y + 22), 1)
                        if app_timer_movement_x >= -124 and app_timer_movement_x <= 0:
                            if button_a.is_pressed():
                                app_timer_movement_x = app_timer_movement_x + 13
                            elif button_b.is_pressed():
                                app_timer_movement_x = app_timer_movement_x + -13
                        elif app_timer_movement_x <= -124:
                            app_timer_movement_x = app_timer_movement_x + 4
                        elif app_timer_movement_x >= 0:
                            app_timer_movement_x = app_timer_movement_x + -4
                        if app_timer_movement_x <= 0 and app_timer_movement_x >= -41:
                            oled.hline((app_timer_movement_x + 2), 47, 45, 1)
                            oled.show()
                            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                                system_consani_done_x = app_timer_movement_x + 0
                                system_consani_done_y = app_timer_movement_y + 10
                                system_consani_done_wide = app_timer_wide
                                system_consani_done_height = app_timer_height
                                system_consani_done_fillet = app_timer_fillet
                                for count in range(7):
                                    oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                                    system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                                    system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                                    system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                                    system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                                    system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                                    oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                                    oled.show()
                                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                        break
                                    time.sleep_ms(7)
                                app_timer_time_underway_start = int(app_timer_time_1 * 60)
                                for app_timer_time_underway in (app_timer_time_underway_start <= 0) and upRange(app_timer_time_underway_start, 0, -1) or downRange(app_timer_time_underway_start, 0, -1):
                                    oled.fill(0)
                                    oled.DispChar(str(str(str(app_back_button) + str('倒数')) + str(str('|') + str('一分'))), 2, 49, 3, True)
                                    oled.hline(0, 50, 126, 1)
                                    myUI.stripBar(34, 40, 60, 7, ((app_timer_time_underway / (app_timer_time_1 * 60)) * 60), 1, 1)
                                    oled.DispChar(str(str(str('倒计时还有') + str(app_timer_time_underway)) + str('秒')), 2, 2, 1, True)
                                    oled.show()
                                    if app_timer_time_underway <= 0:
                                        app_timer_time_underway = 0
                                        oled.DispChar(str(str(app_timer_time_1) + str('分钟倒计时结束了')), 2, 2, 1)
                                        oled.show()
                                        music.play('G3:2')
                                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                        break
                                    time.sleep(1)
                        elif app_timer_movement_x <= -42 and app_timer_movement_x >= -83:
                            oled.hline(((app_timer_movement_x + 53) + 2), 47, 45, 1)
                            oled.show()
                            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                                system_consani_done_x = app_timer_movement_x + 53
                                system_consani_done_y = app_timer_movement_y + 10
                                system_consani_done_wide = app_timer_wide
                                system_consani_done_height = app_timer_height
                                system_consani_done_fillet = app_timer_fillet
                                for count in range(7):
                                    oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                                    system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                                    system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                                    system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                                    system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                                    system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                                    oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                                    oled.show()
                                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                        break
                                    time.sleep_ms(7)
                                app_timer_time_underway_start = int(app_timer_time_2 * 60)
                                for app_timer_time_underway in (app_timer_time_underway_start <= 0) and upRange(app_timer_time_underway_start, 0, -1) or downRange(app_timer_time_underway_start, 0, -1):
                                    oled.fill(0)
                                    oled.DispChar(str(str(str(app_back_button) + str('倒数')) + str(str('|') + str('三分'))), 2, 49, 3, True)
                                    oled.hline(0, 50, 126, 1)
                                    myUI.stripBar(34, 40, 60, 7, ((app_timer_time_underway / (app_timer_time_2 * 60)) * 60), 1, 1)
                                    oled.DispChar(str(str(str('倒计时还有') + str(app_timer_time_underway)) + str('秒')), 2, 2, 1, True)
                                    oled.show()
                                    if app_timer_time_underway <= 0:
                                        app_timer_time_underway = 0
                                        oled.DispChar(str(str(app_timer_time_2) + str('分钟倒计时结束了')), 2, 2, 1)
                                        oled.show()
                                        music.play('G3:2')
                                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                        while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                            pass
                                        break
                                    time.sleep(1)
                        elif app_timer_movement_x <= -84 and app_timer_movement_x >= -125:
                            oled.hline(((app_timer_movement_x + 106) + 2), 47, 45, 1)
                            oled.show()
                            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                                system_consani_done_x = app_timer_movement_x + 106
                                system_consani_done_y = app_timer_movement_y + 10
                                system_consani_done_wide = app_timer_wide
                                system_consani_done_height = app_timer_height
                                system_consani_done_fillet = app_timer_fillet
                                for count in range(7):
                                    oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                                    system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                                    system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                                    system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                                    system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                                    system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                                    oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                                    oled.show()
                                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                        break
                                    time.sleep_ms(7)
                                app_timer_time_underway_start = int(app_timer_time_3 * 60)
                                for app_timer_time_underway in (app_timer_time_underway_start <= 0) and upRange(app_timer_time_underway_start, 0, -1) or downRange(app_timer_time_underway_start, 0, -1):
                                    oled.fill(0)
                                    oled.DispChar(str(str(str(app_back_button) + str('倒数')) + str(str('|') + str('三分'))), 2, 49, 3, True)
                                    oled.hline(0, 50, 126, 1)
                                    myUI.stripBar(34, 40, 60, 7, ((app_timer_time_underway / (app_timer_time_3 * 60)) * 60), 1, 1)
                                    oled.DispChar(str(str(str('倒计时还有') + str(app_timer_time_underway)) + str('秒')), 2, 2, 1, True)
                                    oled.show()
                                    if app_timer_time_underway <= 0:
                                        app_timer_time_underway = 0
                                        oled.DispChar(str(str(app_timer_time_3) + str('分钟倒计时结束了')), 2, 2, 1)
                                        oled.show()
                                        music.play('G3:2')
                                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                        while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                            pass
                                        break
                                    time.sleep(1)
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
                        oled.show()
            elif home_movement_x >= 75 and home_movement_x <= 118:
                home_icon_choosen_name = '木鱼'
                app_mader_name = 'POLA'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    system_consani_done_x = home_movement_x - 80
                    system_consani_done_y = home_movement_y
                    system_consani_done_wide = home_icon_edge
                    system_consani_done_height = home_icon_edge
                    system_consani_done_fillet = home_icon_fillet
                    for count in range(7):
                        oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                        system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                        system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                        system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                        system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                        system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                        oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                        oled.show()
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        time.sleep_ms(7)
                    oled.DispChar(str((''.join([str(x) for x in [app_mader_name, ' ', home_icon_choosen_name]]))), 2, 2, 1)
                    oled.show()
                    if system_app_woodenfish_resetmode == 0:
                        app_woodenfish_times = 0
                        system_app_woodenfish_resetmode = 1
                    elif system_app_woodenfish_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        oled.DispChar(str((''.join([str(x) for x in [app_back_button, '桌面', '|', home_icon_choosen_name]]))), 2, 49, 3, True)
                        oled.hline(0, 50, 126, 1)
                        oled.DispChar(str('摇一摇。'), 2, 2, 1, True)
                        oled.DispChar(str('敲电子木鱼,取赛博真经。'), 2, 15, 1, True)
                        oled.DispChar(str(str(str('今天已经敲了') + str(app_woodenfish_times)) + str('次。')), 2, 28, 1, True)
                        if _is_shaked:
                            music.play('C3:1')
                            app_woodenfish_times = app_woodenfish_times + 1
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
                        oled.show()
            elif home_movement_x >= 119 and home_movement_x <= 162:
                home_icon_choosen_name = '夜灯'
                app_mader_name = '胥正杰'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    system_consani_done_x = home_movement_x - 120
                    system_consani_done_y = home_movement_y
                    system_consani_done_wide = home_icon_edge
                    system_consani_done_height = home_icon_edge
                    system_consani_done_fillet = home_icon_fillet
                    for count in range(7):
                        oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                        system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                        system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                        system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                        system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                        system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                        oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                        oled.show()
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        time.sleep_ms(7)
                    oled.DispChar(str((''.join([str(x) for x in [app_mader_name, ' ', home_icon_choosen_name]]))), 2, 2, 1)
                    oled.show()
                    while True:
                        oled.fill(0)
                        oled.DispChar(str((''.join([str(x) for x in [app_back_button, '桌面', '|', home_icon_choosen_name]]))), 2, 49, 3, True)
                        oled.hline(0, 50, 126, 1)
                        oled.DispChar(str('声音：'), 5, 2, 1, True)
                        oled.DispChar(str('光线：'), 5, 25, 1, True)
                        myUI.ProgressBar(35, 6, 70, 9, ((100 - 0) / (4095 - 0)) * (sound.read() - 0) + 0)
                        myUI.ProgressBar(35, 29, 70, 9, ((100 - 0) / (4095 - 0)) * (light.read() - 0) + 0)
                        oled.show()
                        if sound.read() > light.read() * 100:
                            rgb.fill((int(255), int(255), int(153)))
                            rgb.write()
                            time.sleep_ms(1)
                        else:
                            rgb.fill( (0, 0, 0) )
                            rgb.write()
                            time.sleep_ms(1)
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
            elif home_movement_x >= 163 and home_movement_x <= 206:
                home_icon_choosen_name = '系统'
                app_mader_name = 'POLA'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    system_consani_done_x = home_movement_x - 160
                    system_consani_done_y = home_movement_y
                    system_consani_done_wide = home_icon_edge
                    system_consani_done_height = home_icon_edge
                    system_consani_done_fillet = home_icon_fillet
                    for count in range(7):
                        oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                        system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                        system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                        system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                        system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                        system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                        oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                        oled.show()
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        time.sleep_ms(7)
                    oled.DispChar(str((''.join([str(x) for x in [app_mader_name, ' ', home_icon_choosen_name]]))), 2, 2, 1)
                    oled.show()
                    while True:
                        oled.fill(0)
                        oled.DispChar(str((''.join([str(x) for x in [app_back_button, '桌面', '|', home_icon_choosen_name]]))), 2, 49, 3, True)
                        oled.hline(0, 50, 126, 1)
                        oled.DispChar(str('POLA OS 3'), 2, 2, 1, True)
                        oled.DispChar(str(system_version), 2, 15, 1, True)
                        oled.DispChar(str('到期时间：2023.4.27'), 2, 28, 1, True)
                        oled.show()
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
            elif home_movement_x >= 207 and home_movement_x <= 250:
                home_icon_choosen_name = '求救'
                app_mader_name = 'POLA'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    system_consani_done_x = home_movement_x - 200
                    system_consani_done_y = home_movement_y
                    system_consani_done_wide = home_icon_edge
                    system_consani_done_height = home_icon_edge
                    system_consani_done_fillet = home_icon_fillet
                    for count in range(7):
                        oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                        system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                        system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                        system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                        system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                        system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                        oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                        oled.show()
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        time.sleep_ms(7)
                    oled.DispChar(str((''.join([str(x) for x in [app_mader_name, ' ', home_icon_choosen_name]]))), 2, 2, 1)
                    oled.show()
                    while True:
                        oled.fill(0)
                        oled.DispChar(str((''.join([str(x) for x in [app_back_button, '桌面', '|', home_icon_choosen_name]]))), 2, 49, 2, True)
                        for count in range(3):
                            oled.fill(1)
                            oled.show()
                            rgb.fill((int(255), int(0), int(0)))
                            rgb.write()
                            time.sleep_ms(1)
                            music.play('B5:2')
                            time.sleep(0.3)
                            oled.fill(0)
                            oled.show()
                            rgb.fill( (0, 0, 0) )
                            rgb.write()
                            time.sleep_ms(1)
                            time.sleep(0.3)
                            if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                break
                        time.sleep(0.7)
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        oled.show()
            if touchpad_o.read() + touchpad_n.read() <= 80:
                system_consani_done_x = 2
                system_consani_done_y = 49
                system_consani_done_wide = 126
                system_consani_done_height = 15
                system_consani_done_fillet = 0
                for count in range(7):
                    oled.fill_rect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, 0)
                    system_consani_done_x = (system_consani_done_x - system_consani_start_x) // 2
                    system_consani_done_y = (system_consani_done_y - system_consani_start_y) // 2
                    system_consani_done_wide = (system_consani_start_wide + system_consani_done_wide) // 2
                    system_consani_done_height = (system_consani_start_height + system_consani_done_height) // 2
                    system_consani_done_fillet = (system_consani_done_fillet - syetem_consani_start_fillet) // 2
                    oled.RoundRect(system_consani_done_x, system_consani_done_y, system_consani_done_wide, system_consani_done_height, system_consani_done_fillet, 1)
                    oled.show()
                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                        break
                    time.sleep_ms(7)
                system_homemode = 1
                break
            rgb.fill( (0, 0, 0) )
            rgb.write()
            time.sleep_ms(1)
