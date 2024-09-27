from SeniorOS.lib.devlib import *
import SeniorOS.system.daylight as DayLight
import time
import SeniorOS.fonts.misans
import SeniorOS.fonts.misans_16
import font.dvsmb_21
import font.dvsmb_12
import font.digiface_21
import font.digiface_11
import urequests
import SeniorOS.lib.pages_manager as PagesManager
import SeniorOS.system.core as Core
pagesNum = 0
DLTIME=DayLight.UITime(True)

#-----------------------------------------------------------------------------------#
def Style1():
    oled.fill(0)
    oled.DispChar_font(font.digiface_21, DLTIME, 28, 10)
    oled.DispChar_font(font.digiface_11, (''.join([str(x) for x in [time.localtime()[0], '.', time.localtime()[1], '.', time.localtime()[2]]])), 40, 35)
    oled.show()
#-----------------------------------------------------------------------------------#
def Style2():
    oled.fill(0)
    oled.DispChar_font(font.dvsmb_21, DLTIME, 8, 8)
    oled.DispChar_font(font.dvsmb_12, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 8, 28)
    oled.show()
#-----------------------------------------------------------------------------------#
class Style3Dependencies:
    def IsPYTouth():
        global pagesNum
        if pagesNum >= 0: pagesNum -= 1
        PagesManager.Main.Import("SeniorOS.style.home", "Page%d"%pagesNum)

    def IsONTouth():
        global pagesNum
        if pagesNum <= 1: pagesNum += 1
        PagesManager.Main.Import("SeniorOS.style.home", "Page%d"%pagesNum)
    
    def Page0():
            oled.fill(0)
            oled.DispChar_font(SeniorOS.fonts.misans, DLTIME, 5, 10)
            oled.DispChar_font(SeniorOS.fonts.misans_16, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 5, 35)
            oled.show()
            if eval("[/GetButtonExpr('py')/]"):
                PagesManager.Main.Import("SeniorOS.system.pages", "ShutDown")

    def Page1():
        while not eval("[/GetButtonExpr('py')/]") or eval("[/GetButtonExpr('on')/]"):
            oled.fill(0)
            myUI = UI(oled)
            oled.DispChar('运行时间', 5, 0, 1)
            oled.DispChar("{}s".format(time.time()), 5, 16, 1)
            oled.DispChar('今日已过', 5, 32, 1)
            myUI.ProgressBar(5, 50, 50, 8, time.localtime()[3] // 0.24)
            myUI.qr_code('https://senior.flowecho.org', 65, 0, scale=2)
            oled.show()
            if eval("[/GetButtonExpr('th')/]"):
                PagesManager.Main.Import("SeniorOS.system.pages", "ShutDown")


Style3 = Page0 = Style3Dependencies.Page0
Page1 = Style3Dependencies.Page1
IsPYTouth=Style3Dependencies.IsPYTouth
IsONTouth=Style3Dependencies.IsONTouth
#-----------------------------------------------------------------------------------#