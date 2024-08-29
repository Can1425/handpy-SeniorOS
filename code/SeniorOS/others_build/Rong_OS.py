x1 = None

y1 = None

x2 = None

y2 = None

from mpython import *

x = None

y = None

xz = None

import network

my_wifi = wifi()

try_connect_wifi(my_wifi, "WiFiName", "WiFiPassword", 5)

import ntptime

import json

import urequests

import time

import framebuf

import font.dvsmb_21

i = None

j = None

c = None

def tc():
    global xz, lt, x1, x, c, ngls, c1, c2, c3, xx, y1, y, xx1, x2, dx, a, y2, letter, szfh, letter_big, n_s, yy, my_list, i, j, my_1, ks, js1, js2, sf, sfl
    oled.fill(0)
    c = 0
    for count in range(32):
        oled.fill(0)
        oled.rect(0, 0, (c * 2), c, 1)
        c = c + 2
        oled.show()

import _thread

import usocket

def udp_recv(_udp_msg):
    global sfl, sf, js2, js1, ks, my_1, j, i, my_list, yy, n_s, letter_big, szfh, letter, y2, a, dx, x2, xx1, y, y1, xx, c3, c2, c1, ngls, c, x, x1, lt, xz
    print(_udp_msg)

def thread_udp():
    while True:
        try:
            _msg = socket_udp.recv(1024)
            if _msg: udp_recv(_msg.decode("UTF-8", "ignore"))
        except: pass

_thread.start_new_thread(thread_udp, ())

xx1 = None

dx = None

szfh = None

import music

yy = None

xx = None

my_1 = None

def _E5_BC_80_E5_A7_8B():
    global xz, lt, x1, x, c, ngls, c1, c2, c3, xx, y1, y, xx1, x2, dx, a, y2, letter, szfh, letter_big, n_s, yy, my_list, i, j, my_1, ks, js1, js2, sf, sfl
    while True:
        if touchpad_t.is_pressed():
            break
        xx1 = letter[c1]
        dx = letter_big[c2]
        szfh = n_s[c3]
        if c == 0:
            rgb[2] = (0, 0, 0)
            rgb.write()
            time.sleep_ms(1)
            oled.fill(0)
            oled.DispChar(str(xx1), 0, 0, 2)
            oled.DispChar(str('小写模式'), 9, 0, 1)
            oled.DispChar(str(dx), 60, 0, 1)
            oled.DispChar(str(szfh), 120, 0, 1)
            _E6_98_BE_E7_A4_BA()
        elif c == 1:
            rgb[2] = (int(50), int(0), int(0))
            rgb.write()
            time.sleep_ms(1)
            oled.fill(0)
            oled.DispChar(str(xx1), 0, 0, 1)
            oled.DispChar(str('大写模式'), 69, 0, 1)
            oled.DispChar(str(dx), 60, 0, 2)
            oled.DispChar(str(szfh), 120, 0, 1)
            _E6_98_BE_E7_A4_BA()
        else:
            rgb[2] = (int(50), int(50), int(0))
            rgb.write()
            time.sleep_ms(1)
            oled.fill(0)
            oled.DispChar(str(xx1), 0, 0, 1)
            oled.DispChar(str('数字符号'), 69, 0, 1)
            oled.DispChar(str(dx), 60, 0, 1)
            oled.DispChar(str(szfh), 120, 0, 2)
            _E6_98_BE_E7_A4_BA()
        _E6_95_B0()
        if touchpad_p.is_pressed():
            time.sleep_ms(25)
            if c == 0:
                c1 = c1 + 1
            elif c == 1:
                c2 = c2 + 1
            else:
                c3 = c3 + 1
        if touchpad_y.is_pressed():
            if yy == True:
                music.pitch(554, 75)
            c = c + 1
            time.sleep_ms(500)
        if touchpad_t.is_pressed():
            rgb[0] = (int(0), int(0), int(50))
            rgb.write()
            time.sleep_ms(1)
            time.sleep_ms(400)
            rgb[0] = (0, 0, 0)
            rgb.write()
            time.sleep_ms(1)
            a.append(' ')
        if touchpad_h.is_pressed():
            while not button_a.is_pressed():
                if button_b.is_pressed():
                    if yy == True:
                        music.pitch(659, 100)
                        yy = False
                        time.sleep(0.5)
                    else:
                        music.pitch(932, 100)
                        yy = True
                        time.sleep(0.5)
                _E7_89_88_E6_9C_AC_E4_BF_A1_E6_81_AF()
        if touchpad_o.is_pressed():
            a.clear()
            _E7_A9_BA()
        if touchpad_n.is_pressed():
            time.sleep_ms(25)
            if c == 0:
                c1 = c1 + -1
            elif c == 1:
                c2 = c2 + -1
            else:
                c3 = c3 + -1
        if button_a.is_pressed():
            if yy == True:
                music.pitch(988, 75)
            if len(a) > 53:
                if yy == True:
                    music.pitch(277, 75)
                while True:
                    oled.fill(0)
                    oled.DispChar(str('显示区域已满！'), 20, 24, 1)
                    oled.show()
                    time.sleep_ms(500)
                    if button_a.is_pressed():
                        a.clear()
                        _E5_BC_80_E5_A7_8B()
                    if button_b.is_pressed():
                        _E5_BC_80_E5_A7_8B()
            if c == 0:
                a.append(xx1)
                xx = str(xx) + str(xx1)
            elif c == 1:
                a.append(dx)
                xx = str(xx) + str(dx)
            else:
                a.append(szfh)
                xx = str(xx) + str(szfh)
        if button_b.is_pressed():
            _E7_A9_BA()
            if yy == True:
                music.pitch(415, 50)
            a.pop()
            xx = ''
            my_1 = 0
            for count in range(int(len(a))):
                xx = str(xx) + str(a[my_1])
                my_1 = my_1 + 1
        if c == 3:
            c = 0

import random

import machine

def _E7_89_88_E6_9C_AC_E4_BF_A1_E6_81_AF():
    global xz, lt, x1, x, c, ngls, c1, c2, c3, xx, y1, y, xx1, x2, dx, a, y2, letter, szfh, letter_big, n_s, yy, my_list, i, j, my_1, ks, js1, js2, sf, sfl
    oled.fill(0)
    oled.Bitmap(0, 0, bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X0C,0X00, 0X00,0X00,0X00,0X40,0X00,0X00,0X43,0X00,0X00,0X00,0X00,0X00,0X08,0X00,0X1C,0X00, 0X06,0X72,0X00,0XE0,0X70,0X03,0XFF,0XF0,0X00,0XE0,0X00,0XC0,0X18,0X00,0X3C,0X00, 0X07,0X77,0X00,0XE0,0X70,0X07,0XFF,0XF0,0X00,0XE0,0X01,0XC3,0XFF,0X00,0XFF,0X80, 0X3F,0XFF,0XC0,0XE7,0XFF,0X87,0XFF,0XF0,0X07,0XFF,0XC1,0XC7,0XFF,0X01,0XFF,0X80, 0X3F,0XFF,0XC0,0XFF,0XFF,0XC0,0XE7,0X00,0X3F,0XFF,0XC1,0XFF,0XBF,0X80,0XFF,0X80, 0X1F,0XFF,0XC3,0XFF,0XFF,0X80,0X7A,0X00,0X3F,0XFF,0X01,0XFB,0XFF,0XC0,0X7D,0X80, 0X07,0XFF,0X03,0XE7,0X79,0X80,0XFF,0XC0,0X0C,0X06,0X03,0X83,0XFF,0X80,0X7F,0XE0, 0X07,0XFE,0X02,0XE6,0XFD,0X03,0XFF,0XC0,0X0E,0X0E,0X03,0XFF,0XBF,0X03,0XFF,0XF0, 0X03,0XFE,0X00,0XF9,0XCE,0X03,0XFF,0XE0,0X06,0X0C,0X03,0XFF,0XFF,0X03,0XFF,0XE0, 0X07,0XFF,0X00,0XF9,0XC6,0X03,0X98,0XC0,0X07,0X1C,0X00,0XF7,0XBE,0X00,0X7D,0X80, 0X0F,0XFE,0X00,0XF8,0XFE,0X03,0X98,0XC0,0X03,0XB8,0X00,0XF9,0XBE,0X00,0XEF,0XC0, 0X0F,0XFF,0X83,0XE0,0XFE,0X0F,0XFF,0XF8,0X01,0XF0,0X03,0XF3,0X9C,0X00,0XE3,0X80, 0X0F,0XFF,0X83,0XE0,0X7C,0X1F,0XFF,0XF8,0X01,0XF0,0X03,0XE7,0XBF,0X80,0XC3,0X80, 0X0F,0XFF,0XC0,0XE0,0X38,0X0F,0XFF,0X00,0X01,0XF8,0X00,0X7B,0X7F,0X01,0XFF,0XE0, 0X1F,0XFF,0XC0,0XE0,0X38,0X00,0X73,0X80,0X07,0XFF,0XC0,0XFB,0X9C,0X03,0XFF,0XE0, 0X1F,0XFF,0XC3,0XE0,0X3F,0X00,0XE3,0XC0,0X1F,0X1F,0XE0,0XF7,0XCC,0X03,0XFF,0XE0, 0X01,0XE0,0X03,0XE3,0XFF,0X83,0XE1,0XF8,0X3C,0X03,0XC0,0XE6,0XFF,0X03,0XB6,0X60, 0X01,0XE0,0X01,0XE3,0XFF,0X87,0XC0,0XFC,0X38,0X00,0X00,0XE4,0X3F,0X0F,0XFF,0XF8, 0X00,0X00,0X00,0X40,0X00,0X03,0X00,0X3C,0X00,0X00,0X00,0X40,0X00,0X0F,0XFF,0XFC, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X07,0XFF,0XF8, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X02,0X00,0X08,0X00,0X04,0X18,0X0C,0X00,0X00,0X00, 0X00,0X00,0X03,0XC1,0XC1,0X04,0X0A,0X1E,0X0C,0X00,0X3D,0XF8,0X08,0X20,0X00,0X00, 0X00,0X00,0X07,0XC3,0XF1,0X8C,0X0A,0X60,0X0D,0XFC,0X61,0X01,0XFF,0XF0,0X00,0X00, 0X00,0X00,0X0C,0X06,0X19,0X8C,0X0A,0X40,0X3E,0X88,0X61,0X00,0X10,0X00,0X00,0X00, 0X00,0X00,0X0C,0X0C,0X08,0XD8,0X0F,0XFE,0X0C,0X88,0X7D,0X08,0X3F,0X80,0X00,0X00, 0X00,0X00,0X0E,0X0C,0X0C,0XD8,0X08,0X62,0X0C,0X98,0X65,0XF8,0X20,0X80,0X00,0X00, 0X00,0X00,0X07,0X8C,0X0C,0X70,0X08,0X66,0X1E,0X50,0X65,0X30,0X60,0X80,0X00,0X00, 0X00,0X00,0X01,0XCC,0X0C,0X70,0X0F,0X54,0X1F,0X50,0X7D,0X30,0XBF,0X80,0X00,0X00, 0X00,0X00,0X00,0X6C,0X0C,0X60,0X0B,0XDC,0X3C,0X70,0X65,0X31,0X20,0X80,0X00,0X00, 0X00,0X00,0X00,0X6C,0X18,0X60,0X1B,0XD8,0X2C,0X60,0X63,0X30,0X3F,0X80,0X00,0X00, 0X00,0X00,0X08,0X66,0X38,0X60,0X1B,0X9C,0X0C,0X70,0X42,0X30,0X20,0X80,0X00,0X00, 0X00,0X00,0X0F,0XC3,0XF0,0X60,0X13,0XB6,0X0D,0X9C,0X46,0X30,0X20,0X80,0X00,0X00, 0X00,0X00,0X03,0X00,0XE0,0X00,0X11,0X43,0X0F,0X0E,0X84,0X30,0X23,0X80,0X00,0X00, 0X00,0X00,0X00,0X00,0X3C,0X00,0X00,0X00,0X08,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X1C,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X18,0X01,0XF8,0X10,0X43,0X10,0X32,0XC1,0X88,0X01,0X00,0X64,0X03,0X00, 0X00,0X00,0X18,0X06,0X98,0XF7,0XC7,0X98,0X37,0XF1,0X08,0X01,0X00,0X44,0X03,0X08, 0X00,0X00,0X34,0X02,0X50,0X60,0X04,0XBE,0X7A,0X43,0XDF,0X01,0X01,0XFF,0X9F,0XFC, 0X00,0X00,0X6A,0X0F,0XFC,0X60,0X27,0X80,0X37,0XE2,0X53,0X0D,0X42,0X26,0X82,0X00, 0X1F,0XF8,0XD9,0XD9,0X08,0XF7,0XC5,0XBC,0X37,0XE2,0X63,0X09,0X20,0X66,0X03,0XF0, 0X00,0X01,0X18,0X87,0XF8,0X67,0X87,0XAC,0X7E,0X63,0XDB,0X19,0X30,0X4C,0X07,0X30, 0X00,0X00,0X18,0X01,0X10,0X65,0X84,0XAC,0X77,0XE2,0X4B,0X11,0X19,0X80,0X05,0X20, 0X00,0X00,0X18,0X03,0XF0,0X75,0X85,0XAC,0X3F,0XF2,0X43,0X21,0X18,0XFF,0X04,0XE0, 0X00,0X00,0X18,0X02,0XA0,0XCD,0XA4,0XAC,0X31,0X82,0X43,0X01,0X00,0XAB,0X08,0XC0, 0X00,0X00,0X18,0X04,0X60,0X09,0XA4,0XEE,0X32,0X43,0XC7,0X07,0X00,0XAB,0X19,0XF0, 0X00,0X00,0X18,0X0B,0X9C,0X30,0XE9,0XC7,0X34,0X32,0X46,0X03,0X01,0XFF,0X97,0X1C, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,]), 128, 64, 1)
    oled.show()

c1 = None

c2 = None

c3 = None

def _E6_95_B0():
    global xz, lt, x1, x, c, ngls, c1, c2, c3, xx, y1, y, xx1, x2, dx, a, y2, letter, szfh, letter_big, n_s, yy, my_list, i, j, my_1, ks, js1, js2, sf, sfl
    if c1 + 1 > len(letter) - 1:
        c1 = 0
    elif c2 + 1 > len(letter_big) - 1:
        c2 = 0
    elif c3 + 1 > len(n_s) - 1:
        c3 = 0
    elif c1 < 0:
        c1 = 25
    elif c2 < 0:
        c2 = 25
    elif c3 < 0:
        c3 = 25

def _E6_98_BE_E7_A4_BA():
    global xz, lt, x1, x, c, ngls, c1, c2, c3, xx, y1, y, xx1, x2, dx, a, y2, letter, szfh, letter_big, n_s, yy, my_list, i, j, my_1, ks, js1, js2, sf, sfl
    oled.line(0, 15, 128, 15, 1)
    oled.DispChar(str(xx), 0, 16, 1, True)
    oled.show()

def _E7_A9_BA():
    global xz, lt, x1, x, c, ngls, c1, c2, c3, xx, y1, y, xx1, x2, dx, a, y2, letter, szfh, letter_big, n_s, yy, my_list, i, j, my_1, ks, js1, js2, sf, sfl
    time.sleep(0.25)
    if not len(a):
        if yy == True:
            music.pitch(233, 75)
        oled.fill(0)
        oled.DispChar(str('没有可删除的了！'), 20, 24, 1)
        oled.show()
        _E5_BC_80_E5_A7_8B()

def init_text_file(_path):
    f = open(_path, 'w')
    f.close()

def write_data_to_file(_path, _data, _sep):
    f = open(_path, 'a')
    f.write(_data + _sep)
    f.close()

def get_list_from_file(_path, _sep):
    f = open(_path, 'r')
    result = f.read().split(_sep)
    f.close()
    return result

lt = None

def lt():
    global xz, lt, x1, x, c, ngls, c1, c2, c3, xx, y1, y, xx1, x2, dx, a, y2, letter, szfh, letter_big, n_s, yy, my_list, i, j, my_1, ks, js1, js2, sf, sfl
    _response = urequests.get('http://ycrrongos/rongDownload.GitHub.io/ZKBChatsystem/lt.txt', headers=xx, params={"item":'data'})
    init_text_file('1.txt')
    write_data_to_file('1.txt', xx, '\r\n')
    oled.fill(0)
    oled.DispChar(str((str(get_list_from_file('1.txt', '\r\n')[-0]))), 0, 0, 1, True)
    oled.show()
    lt = ''
    yy = False
    c = 0
    xx = ''
    my_list = []
    a = []
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'z']
    letter_big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Z']
    n_s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?', '!', '.', ',', '_', '-', "'", '@', '&', '←', '→', '#', "'", ':', '"', '/', '/']
    _E7_89_88_E6_9C_AC_E4_BF_A1_E6_81_AF()
    time.sleep(1)
    _E5_BC_80_E5_A7_8B()
    _response = urequests.post('http://ycrrongos/rongDownload.GitHub.io/ZKBChatsystem/lt.txt', files={"file":('1.txt', 'txt/txt')}, params={"item":'data'})
    write_data_to_file('1.txt', xx, '\r\n')

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

socket_udp = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
socket_udp.bind(("0.0.0.0", 100))

ngls = None

ks = None

def START():
    global xz, lt, x1, x, c, ngls, c1, c2, c3, xx, y1, y, xx1, x2, dx, a, y2, letter, szfh, letter_big, n_s, yy, my_list, i, j, my_1, ks, js1, js2, sf, sfl
    tc()
    while not (xz or button_b.is_pressed()):
        oled.fill(0)
        if y < 16:
            oled.DispChar(str('发消息'), 0, 0, 2)
        else:
            oled.DispChar(str('发消息'), 0, 0, 1)
        if y > 16 and y < 32:
            oled.DispChar(str('色子'), 0, 16, 2)
        else:
            oled.DispChar(str('色子'), 0, 16, 1)
        if y > 32 and y < 48:
            oled.DispChar(str('天气'), 0, 32, 2)
        else:
            oled.DispChar(str('天气'), 0, 32, 1)
        if y > 48:
            oled.DispChar(str('更多'), 0, 48, 2)
        else:
            oled.DispChar(str('更多'), 0, 48, 1)
        oled.pixel(x, y, 1)
        if accelerometer.get_x() < -0.3:
            y = y + -2
        elif accelerometer.get_x() > 0.3:
            y = y + 2
        elif accelerometer.get_y() > 0.3:
            x = x + -2
        elif accelerometer.get_y() < -0.3:
            x = x + 2
        if button_a.is_pressed() and y < 16:
            lt()
            time.sleep(1)
        oled.show()
        if button_a.is_pressed() and y > 16 and y < 32:
            oled.fill(0)
            oled.show()
            while not button_b.is_pressed():
                if _is_shaked:
                    oled.fill(0)
                    oled.DispChar(str((str(random.randint(1, 6)))), 0, 0, 1)
                    oled.show()
            time.sleep(1)
        if button_a.is_pressed() and y > 32 and y < 48:
            oled.fill(0)
            oled.show()
            while not button_b.is_pressed():
                oled.fill(0)
                oled.DispChar(str(w1["results"][0]["location"]["name"]), 0, 0, 1)
                oled.DispChar(str(w1["results"][0]["now"]["text"]), 0, 16, 1)
                oled.DispChar(str((str(w1["results"][0]["now"]["temperature"]) + '°')), 0, 32, 1)
                oled.DispChar(str(('紫外线' + str(w1["results"][0]["suggestion"]["uv"]["brief"]))), 0, 48, 1)
                oled.show()
        if button_a.is_pressed() and y > 48 and y < 64:
            oled.fill(0)
            oled.show()
            tc()
            while not (xz or button_b.is_pressed()):
                oled.fill(0)
                if y < 16:
                    oled.DispChar(str('环境信息'), 0, 0, 2)
                else:
                    oled.DispChar(str('环境信息'), 0, 0, 1)
                if y > 16 and y < 32:
                    oled.DispChar(str('WiFi'), 0, 16, 2)
                else:
                    oled.DispChar(str('WiFi'), 0, 16, 1)
                if y > 32 and y < 48:
                    oled.DispChar(str('系统信息'), 0, 32, 2)
                else:
                    oled.DispChar(str('系统信息'), 0, 32, 1)
                if y > 48:
                    oled.DispChar(str('更多'), 0, 48, 2)
                else:
                    oled.DispChar(str('更多'), 0, 48, 1)
                oled.pixel(x, y, 1)
                if accelerometer.get_x() < -0.3:
                    y = y + -2
                elif accelerometer.get_x() > 0.3:
                    y = y + 2
                elif accelerometer.get_y() > 0.3:
                    x = x + -2
                elif accelerometer.get_y() < -0.3:
                    x = x + 2
                if button_a.is_pressed() and y < 16:
                    if touchpad_h.is_pressed():
                        magnetic.calibrate()
                    while not button_b.is_pressed():
                        oled.fill(0)
                        oled.DispChar(str((str(magnetic.get_heading()))), 0, 0, 1)
                        oled.DispChar(str((str(magnetic.get_field_strength()))), 0, 16, 1)
                        oled.DispChar(str((str(sound.read()))), 0, 32, 1)
                        oled.DispChar(str((str(light.read()))), 0, 48, 1)
                        oled.show()
                    time.sleep_ms(500)
                oled.show()
                if button_a.is_pressed() and y > 16 and y < 32:
                    oled.fill(0)
                    oled.show()
                    my_wifi.enable_APWiFi('rongos', 'rongos', channel=11)
                    while not button_b.is_pressed():
                        oled.fill(0)
                        oled.DispChar(str((str(my_wifi.sta.ifconfig()))), 0, 0, 1, True)
                        oled.show()
                        if touchpad_p.is_pressed():
                            try: socket_udp.sendto(bytes('p', "utf-8"), ("255.255.255.255", 100))
                            except: pass
                        if touchpad_y.is_pressed():
                            try: socket_udp.sendto(bytes('y', "utf-8"), ("255.255.255.255", 100))
                            except: pass
                        if touchpad_t.is_pressed():
                            try: socket_udp.sendto(bytes('t', "utf-8"), ("255.255.255.255", 100))
                            except: pass
                        if touchpad_h.is_pressed():
                            try: socket_udp.sendto(bytes('h', "utf-8"), ("255.255.255.255", 100))
                            except: pass
                        if touchpad_o.is_pressed():
                            try: socket_udp.sendto(bytes('o', "utf-8"), ("255.255.255.255", 100))
                            except: pass
                        if touchpad_n.is_pressed():
                            try: socket_udp.sendto(bytes('n', "utf-8"), ("255.255.255.255", 100))
                            except: pass
                    my_wifi.disable_APWiFi()
                    time.sleep_ms(500)
                if button_a.is_pressed() and y > 32 and y < 48:
                    oled.fill(0)
                    oled.show()
                    while not button_b.is_pressed():
                        oled.fill(0)
                        myUI.qr_code('https://ycrrongos.github.io/', 0, 0, scale=1)
                        oled.DispChar(str((str(time.time()))), 0, 48, 1, True)
                        oled.show()
                if y > 48 and button_a.is_pressed():
                    tc()
                    while not (xz or button_b.is_pressed()):
                        oled.fill(0)
                        oled.DispChar(str('计算器'), 0, 0, 1)
                        oled.DispChar(str('卸载'), 0, 16, 1)
                        oled.pixel(x, y, 1)
                        oled.show()
                        if accelerometer.get_x() < -0.3:
                            y = y + -2
                        elif accelerometer.get_x() > 0.3:
                            y = y + 2
                        elif accelerometer.get_y() > 0.3:
                            x = x + -2
                        elif accelerometer.get_y() < -0.3:
                            x = x + 2
                        if button_a.is_pressed() and y < 16:
                            oled.fill(0)
                            oled.DispChar(str('此功能有bug，暂时停止使用'), 0, 0, 1, True)
                            oled.show()
                            time.sleep(1)
                        if button_b.is_pressed() and button_a.is_pressed() and y > 16 and y < 32:
                            init_text_file('main.py')
                            oled.fill(0)
                            _thread.start_new_thread(thread_1, ())
                        if button_a.is_pressed() and y > 32 and y < 48:
                            ngls = 0
                            ks = time.time()
                            _thread.start_new_thread(thread_2, ())
                            _thread.start_new_thread(thread_3, ())
                            _thread.start_new_thread(thread_4, ())
                            tc()
                            while not ngls == 3:
                                pass
                            while not button_b.is_pressed():
                                oled.fill(0)
                                oled.DispChar(str((str(time.time() - ks))), 0, 0, 1)
                                oled.show()
            time.sleep_ms(500)

def get_seni_weather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json

my_clock = Clock(oled, 64, 32, 32)

def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

random.seed(time.ticks_cpu())

def thread_1():
    global sfl, sf, js2, js1, ks, my_1, j, i, my_list, yy, n_s, letter_big, szfh, letter, y2, a, dx, x2, xx1, y, y1, xx, c3, c2, c1, ngls, c, x, x1, lt, xz
    xz = 1
    time.sleep(2)
    for count in range(1000):
        oled.pixel((random.randint(0, 128)), (random.randint(0, 64)), 1)
        oled.show()
    machine.reset()
    _thread.start_new_thread(thread_1, ())

myUI = UI(oled)

def thread_3():
    global sfl, sf, js2, js1, ks, my_1, j, i, my_list, yy, n_s, letter_big, szfh, letter, y2, a, dx, x2, xx1, y, y1, xx, c3, c2, c1, ngls, c, x, x1, lt, xz
    for count in range(100):
        myUI.qr_code('https://www.mpython.cn', (random.randint(0, 128)), (random.randint(0, 64)), scale=2)
        time.sleep(1)
        oled.show()
    ngls = ngls + 1

def thread_4():
    global sfl, sf, js2, js1, ks, my_1, j, i, my_list, yy, n_s, letter_big, szfh, letter, y2, a, dx, x2, xx1, y, y1, xx, c3, c2, c1, ngls, c, x, x1, lt, xz
    for count in range(100):
        oled.DispChar(str((str(random.randint(1, 1000000)) + str(time.ticks_us()))), (random.randint(0, 128)), (random.randint(0, 64)), 1)
        oled.show()
        oled.pixel((random.randint(0, 128)), (random.randint(0, 64)), 1)
        oled.show()
    ngls = ngls + 1

def thread_2():
    global sfl, sf, js2, js1, ks, my_1, j, i, my_list, yy, n_s, letter_big, szfh, letter, y2, a, dx, x2, xx1, y, y1, xx, c3, c2, c1, ngls, c, x, x1, lt, xz
    for count in range(100):
        oled.DispChar(str('测试'), (random.randint(0, 128)), (random.randint(0, 64)), 1)
        oled.show()
        oled.pixel((random.randint(0, 128)), (random.randint(0, 64)), 1)
        oled.show()
    ngls = ngls + 1

my_wifi = wifi()
for count in range(1):
    x1 = 39
    y1 = 2
    x2 = 73
    y2 = 46
    for count in range(10):
        x1 = x1 + 1
        y1 = y1 + 1
        x2 = x2 + -1
        y2 = y2 + -1
        oled.fill(0)
        oled.line(x1, y1, x2, y2, 1)
        oled.show()
    x1 = 43
    y1 = 3
    x2 = 91
    y2 = 64
    for count in range(10):
        x1 = x1 + 1
        y1 = y1 + 1
        x2 = x2 + -1
        y2 = y2 + -1
        oled.fill(0)
        oled.line(49, 12, 63, 36, 1)
        oled.line(x1, y2, x2, y1, 1)
        oled.show()
    x1 = 41
    y1 = 2
    x2 = 75
    y2 = 46
    for count in range(10):
        x1 = x1 + 1
        y1 = y1 + 1
        x2 = x2 + -1
        y2 = y2 + -1
        oled.fill(0)
        oled.line(49, 12, 63, 36, 1)
        oled.line(81, 13, 53, 54, 1)
        oled.line(x1, y1, x2, y2, 1)
        oled.show()
    x1 = 45
    y1 = 3
    x2 = 93
    y2 = 64
    for count in range(10):
        x1 = x1 + 1
        y1 = y1 + 1
        x2 = x2 + -1
        y2 = y2 + -1
        oled.fill(0)
        oled.line(49, 12, 63, 36, 1)
        oled.line(81, 13, 53, 54, 1)
        oled.line(51, 13, 65, 36, 1)
        oled.line(x1, y2, x2, y1, 1)
        oled.show()
x = 0
y = 0
xz = 0
ntptime.settime(8, "ntp.aliyun.com")
w1 = get_seni_weather("https://api.seniverse.com/v3/weather/now.json?key=SMhSshUxuTL0GLVLS", "ip")
while True:
    oled.fill(0)
    oled.pixel(x, y, 1)
    if accelerometer.get_x() < -0.3:
        y = y + -1
    elif accelerometer.get_x() > 0.3:
        y = y + 1
    elif accelerometer.get_y() > 0.3:
        x = x + -1
    elif accelerometer.get_y() < -0.3:
        x = x + 1
    if time.localtime()[3] < 10:
        display_font(font.dvsmb_21, ('0' + str(time.localtime()[3])), 33, 23, False)
    else:
        display_font(font.dvsmb_21, (str(time.localtime()[3])), 33, 23, False)
    display_font(font.dvsmb_21, (str(time.localtime()[4])), 75, 23, False)
    oled.show()
    i = 30
    j = 30
    for count in range(10):
        oled.fill_circle(64, j, 2, 1)
        oled.show()
        oled.fill_circle(64, i, 2, 1)
        oled.show()
        j = j + 1
        i = i + -1
    for count in range(10):
        oled.fill_circle(64, j, 2, 0)
        oled.show()
        oled.fill_circle(64, i, 2, 0)
        oled.show()
        j = j + -1
        i = i + 1
    if button_a.is_pressed():
        START()