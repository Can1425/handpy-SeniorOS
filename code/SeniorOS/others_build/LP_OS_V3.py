from SeniorOS.lib.devlib import *

SET = None

p0 = MPythonPin(0, PinMode.OUT)

p1 = MPythonPin(1, PinMode.OUT)

p13 = MPythonPin(13, PinMode.OUT)

p15 = MPythonPin(15, PinMode.OUT)

set2 = None

import neopixel

p0 = MPythonPin(0, PinMode.IN)

p1 = MPythonPin(1, PinMode.IN)

p13 = MPythonPin(13, PinMode.IN)

p15 = MPythonPin(15, PinMode.IN)

def WLAN():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        oled.DispChar(str('P/引脚普通操作'), 15, 11, 1)
        oled.DispChar(str('Y/灯带操作'), 15, 26, 1)
        oled.DispChar(str('T/读取引脚'), 15, 41, 1)
        oled.show()
        if touchpad_p.is_pressed():
            while not touchpad_n.is_pressed():
                oled.fill_rect(10, 10, 100, 50, 0)
                oled.RoundRect(10, 10, 100, 50, 10, 1)
                oled.DispChar(str(str('P/切换 当前:') + str(SET)), 15, 11, 1)
                oled.DispChar(str('Y/执行 N/退出'), 15, 26, 1)
                oled.DispChar(str(str('T/切换引脚') + str(set2)), 15, 41, 1)
                oled.show()
                if touchpad_p.is_pressed():
                    if SET == 'OFF':
                        SET = 'ON'
                    elif SET == 'ON':
                        SET = 'OFF'
                if touchpad_y.is_pressed():
                    if set2 == 0:
                        if SET == 'OFF':
                            p0.write_digital(0)
                        elif SET == 'ON':
                            p0.write_digital(1)
                    elif set2 == 1:
                        if SET == 'OFF':
                            p1.write_digital(0)
                        elif SET == 'ON':
                            p1.write_digital(1)
                    elif set2 == 2:
                        if SET == 'OFF':
                            p13.write_digital(0)
                        elif SET == 'ON':
                            p13.write_digital(1)
                    elif set2 == 3:
                        if SET == 'OFF':
                            p15.write_digital(0)
                        elif SET == 'ON':
                            p15.write_digital(1)
                if touchpad_t.is_pressed():
                    set2 = set2 + 1
                    if set2 > 4:
                        set2 = 0
                if set2 == 2:
                    set2 = 13
                if set2 == 14:
                    set2 = 15
                if set2 == 16:
                    set2 = 0
        if touchpad_y.is_pressed():
            while not touchpad_n.is_pressed():
                oled.fill_rect(10, 10, 100, 50, 0)
                oled.RoundRect(10, 10, 100, 50, 10, 1)
                oled.DispChar(str(str('P/切换 当前:') + str(SET)), 15, 11, 1)
                oled.DispChar(str('Y/执行 N/退出'), 15, 26, 1)
                oled.show()
                if touchpad_p.is_pressed():
                    if SET == 'OFF':
                        SET = 'ON'
                    elif SET == 'ON':
                        SET = 'OFF'
                if touchpad_y.is_pressed():
                    if SET == 'OFF':
                        my_rgb.fill( (0, 0, 0) )
                        my_rgb.write()
                        my_rgb.write()
                    elif SET == 'ON':
                        my_rgb.fill( (255, 255, 255) )
                        my_rgb.brightness(50 / 100)
                        my_rgb.write()
        if touchpad_t.is_pressed():
            while not touchpad_n.is_pressed():
                oled.fill_rect(10, 10, 100, 50, 0)
                oled.RoundRect(10, 10, 100, 50, 10, 1)
                oled.DispChar(str(str('P/切换引脚') + str(set2)), 15, 11, 1)
                oled.DispChar(str('N/退出'), 15, 26, 1)
                oled.show()
                if set2 == 0:
                    oled.DispChar(str((''.join([str(x) for x in ['从引脚P', set2, '接收到:', p0.read_digital()]]))), 15, 41, 1)
                    oled.show()
                elif set2 == 1:
                    oled.DispChar(str((''.join([str(x) for x in ['从引脚P', set2, '接收到:', p1.read_digital()]]))), 15, 41, 1)
                    oled.show()
                elif set2 == 13:
                    oled.DispChar(str((''.join([str(x) for x in ['从引脚P', set2, '接收到:', p13.read_digital()]]))), 15, 41, 1)
                    oled.show()
                elif set2 == 15:
                    oled.DispChar(str((''.join([str(x) for x in ['从引脚P', set2, '接收到:', p15.read_digital()]]))), 15, 41, 1)
                    oled.show()
                if touchpad_p.is_pressed():
                    set2 = set2 + 1
                if set2 == 2:
                    set2 = 13
                if set2 == 14:
                    set2 = 15
                if set2 == 16:
                    set2 = 0

import network

my_wifi = wifi()

my_wifi.connectWiFi("WiFiName", "WiFiPassword")

import ntptime

my_rgb = neopixel.NeoPixel(Pin(Pin.P13), n=24, bpp=3, timing=1)

list = None

ver = None

xuanquruanjian2 = None

WENBEN = None

C = None

EMM = None

word = None

A = None

H = None

set3 = None

M = None

USER = None

jibu = None

xuenquruanjian = None

kaishicaidanxuanquruanjian = None

shibiejieguo = None

import time

def Deskop():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    my_1()

def on_button_b_pressed(_):
    global shibiejieguo, kaishicaidanxuanquruanjian, xuenquruanjian, jibu, USER, set3, word, EMM, C, SET, set2, WENBEN, xuanquruanjian2, A, ver, H, list, M
    Deskop()

button_b.event_pressed = on_button_b_pressed

import audio

import urequests

def _E8_AF_AD_E9_9F_B3_E8_AF_86_E5_88_AB():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        oled.DispChar(str('按A键识别'), 15, 11, 1)
        oled.show()
        if button_a.is_pressed():
            rgb[0] = (int(255), int(0), int(0))
            rgb.write()
            time.sleep_ms(1)
            audio.recorder_init(i2c)
            audio.record('1.wav', 2)
            audio.recorder_deinit()
            rgb[0] = (int(51), int(255), int(51))
            rgb.write()
            time.sleep_ms(1)
            xunfei_params = {"APPID":'5eb94a71', "APISecret":'baa68983acf0b2d3e646ca1ae465db14', "APIKey":'3461bdfede39b22ce93afa25c7371f99'}
            _rsp = urequests.post("http://119.23.66.134:8085/xunfei_iat", files={"file":('1.wav', "audio/wav")}, params=xunfei_params)
            try:
                xunfei_iat_result = _rsp.json()
            except:
                xunfei_iat_result = {"text":""}
            while not touchpad_p.is_pressed():
                oled.DispChar(str((xunfei_iat_result["text"])), 15, 26, 1)
                oled.DispChar(str('按P键返回'), 15, 41, 1)
                oled.show()

def clock():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    while not button_b.is_pressed():
        if M < 0:
            M = 59
        elif M > 59:
            M = 0
        if H < 0:
            H = 23
        elif H > 23:
            H = 0
        if A < 0:
            A = 0
        elif A > 1:
            A = 1
        if accelerometer.get_x() < -0.3:
            if A == 0:
                H = H + 1
            elif A == 1:
                M = M + 5
        elif accelerometer.get_x() > 0.3:
            if A == 0:
                H = H + -1
            elif A == 1:
                M = M + -5
        if accelerometer.get_y() > 0.3:
            A = A + -1
        elif accelerometer.get_y() < -0.3:
            A = A + 1
        if A == 0:
            oled.DispChar(str('时'), 15, 26, 1)
            oled.show()
        elif A == 1:
            oled.DispChar(str('分'), 15, 26, 1)
            oled.show()
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        oled.DispChar(str(str('闹钟:') + str((str(str('时') + str(str(H) + str('/'))) + str(str('分') + str(M))))), 15, 11, 1)
        oled.show()

import json

def init_text_file(_path):
    f = open(_path, 'w')
    f.close()

def write_data_to_file(_path, _data, _sep):
    f = open(_path, 'a')
    f.write(_data + _sep)
    f.close()

import machine

def update():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    rgb[0] = (int(51), int(255), int(51))
    rgb.write()
    time.sleep_ms(1)
    _response = urequests.get('https://lplplplplplplp.github.io/LP-OS/System', headers={})
    rgb[1] = (int(51), int(255), int(51))
    rgb.write()
    time.sleep_ms(1)
    init_text_file('main.py')
    rgb[2] = (int(51), int(255), int(51))
    rgb.write()
    time.sleep_ms(1)
    write_data_to_file('main.py', _response.text, '\r\n')
    machine.reset()

def _E5_BC_80_E5_A7_8B():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(30, 0, 55, 45, 0)
        oled.RoundRect(30, 0, 60, 45, 10, 1)
        oled.vline(40, 48, 30, 1)
        oled.vline(60, 48, 30, 1)
        oled.DispChar(str('即将重启'), 35, 4, 1)
        oled.DispChar(str('A/是 B/否'), 35, 20, 1)
        oled.hline(0, 48, 150, 1)
        oled.show()
        if button_a.is_pressed():
            machine.reset()

def _E8_AE_BE_E7_BD_AE():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        _response = urequests.get('https://lplplplplplplp.github.io/LP-OS/version', headers={})
        oled.DispChar(str(str('最新版本:') + str(_response.text)), 15, 11, 1)
        oled.DispChar(str('当前版本:3.0'), 15, 26, 1)
        if ver == _response.text[ : 3]:
            oled.DispChar(str('你已是最新版本'), 15, 41, 1)
            oled.show()
        elif ver != _response.text[ : 3]:
            oled.DispChar(str('按A键开始更新'), 15, 41, 1)
            oled.show()
            if button_a.is_pressed():
                rgb.fill((int(255), int(0), int(0)))
                rgb.write()
                time.sleep_ms(1)
                update()
        oled.show()

import music

def my_1():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    while not list == 1:
        oled.fill(0)
        oled.DispChar(str('语音识别'), 3, 2, 1)
        oled.DispChar(str('设置'), 61, 2, 1)
        oled.DispChar(str('时间'), 3, 21, 1)
        oled.DispChar(str('天气'), 41, 21, 1)
        oled.DispChar(str('引脚'), 76, 21, 1)
        oled.rect(2, 2, 50, 15, 1)
        oled.rect(60, 2, 30, 15, 1)
        oled.rect(2, 20, 30, 15, 1)
        oled.rect(40, 20, 30, 15, 1)
        oled.rect(75, 20, 30, 15, 1)
        oled.DispChar(str('              LP '), 0, 48, 1)
        oled.hline(0, 48, 150, 1)
        oled.vline(40, 48, 30, 1)
        oled.vline(60, 48, 30, 1)
        oled.show()
        if accelerometer.get_x() < -0.3:
            _E5_BC_80_E5_A7_8B()
        if xuenquruanjian < 0:
            xuenquruanjian = 4
        elif xuenquruanjian > 4:
            xuenquruanjian = 0
        if accelerometer.get_y() > 0.3:
            xuenquruanjian = xuenquruanjian + -1
        elif accelerometer.get_y() < -0.3:
            xuenquruanjian = xuenquruanjian + 1
        if button_a.is_pressed():
            if xuenquruanjian == 0:
                _E8_AF_AD_E9_9F_B3_E8_AF_86_E5_88_AB()
            elif xuenquruanjian == 1:
                _E8_AE_BE_E7_BD_AE()
            elif xuenquruanjian == 2:
                clock()
            elif xuenquruanjian == 3:
                _E5_A4_A9_E6_B0_94()
            elif xuenquruanjian == 4:
                WLAN()
        if xuenquruanjian == 0:
            oled.fill_rect(2, 2, 50, 15, 1)
            oled.show()
        elif xuenquruanjian == 1:
            oled.fill_rect(60, 2, 30, 15, 1)
            oled.show()
        elif xuenquruanjian == 2:
            oled.fill_rect(2, 20, 30, 15, 1)
            oled.show()
        elif xuenquruanjian == 3:
            oled.fill_rect(40, 20, 30, 15, 1)
            oled.show()
        elif xuenquruanjian == 4:
            oled.fill_rect(75, 20, 30, 15, 1)
            oled.show()
        if time.localtime()[3] == H and time.localtime()[4] == M and my_wifi.sta.isconnected():
            music.play(music.DONG_FANG_HONG, wait=False, loop=False)

def _E5_A4_A9_E6_B0_94():
    global M, list, H, ver, A, xuanquruanjian2, WENBEN, set2, SET, C, EMM, word, set3, USER, jibu, xuenquruanjian, kaishicaidanxuanquruanjian, shibiejieguo
    while not button_b.is_pressed():
        w1 = get_seni_weather("https://api.seniverse.com/v3/weather/now.json?key=SMhSshUxuTL0GLVLS", "ip")
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        oled.DispChar(str(str(w1["results"][0]["location"]["name"]) + str(str(w1["results"][0]["now"]["text"]) + str(w1["results"][0]["now"]["temperature"]))), 15, 11, 1)
        oled.show()

def get_seni_weather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json
ntptime.settime(8, "time.windows.com")
list = 0
ver = '3.0'
xuanquruanjian2 = 0
WENBEN = 15
set2 = 0
SET = 'OFF'
C = False
EMM = False
word = 0
A = 0
H = 0
set3 = 0
M = 0
USER = 'LP'
jibu = 0
xuenquruanjian = 0
kaishicaidanxuanquruanjian = False
shibiejieguo = '空'
oled.fill(0)
oled.DispChar(str('              LP MADE'), 0, 0, 1)
oled.DispChar(str('              WELCOME'), 0, 16, 1)
oled.show()
time.sleep(3)
Deskop()