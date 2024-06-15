import SeniorOS.system.core as Core
import ntptime
import network
import time
import ustruct
import framebuf
from mpython import wifi,oled
from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from mpython import button_a,button_b
import gc
import uos
import math
import urequests

def UITime(pages=True):
    h=str(Core.GetTime.Hour())
    m=str(Core.GetTime.Min())
    return ('0' + h if len(h)==1 else h) + \
             (':' if pages else "") + \
            ('0' + m if len(m)==1 else m)

def OffConsin():
    oled.fill(0)
    oled.show()
    time.sleep_ms(600)
    return

def consani(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, consani_start_x, consani_start_y, consani_start_wide, consani_start_height):
    UITools()
    consani_done_wait = 3
    if int(Core.Data.Get('dynamicEffect')) == 1:
        try:
            oled.fill(0)
            for _ in range(7):
                oled.RoundRect(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, 2, 1)
                oled.fill(0)
                consani_done_x = (consani_done_x - consani_start_x) // 2
                consani_done_y = (consani_done_y - consani_start_y) // 2
                consani_done_wide = (consani_start_wide + consani_done_wide) // 2
                consani_done_height = (consani_start_height + consani_done_height) // 2
                oled.RoundRect(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, 2, 1)
                oled.show()
        except:
            oled.DispChar(' :( 我们遇到了一些问题，将在 3 秒后返回', 5, 25, 1, True)
            oled.show()
            return
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            return
        time.sleep_ms(consani_done_wait)
        consani_done_wait = consani_done_wait + 3
    else:
        OffConsin()

def ConsaniAppOpen(xn, yn, w, wn, h, hn, rn, logo, logo_x):
    UITools()
    if int(Core.Data.Get('dynamicEffect')) == 1:
        try:
            r = 0
            x1 = xn
            y1 = yn
            w1 = wn
            h1 = hn
            r1 = rn
            t = 1
            oled.RoundRect(x1, y1, w1, h1, r1, 1)
            oled.show()
            for count in range(2):
                oled.fill(0)
                oled.RoundRect(x1, y1, w1, h1, r1, 1)
                oled.Bitmap(logo_x, 20, logo, 25, 25, 1)
                oled.show()
                x1 = x1 - t * t
                y1 = y1 - t * t
                w1 = w1 + 2 * (t * t)
                h1 = h1 + 2 * (t * t)
                r1 = r + t * t
                t = t + 1
            for count in range(7):
                x = x1
                y = y1
                w = w1
                h = h1
                r = r1
                oled.fill(0)
                oled.RoundRect(x1, y1, w1, h1, r1, 1)
                oled.Bitmap(logo_x, 20, logo, 25, 25, 1)
                oled.show()
                x1 = (x1 - 0) // 2
                y1 = (y1 - 0) // 2
                w1 = (128 + w1) // 2
                h1 = (64 + h1) // 2
                r1 = (r - 0) // 2
                logo_x = (logo_x + 52) //2
                time.sleep_ms(15)
        except:
            oled.DispChar(' :( 我们遇到了一些问题，将在 3 秒后返回', 5, 25, 1, True)
            oled.show()
            return
    else:
        OffConsin()

def ConsaniAppClose(xn, yn, w, wn, h, hn, rn, logo, logo_x):
    UITools
    if int(Core.Data.Get('dynamicEffect')) == 1:
        try:
            r = 0
            x = 0
            y = 0
            w = 128
            h = 64
            r = rn
            t = 1
            x1 = 0
            y1 = 0
            w1 = 128
            h1 = 64
            for count in range(7):
                oled.fill(0)
                oled.RoundRect(x1, y1, w, h, r, 1)
                oled.Bitmap(logo_x, 20, logo, 25, 25, 1)
                oled.show()
                x1 = (x1 - 0) // 2
                y1 = (y1 - 0) // 2
                w1 = (128 + w1) // 2
                h1 = (64 + h1) // 2
                r1 = (r - 0) // 2
                x = x1
                y = y1
                w = w1
                h = h1
                r = r1
                time.sleep_ms(15)
            for count in range(7):
                oled.fill(0)
                oled.RoundRect(x, y, w, h, r, 1)
                oled.show()
                x = (xn + x) // 2
                y = (yn + y) // 2
                w = (wn + w) // 2
                h = (hn + h) // 2
                r = (rn + r) // 2
                logo_x = logo_x * 2
                time.sleep_ms(15)
        except:
            oled.DispChar(' :( 我们遇到了一些问题，将在 3 秒后返回', 5, 25, 1, True)
            oled.show()
            return
    else:
        OffConsin()
    
def ConsaniSideslip(side:True):
    if int(Core.Data.Get('dynamicEffect')) == 1:
        t = 10
        if side:
            x = 128
            for count in range(3):
                oled.fill(0)
                oled.RoundRect(x, (-1), 130, 66, 2, 1)
                oled.show()
                x = int((x - 3 * math.sqrt(t)))
                time.sleep_ms(t)
            for count in range(7):
                oled.fill(0)
                oled.RoundRect(x, (-1), 130, 66, 2, 1)
                oled.show()
                x = x // 2
                t = t + 3
                time.sleep_ms(t)
        else:
            x = 0
            for count in range(3):
                oled.fill(0)
                oled.RoundRect(x, (-1), 130, 66, 2, 1)
                oled.show()
                x = int((x + 3 * math.sqrt(t)))
                t = t + -3
                time.sleep_ms(t)
            for count in range(7):
                oled.fill(0)
                oled.RoundRect(x, (-1), 130, 66, 2, 1)
                oled.show()
                x = x + (128 - x) // 2
                time.sleep_ms(t)
    else:
        OffConsin()

def GetCharWidth(s):
    strWidth = 0
    for c in s:
        charData = oled.f.GetCharacterData(c)
        if charData is None:continue
        strWidth += ustruct.unpack('HH', charData[:4])[0] + 1
    return strWidth
AutoCenter=lambda string:64-GetCharWidth(string)//2
HomeTimeAutoCenter=lambda string:64-GetCharWidth(string)//2-22

def app(appTitle:str):
    oled.fill(0)
    UITools()
    try:
        oled.invert(int(Core.Data.Get('light')))
    except:
        pass
    oled.DispChar(appTitle, 5, 0, 1)
    oled.DispChar(UITime(True), 93, 0, 1)

def DisplayFont(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

def Select(dispContent:list,appTitle:str):
    selectNum = 0
    while not button_a.is_pressed():
        oled.rect(2, 4, 124, 16, 1)
        oled.DispChar(appTitle, 5, 5, 1)
        oled.DispChar(UITime(True), 93, 5, 1)
        oled.DispChar(dispContent[selectNum], AutoCenter(dispContent[selectNum]), 20, 1)
        oled.DispChar(''.join([str(selectNum + 1),'/',str(len(dispContent))]), 105, 40, 1)
        oled.DispChar('TH-确认', 5, 40, 1)
        oled.show()
        if touchPad_O.is_pressed() and touchPad_N.is_pressed():
            selectNum = selectNum + 1
            if selectNum + 1 > len(dispContent):
                selectNum = len(dispContent) - 1
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            selectNum = selectNum - 1
            if selectNum < 0:
                selectNum = 0
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            return selectNum
    time.sleep_ms(10)
    return

def ListOptions(dispContent:list):
    UITools()
    _list = 0
    listNum = 0
    oled.fill(0)
    oled.fill_rect(1, 0, 126, 16, 1)
    oled.show()
    while not button_a.is_pressed():
        oled.fill(0)
        oled.RoundRect(2, 2, 124, 55, 2, 1)
        oled.DispChar(''.join([str(listNum + 1),'/',str(len(dispContent))]), 105, 40, 1)
        try:
            oled.DispChar(str(dispContent[listNum]), 5, 8, 2)
            oled.DispChar(str(dispContent[(listNum + 1)]), 5, 23, 1)
            oled.DispChar(str(dispContent[(listNum + 2)]), 5, 38, 1)
        except:
            try:
                oled.DispChar(str(dispContent[listNum]), 5, 8, 2)
                oled.DispChar(str(dispContent[(listNum + 1)]), 5, 23, 1)
            except:
                oled.DispChar(str(dispContent[listNum]), 5, 8, 2)
        oled.show()
        if touchPad_O.is_pressed() and touchPad_N.is_pressed():
            listNum = listNum + 1
            if listNum + 1 > len(dispContent):
                listNum = listNum
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            listNum = listNum - 1
            if listNum < listNum:
                listNum = 0
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            return listNum


def message(content:str):
    content = content + "   按A键确认   "
    while not button_a.is_pressed:
        oled.fill(0)
        oled.fill_rect(1, 0, 126, 16, 1)
        oled.DispChar(content, 0, 0, 2)
        oled.show()
        time.sleep(0.2)
        content = content[1:] + content[0]
    OffConsin()

def UITools():
    try:
        oled.invert(int(Core.Data.Get('light')))
        oled.contrast(int(Core.Data.Get('luminance')))
    except:
        pass

def About():
    while not button_a.is_pressed():
        oled.fill(0)
        UITools()
        oled.DispChar(str('关于日光引擎'), 5, 5, 1)
        oled.DispChar("这是一个 GUI 框架，", 5, 20, 1)
        oled.DispChar("负责渲染部分特有 GUI", 5,35 , 1)
        oled.DispChar("鸣谢POLA在的巨大贡献", 5, 50, 1)
        oled.show()
    return