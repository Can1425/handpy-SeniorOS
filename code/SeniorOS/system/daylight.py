import SeniorOS.system.core as Core
import SeniorOS.apps.logo as Logo
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

def VastSeaOff():
    oled.fill(0)
    oled.show()
    time.sleep_ms(400)
    return

def Consani(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, consani_start_x, consani_start_y, consani_start_wide, consani_start_height):
    UITools()
    consani_done_wait = 3
    if int(Core.Data.Get('VastSea_switch')) == 1:
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

    
def ConsaniSideslip(side:True):
    if int(Core.Data.Get('VastSea_switch')) == 1:
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

def Select(dispContent:list, y:int, window:False, appTitle:str):
    UITools()
    selectNum = 0

    if appTitle == "None":
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
    OffConsin()

class VastSea:
    speed = 3 #3,6,12
    class AppsPage:
        def Open(nowX1, nowX2, nowX3, nowX4, nowY1, nowY2, nowY3, nowY4, appNum:int):
            if int(Core.Data.Get('VastSea_switch')) == 1:
                appList = Core.Data.Get("app").split(',')
                # nowX1 = 30
                # nowX2 = 85
                # nowX3 = AutoCenter(appList[appNum])
                # nowX4 = 46
                # nowY1 = 25
                # nowY2 = 25
                # nowY3 = 48
                # nowY4 = 10
                oled.DispChar(str('〔'), nowX1, nowY1, 1)
                oled.DispChar(str('〕'), nowX2, nowY2, 1)
                oled.DispChar(appList[appNum], nowX3, nowY3, 1)
                oled.show()
                for count in range(VastSea.speed):
                    nowX1 = nowX1 - (6 * (12/VastSea.speed))
                    nowX2 = nowX2 + (6 * (12/VastSea.speed))
                    nowX3 = nowX3 - (nowX3 // (VastSea.speed / 2))
                    print(nowX3)
                    nowY1 = nowY1 - (3 * (12/VastSea.speed))
                    nowY2 = nowY2 - (3 * (12/VastSea.speed))
                    nowY3 = nowY3 - (4 * (12/VastSea.speed))
                    # nowY4 = nowY4 + (6 * (12/VastSea.speed))
                    oled.fill(0)
                    oled.DispChar(appList[appNum], int(nowX3), int(nowY3), 1)
                    oled.DispChar('〔', int(nowX1), int(nowY1), 1)
                    oled.DispChar('〕', int(nowX2), int(nowY2), 1)
                    oled.show()
                oled.fill(0)
            else:
                VastSeaOff()
        def Close(nowX1, nowX2, nowX3, nowX4, nowY1, nowY2, nowY3, nowY4, appNum:int):
            if int(Core.Data.Get('VastSea_switch')) == 1:
                appList = Core.Data.Get("app").split(',')
                # nowX1 = -40
                # nowX2 = 157
                # nowX3 = 1
                # nowX4 = None
                # nowY1 = -11
                # nowY2 = -11
                # nowY3 = 0
                # nowY4 = None
                oled.DispChar(str('〔'), nowX1, nowY1, 1)
                oled.DispChar(str('〕'), nowX2, nowY2, 1)
                oled.DispChar(appList[appNum], nowX3, nowY3, 1)
                oled.show()
                for count in range(VastSea.speed):
                    nowX1 = nowX1 + (6 * (12/VastSea.speed))
                    nowX2 = nowX2 - (6 * (12/VastSea.speed))
                    nowX3 = nowX3 + (nowX3 * (VastSea.speed / 2))
                    nowY1 = nowY1 + (3 * (12/VastSea.speed))
                    nowY2 = nowY2 + (3 * (12/VastSea.speed))
                    nowY3 = nowY3 + (4 * (12/VastSea.speed))
                    # nowY4 = nowY4 - (6 * (12/VastSea.speed))
                    oled.fill(0)
                    oled.DispChar(appList[appNum], int(nowX3), int(nowY3), 1)
                    oled.DispChar('〔', int(nowX1), int(nowY1), 1)
                    oled.DispChar('〕', int(nowX2), int(nowY2), 1)
                    oled.show()
                oled.fill(0)
            else:
                VastSeaOff()
    class SeniorMove:
        def Line(nowX:int, nowY:int, nowLength:int, newX:int, newY:int, newLength:int):
            oled.hline(nowX, nowY, nowLength, 1)
            oled.show()
            for count in range(VastSea.speed):
                nowX = nowX + ((newX-nowX) // VastSea.speed)
                nowY = nowY - ((nowY-newY) // VastSea.speed + (newY - newY//2))
                nowLength = nowLength + ((newLength - nowLength) // VastSea.speed)
                oled.fill(0)
                oled.hline(nowX, nowY, nowLength, 1)
                oled.DispChar(str(nowX), 0, 32, 1)
                oled.DispChar(str(nowY), 0, 48, 1)
                oled.show()

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