import SeniorOS.system.core as Core
import SeniorOS.style.bar as BarStyle
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

def GetCharWidth(s):
    strWidth = 0
    for c in s:
        charData = oled.f.GetCharacterData(c)
        if charData is None:continue
        strWidth += ustruct.unpack('HH', charData[:4])[0] + 1
    return strWidth

AutoCenter=lambda string:64-GetCharWidth(string)//2
HomeTimeAutoCenter=lambda string:64-GetCharWidth(string)

BarPage = {  
    1: BarStyle.Style1,  
    2: BarStyle.Style2,  
    3: BarStyle.Style3,
    4: BarStyle.Style4,
}

def app(appTitle:str):
    oled.fill(0)
    UITools()
    BarPage.get(int(Core.Data.Get("text", "barStyleNum")))(appTitle)

def DisplayFont(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

class Select:
    def Style1(dispContent:list, y:int, window:bool = False, appTitle = None):
        oled.fill(0)
        UITools()
        selectNum = 0
        if appTitle == None:
            pass
        else:
            if window == False:
                app(appTitle)
            else:
                oled.DispChar(appTitle, 5, 5, 1)
                oled.DispChar(UITime(True), 93, 5, 1)
        oled.show()
        while not button_a.is_pressed():
            oled.fill_rect(0, 20, 128, 45, 0)
            oled.DispChar(dispContent[selectNum], AutoCenter(dispContent[selectNum]), y, 1)
            oled.DispChar(''.join([str(selectNum + 1),'/',str(len(dispContent))]), 105, 40, 1)
            if window == True:
                oled.RoundRect(2, y - 26, 124, 55, 2, 1)
            else:
                pass
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
            time.sleep_ms(300)
        time.sleep_ms(300)
        return
    def Style2(dispContent:list, tip:list, y:int, window:bool=False, appTitle = None):
        oled.fill(0)
        UITools()
        selectNum = 0
        if appTitle == None:
            pass
        else:
            if window == False:
                app(appTitle)
            else:
                oled.DispChar(appTitle, 5, 5, 1)
                oled.DispChar(UITime(True), 93, 5, 1)
        oled.show()
        while not button_a.is_pressed():
            if window == True:
                oled.RoundRect(2, y - 18, 124, 55, 2, 1)
            else:
                pass
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
            oled.DispChar(tip[selectNum], 5, y, 1, True)
            oled.DispChar(dispContent[selectNum], 5, y + 27, 1)
            oled.DispChar(''.join([str(selectNum + 1),'/',str(len(dispContent))]), 105, 45, 1)
            oled.show()

def ListOptions(dispContent:list, y:int, window:False, appTitle:str):
    # 请不要在激活 appTitle 时设置 window = True
    UITools()
    _list = 0
    listNum = 0
    oled.fill(0)
    if appTitle == "None":
        pass
    else:
        app(appTitle)
    oled.show()
    while not button_a.is_pressed():
        oled.fill_rect(0, 20, 128, 45, 0)
        oled.DispChar(''.join([str(listNum + 1),'/',str(len(dispContent))]), 105, 40, 1)
        try:
            oled.DispChar(str(dispContent[listNum]), 5, y, 2)
            oled.DispChar(str(dispContent[(listNum + 1)]), 5, y + 15, 1)
            oled.DispChar(str(dispContent[(listNum + 2)]), 5, y + 30, 1)
        except:
            try:
                oled.DispChar(str(dispContent[listNum]), 5, y, 2)
                oled.DispChar(str(dispContent[(listNum + 1)]), 5, y + 15, 1)
            except:
                oled.DispChar(str(dispContent[listNum]), 5, y, 2)
        if window == True:
            oled.RoundRect(2, y - 6, 124, 55, 2, 1)
        else:
            pass
        oled.show()
        if touchPad_O.is_pressed() and touchPad_N.is_pressed():
            listNum = listNum + 1
            if listNum + 1 > len(dispContent):
                listNum = len(dispContent) - 1
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            listNum = listNum - 1
            if listNum < 0:
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

class VastSea:
    speed = int(Core.Data.Get("text", "VastSeaSpeed"))
    def Off():
        oled.fill(0)
        oled.show()
        time.sleep_ms(VastSea.speed * 90)
        return
    def Progressive(mode):
        if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
            if mode == True:
                luminance = int(Core.Data.Get("text", "luminance"))
                for count in range(VastSea.speed):
                    luminance = luminance - luminance // VastSea.speed
                    oled.contrast(luminance)
                oled.fill(0)
                UITools()
            if mode == False:
                luminance = int(Core.Data.Get("text", "luminance"))
                for count in range(VastSea.speed):
                    luminance = 0 + luminance // VastSea.speed
                    oled.contrast(luminance)
                UITools()
    class SeniorMove:
        def Line(nowX1:int, nowY1:int, nowX2:int, nowY2:int, newX1:int, newY1:int, newX2:int, newY2:int):
            oled.fill(0)
            oled.line(nowX1, nowY1, nowX2, nowY2, 1)
            oled.show()
            if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
                for count in range(VastSea.speed):
                    oled.line(nowX1, nowY1, nowX2, nowY2, 0)
                    nowX1 = nowX1 + ((newX1-nowX1) // VastSea.speed)
                    nowY1 = nowY1 - ((nowY1-newY1) // VastSea.speed + (newY1 - newY1//2))
                    nowX2 = nowX2 + ((newX2-nowX2) // VastSea.speed)
                    nowY2 = nowY2 - ((nowY2-newY2) // VastSea.speed + (newY2 - newY2//2))
                    oled.line(nowX1, nowY1, nowX2, nowY2, 1)
                    # oled.DispChar(str(nowX1), 0, 32, 1)
                    # oled.DispChar(str(nowY1), 0, 48, 1)
                    # oled.DispChar(str(nowX2), 50, 32, 1)
                    # oled.DispChar(str(nowY2), 50, 48, 1)
                    oled.show()
            else:
                VastSea.Off()
            oled.fill(0)
            time.sleep_ms(200)

        def Text(text, nowX:int, nowY:int, newX:int, newY:int):
            if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
                oled.fill(0)
                oled.DispChar(str(text), nowX, nowY)
                oled.show()
                for count in range(VastSea.speed):
                    oled.fill_rect(0, nowY, 128, 16, 0)
                    nowX = nowX + ((newX-nowX) // VastSea.speed)
                    nowY = nowY - ((nowY-newY) // VastSea.speed + (newY - newY//2))
                    oled.DispChar(str(text), nowX, nowY)
                    # oled.DispChar(str(nowX), 0, 32, 1)
                    # oled.DispChar(str(nowY), 0, 48, 1)
                    oled.show()
            else:
                VastSea.Off()
            oled.fill(0)
            time.sleep_ms(300)

def UITools():
    try:
        oled.invert(int(Core.Data.Get("text", "lightMode")))
        oled.contrast(int(Core.Data.Get("text", "luminance")))
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