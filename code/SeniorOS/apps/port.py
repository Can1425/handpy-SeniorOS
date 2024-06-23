from mpython import *
import time
import SeniorOS.apps.logo as logo
import SeniorOS.system.daylight as DayLight
from SeniorOS.apps.main import *
import SeniorOS.system.core as Core

appNum = 0
appList = Core.Data.Get("app").split(',')
operationalJudgment = 0

def AppDynamic():
    global waitTime, select1X, select2X, select3X, select4X, appList, appNum, operationalJudgment
    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
        operationalJudgment = 0
        appNum = appNum + 1
        if appNum + 1 > len(appList):
            appNum = len(appList) - 1
            return
        waitTime = 5
        select1X = -77
        select2X = -23
        select3X = 31
        select4X = 85
        for count in range(4):
            select1X = select1X + 18
            select2X = select2X + 18
            select3X = select3X + 18
            select4X = select4X + 18
            oled.fill_rect(0, 0, 128, 43, 0)
            try:
                exec("oled.Bitmap(select1X, 10, logo.app_" + str(appNum + 1) + ", 25, 25, 1)")
            except:
                pass
            exec("oled.Bitmap(select2X, 10, logo.app_" + str(appNum) + ", 25, 25, 1)")
            try:
                exec("oled.Bitmap(select3X, 10, logo.app_" + str(appNum - 1) + ", 25, 25, 1)")
                exec("oled.Bitmap(select4X, 10, logo.app_" + str(appNum - 2) + ", 25, 25, 1)")
            except:
                pass
            oled.fill_rect(0, 47, 128, 18, 0)
            oled.show()
            time.sleep_ms(waitTime)
            waitTime = waitTime + 20
    if touchpad_o.is_pressed() and touchpad_n.is_pressed():
        operationalJudgment = 1
        appNum = appNum - 1
        if appNum < 0:
            appNum = 0
            return
        waitTime = 5
        select1X = 172
        select2X = 118
        select3X = 64
        select4X = 10
        for count in range(4):
            select1X = select1X + -18
            select2X = select2X + -18
            select3X = select3X + -18
            select4X = select4X + -18
            oled.fill_rect(0, 0, 128, 43, 0)
            try:
                exec("oled.Bitmap(select1X, 10, logo.app_" + str(appNum - 1) + ", 25, 25, 1)")
            except:
                pass
            exec("oled.Bitmap(select2X, 10, logo.app_" + str(appNum) + ", 25, 25, 1)")
            try:
                exec("oled.Bitmap(select3X, 10, logo.app_" + str(appNum + 1) + ", 25, 25, 1)")
                exec("oled.Bitmap(select4X, 10, logo.app_" + str(appNum + 2) + ", 25, 25, 1)")
            except:
                pass
            oled.fill_rect(0, 47, 128, 18, 0)
            oled.show()
            time.sleep_ms(waitTime)
            waitTime = waitTime + 20

def App():
    global waitTime, select1X, select2X, select3X, select4X, appNum
    appNum = 0
    select1X = -5
    select2X = 49
    oled.fill(0)
    oled.Bitmap(select1X, 10, logo.app_1, 25, 25, 1)
    oled.Bitmap(select2X, 10, logo.app_0, 25, 25, 1)
    oled.show()
    while not (button_a.is_pressed() or touchpad_t.is_pressed() and touchpad_h.is_pressed()):
        oled.hline(4, 46, 126, 1)
        oled.show()
        oled.DispChar(str('〔'), 30, 20, 1)
        oled.DispChar(str('〕'), 85, 20, 1)
        oled.DispChar(str('>'), 120, 48, 1)
        oled.DispChar(str('<'), 1, 48, 1)
        oled.DispChar(appList[appNum],DayLight.AutoCenter(appList[appNum]), 48, 1)
        oled.show()
        AppDynamic()
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            DayLight.VastSea.AppsPage.Open(30,85,DayLight.AutoCenter(appList[appNum]),46,25,25,48,10,appNum)
            exec(str("app_"+ str(appNum) +"()"))
            DayLight.VastSea.AppsPage.Close(-40,157,1,None,-11,-11,0,None,appNum)
            if operationalJudgment == 0:
                try:
                    exec("oled.Bitmap(select1X, 10, logo.app_" + str(appNum + 1) + ", 25, 25, 1)")
                except:
                    pass
                exec("oled.Bitmap(select2X, 10, logo.app_" + str(appNum) + ", 25, 25, 1)")
                try:
                    exec("oled.Bitmap(select3X, 10, logo.app_" + str(appNum - 1) + ", 25, 25, 1)")
                    exec("oled.Bitmap(select4X, 10, logo.app_" + str(appNum - 2) + ", 25, 25, 1)")
                except:
                    pass
                oled.show()
            elif operationalJudgment == 1:
                try:
                    exec("oled.Bitmap(select1X, 10, logo.app_" + str(appNum - 1) + ", 25, 25, 1)")
                except:
                    pass
                exec("oled.Bitmap(select2X, 10, logo.app_" + str(appNum) + ", 25, 25, 1)")
                try:
                    exec("oled.Bitmap(select3X, 10, logo.app_" + str(appNum + 1) + ", 25, 25, 1)")
                    exec("oled.Bitmap(select4X, 10, logo.app_" + str(appNum + 2) + ", 25, 25, 1)")
                except:
                    pass
                oled.show()