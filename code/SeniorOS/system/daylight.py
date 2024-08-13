import SeniorOS.system.core as Core
import gc
import time
from SeniorOS.system.devlib import *
import SeniorOS.system.log_manager as LogManager
import SeniorOS.system.pages_manager as PagesManager
LogManager.Output("system/daylight.mpy", "INFO")

# 缓存时间相关的字符串
def UITime(pages=True):
    h = str(Core.GetTime.Hour())
    m = str(Core.GetTime.Min())
    return ('0' + str(h) if len(str(h)) == 1 else str(h)) + \
             (':' if pages else "") + \
            ('0' + str(m) if len(str(m)) == 1 else str(m))

def GetCharWidth(s):
    # 获取字符宽度的优化实现
    return oled.DispChar(s, 0, 0, Colormode.noshow)[0][0]

AutoCenter = lambda string: 64 - GetCharWidth(string) // 2
HomeTimeAutoCenter = AutoCenter

def Box(x1, y1, x2, y2, fill = False, function = False):
    UITools()
    if fill:
        oled.fill_rect(x1 + 1, y1 + 1, x2 - 2, y2 - 2, 0)
    if function:
        function()
    oled.rect(x1, y1, x2, y2, 1)

class App:
    def Style1(appTitle:str, window = False):
        gc.collect()
        oled.fill(0)
        if window:
            Box(1, 1, 126, 62)
        UITools()
        Text(appTitle, 5, 0, 3, 1, 100)
        oled.DispChar(UITime(True), 93, 0, 1)

    def Style2(appTitle:str, window = False):
        gc.collect()
        oled.fill(0)
        if window:
            Box(1, 1, 126, 62)
        UITools()
        Text(appTitle, 5, 5, 3, 90)

class Select:
    @staticmethod
    def Style1(dispContent:list, y:int, window:bool = False, appTitle = None):
        oled.fill(0)
        UITools()
        selectNum = 0
        if appTitle:
            if not window:
                App.Style1(appTitle)
            else:
                App.Style1(appTitle, True)
        elif window:
            Box(1,1,126,62)
        oled.show()
        while not button_a.is_pressed():
            oled.fill_rect(0, 20, 128, 45, 0)
            oled.DispChar(dispContent[selectNum], AutoCenter(dispContent[selectNum]), y, 1)
            oled.DispChar(Core.ListState(dispContent, selectNum), 105, 40, 1)
            oled.show()
            on_pressed = eval("[/GetButtonExpr('on')/]")
            py_pressed = eval("[/GetButtonExpr('py')/]")
            th_pressed = eval("[/GetButtonExpr('th')/]")
            if on_pressed:
                selectNum = min(selectNum + 1, len(dispContent) - 1)
            if py_pressed:
                selectNum = max(selectNum - 1, 0)
            if th_pressed:
                return selectNum
            time.sleep_ms(int(eval("[/Const('interval')/]")))
        return

    @staticmethod
    def Style2(dispContent:list, tip:list, y:int, window:bool = False, appTitle = None):
        oled.fill(0)
        UITools()
        selectNum = 0
        if appTitle:
            if not window:
                App.Style1(appTitle)
            else:
                App.Style1(appTitle, True)
        elif window:
            Box(1,1,126,62)
        oled.show()
        while not button_a.is_pressed():
            if window:
                oled.RoundRect(2, y - 18, 124, 55, 2, 1)
            oled.show()
            on_pressed = eval("[/GetButtonExpr('on')/]")
            py_pressed = eval("[/GetButtonExpr('py')/]")
            th_pressed = eval("[/GetButtonExpr('th')/]")
            if on_pressed:
                selectNum = min(selectNum + 1, len(dispContent) - 1)
            if py_pressed:
                selectNum = max(selectNum - 1, 0)
            if th_pressed:
                return selectNum
            time.sleep_ms(int(eval("[/Const('interval')/]")))
            Text(dispContent[selectNum], 5, y, 2)
            Text(dispContent[selectNum], 5, y + 27, 3)
            oled.DispChar(Core.ListState(dispContent, selectNum), 105, 45, 1)
            oled.show()

    @staticmethod
    def Style3():
        UITools()
        selectNum = 0
        while not button_a.is_pressed():
            py_pressed = eval("[/GetButtonExpr('py')/]")
            on_pressed = eval("[/GetButtonExpr('on')/]")
            if py_pressed:
                selectNum = 1
                return selectNum
            if on_pressed:
                selectNum = 0
                return selectNum
            time.sleep_ms(int(eval("[/Const('interval')/]")))

    def Style4(dispContent:list, window:False, appTitle:str = "None"):
        lendispcontext = len(dispContent)
        maxdispcontextindex = lendispcontext - 1
        UITools()
        listNum = 0
        while not eval("[/GetButtonExpr('ath')/]"):
            oled.fill(0)
            if not appTitle == "None":
                App.Style1(appTitle,window)
            elif window:
                Box(1, 1, 126, 62)
            start = max(0, min(len(dispContent) - 3, listNum - 1))
            displayItems = dispContent[start:start + 3]
            for i, item in enumerate(displayItems):
                Text(item, 5, 16 * (i + 1), 2, showMode=1)
            if len(displayItems) > 0:
                oled.fill_rect(0, 16 + 16 * (listNum - start), 128, 16, 1)
                Text(displayItems[listNum - start], 5, 16 + 16 * (listNum - start), 2, showMode = 2)
            oled.show()
            while not button_a.is_pressed():
                if eval("[/GetButtonExpr('on')/]"):
                    if listNum < maxdispcontextindex:
                        listNum += 1
                        break
                elif eval("[/GetButtonExpr('py')/]"):
                    if listNum > 0:
                        listNum -= 1
                        break
                elif eval("[/GetButtonExpr('th')/]"):
                    return listNum

ListOptions = Select.Style4

class VastSea:
    speed = int(Core.Data.Get("text", "VastSeaSpeed"))

    @staticmethod
    def Switch():
        while not button_a.is_pressed():
            oled.fill(0)
            UITools()
            App.Style2(eval("[/Language('动效开关')/]"))
            time.sleep_ms(5)
            get = int(Core.Data.Get("text", "VastSeaSwitch"))
            oled.DispChar([eval("[/Language('关闭')/]"), eval("[/Language('开启')/]")][get], 5, 18, 1)
            oled.show()
            get = Select.Style3()
            Core.Data.Write("text", 'VastSeaSwitch', str(get))
        return
    
    @staticmethod
    def Off():
        oled.fill(0)
        oled.show()
        time.sleep_ms(VastSea.speed * 90)
        return

    @staticmethod
    def Transition():
        if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
            for i in range(13):
                times = i * i
                oled.vline(times, 0, 64, 1)
                oled.vline(times+1, 0, 64, 0)
                oled.fill_rect(0, 0, times, 64, 0)
                oled.show()
        else:
            VastSea.Off()

    class SeniorMove:
        @staticmethod
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
                    oled.show()
            else:
                VastSea.Off()
            oled.fill(0)
            time.sleep_ms(200)

        @staticmethod
        def Box(text):
            boxlong=17+(len(text)*8)
            xb=128-boxlong
            yb=48
            for _ in range(7):
                oled.fill_rect(0,0,xb,yb,0)
                oled.rect(0,0,xb,yb,1)
                oled.show()
                xb=(128-xb)//2+xb
                yb=(64-yb)//2+yb
            oled.fill_rect(0,0,128,64,0)
            oled.rect(0,0,128,64,1)
            oled.show()
        @staticmethod
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

def Text(text, x, y, outMode, space = 1, maximum_x = 122, returnX = 5, returnAddy = 16, showMode = 1):
    if outMode == 1:
        oled.DispChar(text, x, y, showMode, Outmode.stop, maximum_x, space, return_x = returnX, return_addy = returnAddy)
        return
    if outMode == 2:
        oled.DispChar(text, x, y, showMode, Outmode.autoreturn, maximum_x, space, return_x = returnX, return_addy = returnAddy)
        return
    if outMode == 3:
        oled.DispChar(text, x, y, showMode, Outmode.ellipsis, maximum_x, space, return_x = returnX, return_addy = returnAddy)
        return
