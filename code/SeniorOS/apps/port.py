from SeniorOS.lib.devlib import *
import time
import micropython
from SeniorOS.apps.logo import Logo
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import sys,os,gc
import SeniorOS.lib.pages_manager as PagesManager

appNum = 0
operationalJudgment = 0
List = Core.Data.Get("list", "localAppName")
appDir=os.listdir("SeniorOS/apps")
for i in range(len(appDir)):
    if appDir[i]!="port.py" or appDir[i]!="logo.py":
        appDir[i]=appDir[i].replace(".mpy","")

def Bitmap(bitMap0, bitMap1, bitMap2, bitMap3, bitMap4, startX, startY, endX, endY):
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
            if bitMap0 != None:
                oled.Bitmap(int(currentX - 120), int(currentY), bitMap0, 25, 25, 1)
            if bitMap1 != None:
                oled.Bitmap(int(currentX - 60), int(currentY), bitMap1, 25, 25, 1)
            oled.Bitmap(int(currentX), int(currentY), bitMap2, 25, 25, 1)
            oled.Bitmap(int(currentX + 60), int(currentY), bitMap3, 25, 25, 1)
            if bitMap4 != None:
                oled.Bitmap(int(currentX + 120), int(currentY), bitMap4, 25, 25, 1)
            oled.show()
    else:
        DayLight.VastSea.Off()

def App():
    global appNum
    appNum = 0
    while not eval("[/GetButtonExpr('ath')/]"):
        oled.DispChar('>', 120, 48, 1)
        oled.DispChar('<', 1, 48, 1)
        oled.DispChar(List[appNum],DayLight.AutoCenter(List[appNum]), 48, 1)
        if appNum - 1 >= 0:
            oled.Bitmap(-10, 10, Logo[appNum - 1], 25, 25, 1)
        oled.Bitmap(50, 10, Logo[appNum], 25, 25, 1)
        if appNum + 1 < len(Logo) - 1:
            oled.Bitmap(110, 10, Logo[appNum + 1], 25, 25, 1)
        oled.hline(0, 46, 128, 1)
        oled.show()
        if eval("[/GetButtonExpr('py')/]"):
            if appNum - 1 >= 0:
                if appNum - 2 >= 0:
                    Bitmap(Logo[appNum - 2], Logo[appNum - 1], Logo[appNum], Logo[appNum + 1], None, 50, 10, 110, 10)
                else:
                    Bitmap(None, Logo[appNum - 1], Logo[appNum], Logo[appNum + 1], None, 50, 10, 110, 10)
                appNum -= 1
        if eval("[/GetButtonExpr('on')/]"):
            if appNum + 2 <= len(Logo) - 1:
                if appNum - 1 >= 0:
                    if appNum - 2 >= 0:
                        Bitmap(Logo[appNum - 2], Logo[appNum - 1], Logo[appNum], Logo[appNum + 1], Logo[appNum + 2], 50, 10, -10, 10)
                    else:
                        Bitmap(None, Logo[appNum - 2], Logo[appNum], Logo[appNum + 1], Logo[appNum + 2], 50, 10, -10, 10)
                else:
                    Bitmap(None, None, Logo[appNum], Logo[appNum + 1], Logo[appNum + 2], 50, 10, -10, 10)
            elif appNum + 1 <= len(Logo) - 1:
                if appNum - 1 >= 0:
                    if appNum - 2 >= 0:
                        Bitmap(Logo[appNum - 2], Logo[appNum - 1], Logo[appNum], Logo[appNum + 1], None, 50, 10, -10, 10)
                    else:
                        Bitmap(None, Logo[appNum - 2], Logo[appNum], Logo[appNum + 1], None, 50, 10, -10, 10)
                else:
                    Bitmap(None, None, Logo[appNum], Logo[appNum + 1], None, 50, 10, -10, 10)
            appNum += 1
        if eval("[/GetButtonExpr('th')/]"):
            DayLight.VastSea.SeniorMove.Text(List[appNum], DayLight.AutoCenter(List[appNum]), 48, 5, 0)
            PagesManager.Main.Import('SeniorOS.apps.' + str(appDir[appNum]), 'Main')
            del sys.modules[eval("[/Const('systemName')/]") + '.apps.' + str(appDir[appNum])]
            gc.collect()
            DayLight.VastSea.SeniorMove.Text(List[appNum], 5, 0, DayLight.AutoCenter(List[appNum]), 48)