import SeniorOS.system.core as Core
import sys
import time
from SeniorOS.system.devlib import *
import SeniorOS.system.log_manager as LogManager
import SeniorOS.system.pages_manager as PagesManager
import SeniorOS.system.dynamic_run_page as DynamicRun
LogManager.Output("system/daylight.mpy", "INFO")
Manager = PagesManager('system/daylight.mpy')

def UITime(pages=True):
    h=str(Core.GetTime.Hour())
    m=str(Core.GetTime.Min())
    return ('0' + h if len(h)==1 else h) + \
             (':' if pages else "") + \
            ('0' + m if len(m)==1 else m)

def GetCharWidth(s):
    strWidth = oled.DispChar(s,0,0,Colormode.noshow)[0][0]
    #for c in s:
    #    charData = oled.f.GetCharacterData(c)
    #    if charData is None:continue
    #    strWidth += ustruct.unpack('HH', charData[:4])[0] + 1
    return strWidth

AutoCenter=lambda string:64-GetCharWidth(string)//2
HomeTimeAutoCenter=lambda string:64-GetCharWidth(string)

class App:
    def Style1(appTitle:str):
        oled.fill(0)
        UITools()
        DynamicRun.Main(Manager, 'SeniorOS.style.bar', 'Style' + Core.Data.Get("text", "barStyleNum"), 'Style' + Core.Data.Get("text", "barStyleNum"))
        del sys.modules['SeniorOS.style.bar']
    def Style2(appTitle:str):
        oled.fill(0)
        UITools()
        Text(appTitle, 5, 5, 3, 90)
        # oled.DispChar(appTitle, 5, 5, 1)

class Select:
    def Style1(dispContent:list, y:int, window:bool = False, appTitle = None):
        oled.fill(0)
        UITools()
        selectNum = 0
        if appTitle == None:
            pass
        else:
            if window == False:
                App.Style1(appTitle)
            else:
                oled.DispChar(appTitle, 5, 5, 1)
                oled.DispChar(UITime(True), 93, 5, 1)
        oled.show()
        while not button_a.is_pressed():
            oled.fill_rect(0, 20, 128, 45, 0)
            oled.DispChar(dispContent[selectNum], AutoCenter(dispContent[selectNum]), y, 1)
            oled.DispChar(Core.ListState(dispContent, selectNum), 105, 40, 1)
            if window == True:
                oled.RoundRect(2, y - 26, 124, 55, 2, 1)
            else:
                pass
            oled.show()
            if eval("[/GetButtonExpr('on')/]"):
                selectNum = selectNum + 1
                if selectNum + 1 > len(dispContent):
                    selectNum = len(dispContent) - 1
            if eval("[/GetButtonExpr('py')/]"):
                selectNum = selectNum - 1
                if selectNum < 0:
                    selectNum = 0
            if eval("[/GetButtonExpr('th')/]"):
                return selectNum
            time.sleep_ms(int(eval("[/Const('interval')/]")))
        return
    def Style2(dispContent:list, tip:list, y:int, window:bool=False, appTitle = None):
        oled.fill(0)
        UITools()
        selectNum = 0
        if appTitle == None:
            pass
        else:
            if window == False:
                App.Style1(appTitle)
            else:
                Text(appTitle, 5, 5, 3, 90)
                oled.DispChar(UITime(True), 93, 5, 1)
        oled.show()
        while not button_a.is_pressed():
            if window == True:
                oled.RoundRect(2, y - 18, 124, 55, 2, 1)
            else:
                pass
            oled.show()
            if eval("[/GetButtonExpr('on')/]"):
                selectNum = selectNum + 1
                if selectNum + 1 > len(dispContent):
                    selectNum = len(dispContent) - 1
            if eval("[/GetButtonExpr('py')/]"):
                selectNum = selectNum - 1
                if selectNum < 0:
                    selectNum = 0
            if eval("[/GetButtonExpr('th')/]"):
                return selectNum
            time.sleep_ms(int(eval("[/Const('interval')/]")))
            Text(dispContent[selectNum], 5, y, 2)
            # oled.DispChar(tip[selectNum], 5, y, 1, True)
            # oled.DispChar(dispContent[selectNum], 5, y + 27, 1)
            Text(dispContent[selectNum], 5, y + 27, 3)
            oled.DispChar(Core.ListState(dispContent, selectNum), 105, 45, 1)
            oled.show()
    def Style3():
        UITools()
        selectNum = 0
        while not button_a.is_pressed():
            if eval("[/GetButtonExpr('py')/]"):
                selectNum = 1
                return selectNum
            if eval("[/GetButtonExpr('on')/]"):
                selectNum = 0
                return selectNum
            time.sleep_ms(int(eval("[/Const('interval')/]")))

def ListOptions(dispContent:list, y:int, window:False, appTitle:str):
    # 请不要在激活 appTitle 时设置 window = True
    UITools()
    _list = 0
    listNum = 0
    oled.fill(0)
    if appTitle == "None":
        pass
    else:
        App.Style1(appTitle)
    oled.show()
    while not button_a.is_pressed():
        oled.fill_rect(0, 20, 128, 45, 0)
        oled.DispChar(Core.ListState(dispContent, listNum), 105, 40, 1)
        try:
            Text(str(dispContent[listNum]), 5, y, 3)
            # oled.DispChar(str(dispContent[listNum]), 5, y, 2)
            Text(str(dispContent[(listNum + 1)]), 5, y + 15, 3)
            # oled.DispChar(str(dispContent[(listNum + 1)]), 5, y + 15, 1)
            Text(str(dispContent[(listNum + 1)]), 5, y + 30, 3)
            # oled.DispChar(str(dispContent[(listNum + 2)]), 5, y + 30, 1)
        except:
            try:
                Text(str(dispContent[listNum]), 5, y, 3)
                # oled.DispChar(str(dispContent[listNum]), 5, y, 2)
                Text(str(dispContent[(listNum + 1)]), 5, y + 15, 3)
            except:
                Text(str(dispContent[listNum]), 5, y, 3)
                # oled.DispChar(str(dispContent[listNum]), 5, y, 2)
        if window == True:
            oled.RoundRect(2, y - 6, 124, 55, 2, 1)
        else:
            pass
        oled.show()
        if eval("[/GetButtonExpr('on')/]"):
            listNum = listNum + 1
            if listNum + 1 > len(dispContent):
                listNum = len(dispContent) - 1
        if eval("[/GetButtonExpr('py')/]"):
            listNum = listNum - 1
            if listNum < 0:
                listNum = 0
        if eval("[/GetButtonExpr('th')/]"):
            return listNum

class VastSea:
    speed = int(Core.Data.Get("text", "VastSeaSpeed"))
    def Switch():
        while not button_a.is_pressed():
            oled.fill(0)
            UITools()
            App.Style2(eval("[/Language('动效开关')/]"))
            time.sleep_ms(5)
            get = int(Core.Data.Get("text", "VastSeaSwitch"))
            oled.DispChar([eval("[/Language('关闭')/]"),eval("[/Language('开启')/]")](get), 5, 18, 1)
            oled.show()
            get = Select.Style3()
            Core.Data.Write("text",'VastSeaSwitch', str(get))
        return
    
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
                for _ in range(VastSea.speed):
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
        oled.DispChar('关于日光引擎', 5, 5, 1)
        oled.DispChar("这是一个 GUI 框架，", 5, 20, 1)
        oled.DispChar("负责渲染部分特有 GUI", 5,35 , 1)
        oled.DispChar("鸣谢POLA在的巨大贡献", 5, 50, 1)
        oled.show()
    return

def LightModeSet():
    while not button_a.is_pressed():
        oled.fill(0)
        UITools()
        App.Style2(eval("[/Language('日光模式')/]"))
        time.sleep_ms(5)
        get = int(Core.Data.Get("text", "luminance"))
        oled.DispChar([eval("[/Language('关闭')/]"),eval("[/Language('开启')/]")](get), 5, 18, 1)
        oled.show()
        get = Select.Style3()
        Core.Data.Write("text",'lightMode', str(get))

def LuminanceSet():
    luminance = int(Core.Data.Get("text", "luminance"))
    oled.contrast(luminance)
    UITools()
    while not button_a.is_pressed():
        oled.contrast(luminance)
        oled.fill(0)
        App.Style2(eval("[/Language('亮度调节')/]"))
        time.sleep_ms(5)
        oled.DispChar(eval("[/Language('当前值')/]") + str(luminance), 5, 18, 1)
        oled.show()
        if eval("[/GetButtonExpr('on')/]"):
            luminance = luminance + 5
            if luminance > 255:
                luminance = 255
            oled.contrast(luminance)
        if eval("[/GetButtonExpr('py')/]"):
            luminance = luminance - 5
            if luminance < 0:
                luminance = 0
            oled.contrast(luminance)
    oled.contrast(luminance)
    Core.Data.Write("text",'luminance',str(luminance))
    return

def Text(text, x, y, outMode, maximum_x = 118, return_x = 5, return_addy = 18):
    if outMode == 1:
        oled.DispChar(text, x, y, 1, Outmode.stop, maximum_x, return_x, return_addy)
        return
    if outMode == 2:
        oled.DispChar(text, x, y, 1, Outmode.autoreturn, maximum_x, return_x, return_addy)
        return
    if outMode == 3:
        oled.DispChar(text, x, y, 1, Outmode.ellipsis, maximum_x, return_x, return_addy)
        return