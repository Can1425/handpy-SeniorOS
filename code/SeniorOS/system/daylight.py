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

class App:
    @staticmethod
    def Style1(appTitle:str):
        gc.collect()
        oled.fill(0)
        UITools()
        PagesManager.Main.Import('SeniorOS.style.bar', ('Style' + Core.Data.Get("text", "barStyleNum")), True, appTitle)

    @staticmethod
    def Style2(appTitle:str):
        gc.collect()
        oled.fill(0)
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
                oled.DispChar(appTitle, 5, 5, 1)
                oled.DispChar(UITime(True), 93, 5, 1)
        oled.show()
        while not button_a.is_pressed():
            oled.fill_rect(0, 20, 128, 45, 0)
            oled.DispChar(dispContent[selectNum], AutoCenter(dispContent[selectNum]), y, 1)
            oled.DispChar(Core.ListState(dispContent, selectNum), 105, 40, 1)
            if window:
                oled.RoundRect(2, y - 26, 124, 55, 2, 1)
            oled.show()
            on_pressed = GetButtonExpr('on')
            py_pressed = GetButtonExpr('py')
            th_pressed = GetButtonExpr('th')
            if on_pressed:
                selectNum = min(selectNum + 1, len(dispContent) - 1)
            if py_pressed:
                selectNum = max(selectNum - 1, 0)
            if th_pressed:
                return selectNum
            time.sleep_ms(Const('interval'))
        return

    @staticmethod
    def Style2(dispContent:list, tip:list, y:int, window:bool=False, appTitle = None):
        oled.fill(0)
        UITools()
        selectNum = 0
        if appTitle:
            if not window:
                App.Style1(appTitle)
            else:
                Text(appTitle, 5, 5, 3, 90)
                oled.DispChar(UITime(True), 93, 5, 1)
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
            time.sleep_ms(Const('interval'))
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
            time.sleep_ms(Const('interval'))

def ListOptions(dispContent:list, y:int, window:False, appTitle:str):
    # 请不要在激活 appTitle 时设置 window = True
    UITools()
    listNum = 0
    oled.fill(0)
    if appTitle != "None":
        App.Style1(appTitle)
    oled.show()
    while not button_a.is_pressed():
        oled.fill_rect(0, 20, 128, 45, 0)
        oled.DispChar(Core.ListState(dispContent, listNum), 105, 40, 1)
        try:
            Text(str(dispContent[listNum]), 5, y, 3, showMode=2)
            Text(str(dispContent[listNum + 1]), 5, y + 15, 3)
            Text(str(dispContent[listNum + 2]), 5, y + 30, 3)
        except IndexError:
            try:
                Text(str(dispContent[listNum]), 5, y, 3, showMode=2)
                Text(str(dispContent[listNum + 1]), 5, y + 15, 3)
            except IndexError:
                Text(str(dispContent[listNum]), 5, y, 3, showMode=2)
        if window:
            oled.RoundRect(2, y - 6, 124, 55, 2, 1)
        oled.show()
        on_pressed = eval("[/GetButtonExpr('on')/]")
        py_pressed = eval("[/GetButtonExpr('py')/]")
        th_pressed = eval("[/GetButtonExpr('th')/]")
        if on_pressed:
            listNum = min(listNum + 1, len(dispContent) - 1)
        if py_pressed:
            listNum = max(listNum - 1, 0)
        if th_pressed:
            return listNum

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
    def Progressive(mode):
        if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
            luminance = int(Core.Data.Get("text", "luminance"))
            if mode:
                for _ in range(VastSea.speed):
                    luminance -= luminance // VastSea.speed
                    oled.contrast(luminance)
                oled.fill(0)
                UITools()
            else:
                for _ in range(VastSea.speed):
                    luminance += (255 - luminance) // VastSea.speed
                    oled.contrast(luminance)
                UITools()

    class SeniorMove:
        @staticmethod
        def Line(nowX1:int, nowY1:int, nowX2:int, nowY2:int, newX1:int, newY1:int, newX2:int, newY2:int):
            oled.fill(0)
            oled.line(nowX1, nowY1, nowX2, nowY2, 1)
            oled.show()
            if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
                for _ in range(VastSea.speed):
                    oled.fill(0)
                    nowX1 = nowX1 + ((newX1-nowX1) // VastSea.speed)
                    nowY1 = nowY1 - ((nowY1-newY1) // VastSea.speed + (newY1 - newY1//2))
                    nowX2 = nowX2 + ((newX2-nowX2) // VastSea.speed)
                    nowY2 = nowY2 - ((nowY2-newY2) // VastSea.speed + (newY2 - newY2//2))
                    oled.line(newX1, newY1, newX2, newY2, 1)
                    oled.show()
                    time.sleep_ms(10)
                oled.fill(0)
                oled.show()
            return

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