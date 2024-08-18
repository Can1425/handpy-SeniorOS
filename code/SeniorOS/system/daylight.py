import SeniorOS.system.core as Core
import math
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

    @staticmethod        
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
    def SpeedSet():
        presuppose = {
            0:"100",
            1:"200",
            2:"300",
        }
        while not button_a.is_pressed():
            options = Select.Style4(["高效", "优雅", "柔和"], False, "动画速率")
            if options != None:
                VastSea.Transition()
                Box(54,126,74,126,True)
                oled.DispChar(eval("[/Language('加载成功')/]"), AutoCenter(eval("[/Language('加载成功')/]")), 55)
                Core.Data.Write("text", "VastSeaSpeed", presuppose[options])
                VastSea.Transition(False)

        else:
            VastSea.Transition(False)
    @staticmethod   
    def Off():
        oled.fill(0)
        oled.show()
        time.sleep_ms(int(eval("[/Const('interval')/]")))
        return
    @staticmethod   
    def Transition(mode:bool = True):
        if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
            if mode:
                for i in range(13):
                    times = i * i
                    oled.vline(times, 0, 64, 1)
                    oled.vline(times+1, 0, 64, 0)
                    oled.fill_rect(0, 0, times, 64, 0)
                    oled.show()
            else:
                for i in range(13):
                    times = 13 - i
                    times_squared = times * times
                    oled.fill_rect(0, 0, 128, 64, 0)
                    oled.vline(times_squared, 0, 64, 1)
                    oled.vline(times_squared + 1, 0, 64, 0)
                    oled.show()
                oled.fill_rect(0, 0, 128, 64, 0)
                oled.show()
        else:
            VastSea.Off()

    class SeniorMove:
        @staticmethod
        def Text(text, startX, startY, endX, endY):
            speed = int(Core.Data.Get("text", "VastSeaSpeed"))
            if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
                elapsedTime = 0  # 已过去的时间
                timer = 10  # 定时器间隔（毫秒）
                while elapsedTime < speed:
                    elapsedTime += timer
                    t = elapsedTime / speed
                    factor = -(math.cos(math.pi * t) - 1) / 2
                    currentX= startX + (endX - startX) * factor
                    currentY = startY + (endY - startY) * factor
                    # 根据计算出的 current_x 和 current_y 更新位置
                    oled.fill(0)
                    oled.DispChar(text, int(currentX), int(currentY))
                    oled.show()
            else:
                VastSea.Off()

        # 你希望实现与现在相反的效果？不是，从理论上说，我写的这个是可以做到的，但是在 某种情况（确实是某种情况，那只是个代表）下出现了那种问题，我暂时还没搞清楚为什么会这样
        # 什么意思(emo)问一下你是希望再写个函数还是基于原来的函数，我认为这是一个bug，所以基于原函数修改(emo)懂了，你的意思是说，调用Line(sx,sy,ex,ey,sl,el)的Line(ex,ey,sx,sy,el,sl)的动画效果不是相反的？这是一个典例，我想要表达的并不是这个意思，而是我发现，当这些值满足一定条件时，动画效果是不受控制的(emo)懂了，从数学角度上，sin和cos呈现周期性，所以会有这种情况（除非你能保证sin和cos的输入值都在±π）so，我们该做些什么(emo)先检查sin和cos的输入范围。对了，那个“当这些值满足一定条件时，动画效果是不受控制的”能细说一下条件吗？事实证明，我似乎还没探索出什么规律 (emo)检查发现sin和cos的输入范围确实在±π，所以得先检查一下atan2 诶我发现了，如果endY-startY≠0但是endX-startX=0的情况下，math.atan2(endY - startY, endX - startX)的输出貌似会出现一些截断情况（例如从-π突然跳到π） 啊，因为math.atan2(y,x)的函数原型是math.atan(y/x)，可能是这样，我在测试中的确输入了一些 0 嗯嗯所以看来如果要改的话只能改动画函数了 你可以试试吗？ 这不能帮你（因为我这里没有完整的SeniorOS编译环境）这一段没有使用 SROS API 可直接运行 哦哦不过对于这些大问题我懒得帮（ 6
        @staticmethod
        def Line(startX, startY, startX2,startY2, endX, endY, endX2, endY2):
            speed = int(Core.Data.Get("text", "VastSeaSpeed"))
            if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
                elapsedTime = 0  # 已过去的时间
                timer = 10  # 定时器间隔（毫秒）
                while elapsedTime < speed:
                    elapsedTime += timer
                    t = elapsedTime / speed
                    factor = -(math.cos(math.pi * t) - 1) / 2
                    currentX = startX + (endX - startX) * factor
                    currentY = startY + (endY - startY) * factor
                    currentX2 = startX2 + (endX2 - startX2) * factor
                    currentY2 = startY2 + (endY2 - startY2) * factor
                    # 根据计算出的 currentX、currentY、currentX2 和 currentY2 更新线条的位置
                    oled.fill(0)
                    oled.line(int(currentX), int(currentY), int(currentX2), int(currentY2), 1)
                    oled.show()
            else:
                VastSea.Off()
        @staticmethod
        def Bitmap(bitMap, startX, startY, endX, endY, h, w):
            speed = int(Core.Data.Get("text", "VastSeaSpeed"))
            if int(Core.Data.Get("text", "VastSeaSwitch")) == 1:
                elapsedTime = 0  # 已过去的时间
                timer = 10  # 定时器间隔（毫秒）
                while elapsedTime < speed:
                    elapsedTime += timer
                    t = elapsedTime / speed
                    factor = -(math.cos(math.pi * t) - 1) / 2
                    currentX= startX + (endX - startX) * factor
                    currentY = startY + (endY - startY) * factor
                    # 根据计算出的 current_x 和 current_y 更新位置
                    oled.fill(0)
                    oled.Bitmap(int(currentX), int(currentY), bitMap, w, h, 1)
                    oled.show()
            else:
                VastSea.Off()

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
    return luminance

def TouchPadValueSet():
    sensitivity = int(Core.Data.Get("text", "touchPadValue"))
    while not button_A.is_pressed():
        oled.fill(0)
        App.Style2(eval("[/Language('触摸键灵敏度')/]"))
        time.sleep_ms(5)
        oled.DispChar(eval("[/Language('当前值')/]") + str(sensitivity), 5, 18, 1)
        oled.show()
        if eval("[/GetButtonExpr('on')/]"):
            sensitivity = sensitivity + 5
            if sensitivity > 800:
                sensitivity = 800
            TouchPad.config(sensitivity)
        if eval("[/GetButtonExpr('py')/]"):
            sensitivity = sensitivity - 5
            if sensitivity < -100:
                sensitivity = -100
            TouchPad.config(sensitivity)
    TouchPad.config(sensitivity)
    Core.Data.Write("text",'luminance',str(sensitivity))
    return sensitivity

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
