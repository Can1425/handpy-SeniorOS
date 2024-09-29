from SeniorOS.lib.devlib import *
from SeniorOS.apps.logo import Logo
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import sys,os,gc
import SeniorOS.lib.pages_manager as PagesManager

appNum = 0
operationalJudgment = 0
List = Core.Data.Get("list", "localAppName")
appDir=os.listdir("/SeniorOS/apps")
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
            oled.fill_rect(0,0,128,46,0)
            if bitMap0 != None:oled.Bitmap(int(currentX - 120), int(currentY), bitMap0, 25, 25, 1)
            if bitMap1 != None:oled.Bitmap(int(currentX - 60), int(currentY), bitMap1, 25, 25, 1)
            oled.Bitmap(int(currentX), int(currentY), bitMap2, 25, 25, 1)
            if bitMap3 !=None:oled.Bitmap(int(currentX + 60), int(currentY), bitMap3, 25, 25, 1)
            if bitMap4 != None:
                oled.Bitmap(int(currentX + 120), int(currentY), bitMap4, 25, 25, 1)
            oled.show()
    else:
        DayLight.VastSea.Off()
def PYTouch(a,b,c,d):Bitmap(a, b, c, d, None, 50, 10, 110, 10)
def ONTouch(a,b,c,d,e):Bitmap(a, b, c, d, e, 50, 10, -10, 10)
def App():
    global appNum
    appNum = 0
    while not eval("[/GetButtonExpr('ath')/]"):
        oled.fill_rect(0,50,128,16,0)
        try:oled.DispChar("<  {}  >".format(List[appNum]),DayLight.AutoCenter("<  {}  >".format(List[appNum])), 48, 1)
        except:appNum-=1;oled.DispChar("<  {}  >".format(List[appNum]),DayLight.AutoCenter("<  {}  >".format(List[appNum])), 48, 1)
        if appNum - 1 >= 0:
            oled.Bitmap(-10, 10, Logo[appNum - 1], 25, 25, 1)
        oled.Bitmap(50, 10, Logo[appNum], 25, 25, 1)
        if appNum < len(Logo) - 1:
            oled.Bitmap(110, 10, Logo[appNum + 1], 25, 25, 1)
        oled.hline(0, 46, 128, 1)
        oled.show()
        oled.fill_rect(0,50,128,16,0)
        oled.DispChar("<  {}  >".format(List[appNum]),DayLight.AutoCenter("<  {}  >".format(List[appNum])), 48, 1)
        if eval("[/GetButtonExpr('py')/]"):
                if appNum - 1 >= 0:
                    if appNum - 2 >= 0 and not (appNum == len(Logo) - 1):
                        PYTouch(Logo[appNum - 2], Logo[appNum - 1], Logo[appNum], Logo[appNum + 1])
                    elif appNum == len(Logo) - 1:
                        try:PYTouch(Logo[appNum - 2], Logo[appNum - 1], Logo[appNum], None)
                        except:PYTouch(None, Logo[appNum - 1], Logo[appNum], None)
                    else:
                        PYTouch(None, Logo[appNum - 1], Logo[appNum], Logo[appNum + 1])
                    appNum -= 1
        elif eval("[/GetButtonExpr('on')/]"):
            if appNum + 2 <= len(Logo) - 1:
                if appNum - 1 >= 0:
                    ist = appNum - 2 >= 0#温馨提示，这里所有的ist都是bool类型，只占1个字节，不用改了
                    ONTouch((Logo[appNum - 2] if ist else None), 
                            Logo[appNum - 1],Logo[appNum], Logo[appNum + 1], Logo[appNum + 2])
                else:
                    ONTouch(None, None, Logo[appNum], Logo[appNum + 1], Logo[appNum + 2])
            elif appNum + 1 <= len(Logo) - 1:
                if appNum - 1 >= 0:
                    ist = appNum - 2 >= 0
                    ONTouch((Logo[appNum - 2] if ist else None),
                            Logo[appNum - 1],Logo[appNum], Logo[appNum + 1], None)
                else:
                    ONTouch(None, None, Logo[appNum], Logo[appNum + 1], None)
            appNum += 1
        elif eval("[/GetButtonExpr('th')/]"):
            DayLight.VastSea.SeniorMove.Text(List[appNum], DayLight.AutoCenter(List[appNum]), 48, 5, 0)
            PagesManager.Main.Import('SeniorOS.apps.%s'%appDir[appNum], 'Main')
            del sys.modules["{}.apps.{}".format(eval("[/Const('systemName')/]"),appDir[appNum])]
            gc.collect()
            DayLight.VastSea.SeniorMove.Text(List[appNum], 5, 0, DayLight.AutoCenter(List[appNum]), 48)