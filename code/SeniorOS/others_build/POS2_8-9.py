#mPythonType:0
version = None

patch = None

bobo_monster = None

from mpython import *

import network

my_wifi = wifi()

my_wifi.connectWiFi("WiFiName", "WiFiPassword")

deskmode = None

back_button = None

load_text = None

deskapp = None

deskapp_1 = None

deskapp_2 = None

deskapp_3 = None

deskapp_4 = None

x = None

y = None

w = None

t = None

r = None

s = None

import time

import random

import json

import urequests

import ntptime

time_minute = None

time_hour = None

random.seed(time.ticks_cpu())

def get_seni_weather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json
version = '2'
patch = '8.9（2022/11/2）'
bobo_monster = '0X00,0X07,0XFC,0X00,0X00,0X00,0X18,0X03,0X00,0X00,0X00,0X60,0X00,0XC0,0X00,0X01, 0X80,0X00,0X30,0X00,0X07,0X80,0X00,0X3C,0X00,0X06,0X00,0X00,0X0C,0X00,0X0C,0X00, 0X00,0X06,0X00,0X10,0X00,0X00,0X03,0X00,0X10,0X00,0X00,0X03,0X00,0X20,0X00,0X00, 0X00,0X80,0X20,0X00,0X00,0X00,0X80,0X40,0X00,0X00,0X00,0X40,0X40,0X78,0X03,0XC0, 0X40,0X80,0X8C,0X02,0X60,0X20,0X80,0X87,0XFC,0X30,0X20,0X80,0X8C,0X07,0X10,0X20, 0X80,0XBC,0X07,0XB0,0X20,0X80,0XB0,0X01,0XB0,0X20,0X80,0X60,0X00,0X60,0X20,0X80, 0XC0,0X00,0X20,0X20,0X81,0X80,0X00,0X1C,0X20,0X81,0X06,0X1C,0X0E,0X20,0X46,0X06, 0X18,0X06,0X40,0X46,0X00,0X00,0X03,0X40,0X2E,0X00,0X00,0X03,0X80,0X2C,0X00,0XF0, 0X00,0X80,0X1C,0X01,0XF0,0X03,0X00,0X1C,0X00,0XF0,0X03,0X00,0X0C,0X00,0X60,0X06, 0X00,0X0E,0X00,0X60,0X0E,0X00,0X06,0X00,0X60,0X0C,0X00,0X01,0X80,0X70,0X30,0X00, 0X00,0X60,0X10,0XC0,0X00,0X00,0X18,0X73,0X00,0X00,0X00,0X07,0XFC,0X00,0X00,'
oled.Bitmap(7, 17, bytearray(bobo_monster), 35, 35, 1)
oled.DispChar(str(str('POLA OS ') + str(version)), 50, 18, 1)
oled.DispChar(str(patch), 50, 34, 1)
oled.show()
deskmode = 1
back_button = '<P'
load_text = '正在载入……'
deskapp = 1
deskapp_1 = '天气'
deskapp_2 = '更多'
deskapp_3 = '关于'
deskapp_4 = '聊天'
x = 47
y = 12
w = 36
t = 36
r = 7
s = 1
time.sleep_ms((random.randint(1000, 3000)))
while True:
    if deskapp == 1:
        if deskmode < 5:
            if button_a.is_pressed():
                deskmode = deskmode + -1
            elif button_b.is_pressed():
                deskmode = deskmode + 1
        else:
            deskmode = 4
        # “生活”APP
        if deskmode == 1:
            oled.fill(0)
            oled.RoundRect(x, y, w, t, r, 1)
            oled.DispChar(str(deskapp_1), 53, 50, 1)
            oled.RoundRect(90, 20, 35, 35, 7, 1)
            oled.DispChar(str(deskapp_2), 92, 6, 1)
            oled.show()
            if touchpad_t.is_pressed() or touchpad_h.is_pressed():
                oled.fill_rect(x, y, w, t, 0)
                x = x + 1
                y = y + 1
                w = w + -2
                t = t + -2
                oled.RoundRect(x, y, w, t, r, 1)
                oled.show()
                for count in range(9):
                    oled.fill_rect(x, y, w, t, 0)
                    x = x + -7
                    y = y + -2
                    w = w + 14
                    t = t + 4
                    r = r + -1
                    oled.RoundRect(x, y, w, t, r, 1)
                    oled.show()
                    time.sleep_ms(s)
                    s = s + 1
                oled.fill(0)
                oled.DispChar(str(load_text), 33, 20, 1, True)
                oled.show()
                x = 47
                y = 12
                w = 36
                t = 36
                r = 7
                s = 1
                W1 = get_seni_weather("https://api.seniverse.com/v3/weather/now.json?key=SboqGMxP4tYNXUN8f", "ip")
                W2 = get_seni_weather("https://api.seniverse.com/v3/weather/daily.json?key=SboqGMxP4tYNXUN8f", "ip")
                while True:
                    ntptime.settime(8, "ntp.aliyun.com")
                    if len(str(time.localtime()[4])) != 2:
                        time_minute = str('0') + str((str(time.localtime()[4])))
                    else:
                        time_minute = str(time.localtime()[4])
                    if len(str(time.localtime()[3])) != 2:
                        time_hour = str('0') + str((str(time.localtime()[3])))
                    else:
                        time_hour = str(time.localtime()[3])
                    oled.fill(0)
                    oled.DispChar(str(str('定位：') + str(W1["results"][0]["location"]["name"])), 2, 2, 1, True)
                    oled.DispChar(str(str(str(str(W1["results"][0]["now"]["text"]) + str('，')) + str(str(str(W2["results"][0]["daily"][0]["low"]) + str('~')) + str(W2["results"][0]["daily"][0]["high"]))) + str('℃')), 2, 20, 1, True)
                    oled.DispChar(str(str(str('现在') + str(W1["results"][0]["now"]["temperature"])) + str('℃')), 2, 38, 1, True)
                    oled.DispChar(str(back_button), 2, 50, 1, True)
                    oled.DispChar(str(str(str(time_hour) + str(':')) + str(time_minute)), 97, 50, 1, True)
                    oled.show()
                    if touchpad_p.is_pressed():
                        break
        # 第三方开发者应用
        if deskmode == 2:
            oled.fill(0)
            oled.RoundRect(0, 20, 35, 35, 7, 1)
            oled.DispChar(str(deskapp_1), 8, 6, 1)
            oled.RoundRect(x, y, w, t, r, 1)
            oled.DispChar(str(deskapp_2), 53, 50, 1)
            oled.RoundRect(90, 20, 35, 35, 7, 1)
            oled.DispChar(str(deskapp_3), 92, 6, 1)
            oled.show()
            if touchpad_t.is_pressed() or touchpad_h.is_pressed():
                oled.fill_rect(x, y, w, t, 0)
                x = x + 1
                y = y + 1
                w = w + -2
                t = t + -2
                oled.RoundRect(x, y, w, t, r, 1)
                oled.show()
                for count in range(9):
                    oled.fill_rect(x, y, w, t, 0)
                    x = x + -7
                    y = y + -2
                    w = w + 14
                    t = t + 4
                    r = r + -1
                    oled.RoundRect(x, y, w, t, r, 1)
                    oled.show()
                    time.sleep_ms(s)
                    s = s + 1
                oled.fill(0)
                oled.DispChar(str(load_text), 33, 20, 1, True)
                oled.show()
                x = 47
                y = 12
                w = 36
                t = 36
                r = 7
                s = 1
                while True:
                    ntptime.settime(8, "ntp.aliyun.com")
                    if len(str(time.localtime()[4])) != 2:
                        time_minute = str('0') + str((str(time.localtime()[4])))
                    else:
                        time_minute = str(time.localtime()[4])
                    if len(str(time.localtime()[3])) != 2:
                        time_hour = str('0') + str((str(time.localtime()[3])))
                    else:
                        time_hour = str(time.localtime()[3])
                    oled.fill(0)
                    oled.DispChar(str('聊天 by LP'), 2, 2, 1, True)
                    oled.DispChar(str(back_button), 2, 50, 1, True)
                    oled.DispChar(str(str(str(time_hour) + str(':')) + str(time_minute)), 97, 50, 1, True)
                    oled.show()
                    if touchpad_p.is_pressed():
                        break
        # 关于本机
        if deskmode == 3:
            oled.fill(0)
            oled.RoundRect(0, 20, 35, 35, 7, 1)
            oled.DispChar(str(deskapp_2), 8, 6, 1)
            oled.RoundRect(x, y, w, t, r, 1)
            oled.DispChar(str(deskapp_3), 53, 50, 1)
            oled.RoundRect(90, 20, 35, 35, 7, 1)
            oled.DispChar(str(deskapp_4), 92, 6, 1)
            oled.show()
            if touchpad_t.is_pressed() or touchpad_h.is_pressed():
                oled.fill_rect(x, y, w, t, 0)
                x = x + 1
                y = y + 1
                w = w + -2
                t = t + -2
                oled.RoundRect(x, y, w, t, r, 1)
                oled.show()
                for count in range(9):
                    oled.fill_rect(x, y, w, t, 0)
                    x = x + -7
                    y = y + -2
                    w = w + 14
                    t = t + 4
                    r = r + -1
                    oled.RoundRect(x, y, w, t, r, 1)
                    oled.show()
                    time.sleep_ms(s)
                    s = s + 1
                oled.fill(0)
                oled.DispChar(str(load_text), 33, 20, 1, True)
                oled.show()
                x = 47
                y = 12
                w = 36
                t = 36
                r = 7
                s = 1
                while True:
                    ntptime.settime(8, "ntp.aliyun.com")
                    if len(str(time.localtime()[4])) != 2:
                        time_minute = str('0') + str((str(time.localtime()[4])))
                    else:
                        time_minute = str(time.localtime()[4])
                    if len(str(time.localtime()[3])) != 2:
                        time_hour = str('0') + str((str(time.localtime()[3])))
                    else:
                        time_hour = str(time.localtime()[3])
                    oled.fill(0)
                    oled.Bitmap(7, 17, bytearray(bobo_monster), 35, 35, 1)
                    oled.DispChar(str(str('POLA OS ') + str(version)), 50, 18, 1)
                    oled.DispChar(str(patch), 50, 34, 1)
                    oled.DispChar(str(str(str(time_hour) + str(':')) + str(time_minute)), 97, 50, 1, True)
                    oled.DispChar(str(back_button), 2, 50, 1, True)
                    oled.show()
                    if touchpad_p.is_pressed():
                        break
        # 聊天
        if deskmode == 4:
            oled.fill(0)
            oled.RoundRect(0, 20, 35, 35, 7, 1)
            oled.DispChar(str(deskapp_3), 8, 6, 1)
            oled.RoundRect(x, y, w, t, r, 1)
            oled.DispChar(str(deskapp_4), 53, 50, 1)
            oled.show()
            if touchpad_t.is_pressed() or touchpad_h.is_pressed():
                oled.fill_rect(x, y, w, t, 0)
                x = x + 1
                y = y + 1
                w = w + -2
                t = t + -2
                oled.RoundRect(x, y, w, t, r, 1)
                oled.show()
                for count in range(9):
                    oled.fill_rect(x, y, w, t, 0)
                    x = x + -7
                    y = y + -2
                    w = w + 14
                    t = t + 4
                    r = r + -1
                    oled.RoundRect(x, y, w, t, r, 1)
                    oled.show()
                    time.sleep_ms(s)
                    s = s + 1
                oled.fill(0)
                oled.DispChar(str(load_text), 33, 20, 1)
                oled.show()
                x = 47
                y = 12
                w = 36
                t = 36
                r = 7
                s = 1
                while True:
                    ntptime.settime(8, "ntp.aliyun.com")
                    if len(str(time.localtime()[4])) != 2:
                        time_minute = str('0') + str((str(time.localtime()[4])))
                    else:
                        time_minute = str(time.localtime()[4])
                    if len(str(time.localtime()[3])) != 2:
                        time_hour = str('0') + str((str(time.localtime()[3])))
                    else:
                        time_hour = str(time.localtime()[3])
                    oled.fill(0)
                    oled.DispChar(str('开发者：LP'), 2, 2, 1, True)
                    oled.DispChar(str('开发者需要更新APP 使其继续可用。'), 2, 20, 1, True)
                    oled.DispChar(str(back_button), 2, 50, 1, True)
                    oled.DispChar(str(str(str(time_hour) + str(':')) + str(time_minute)), 97, 50, 1, True)
                    oled.show()
                    if touchpad_p.is_pressed():
                        break
