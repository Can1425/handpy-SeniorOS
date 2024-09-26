from SeniorOS.lib.devlib import oled,touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T,button_a,button_b
import time
import gc
import sys
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import os
def ClearVar():
    for var in sys.modules:
        if not var in ('Core', 'DayLight', 'time', 'NeoPixel', '__name__', 'gc', 'uos', 'bdev', 'machine', 'count', 'oled', 'touchPad_P', 'touchPad_Y', 'touchPad_H', 'touchPad_O', 'touchPad_N', 'touchPad_T', 'sys'):
            del sys.modules[var]
    Core.FullCollect()
def Selset(ItemString:str,x,y,*MoreString):
    DayLight.VastSea.SeniorMove.Box(ItemString,x,y)
    oled.fill(0)
    oled.DispChar('启动至 %s'%(ItemString.split(" - ")[1]),5,0)
    if MoreString != None:
        for i in [0,1,2]:oled.DispChar(MoreString[i],5,(i + 1) << 4)
    oled.show()
    time.sleep(0.5)
while True:
    oled.fill(0)
    oled.DispChar(eval("[/Language('SeniorOS 启动选择器')/]") ,5,0)
    oled.DispChar('PY - SeniorOS',5,16)
    oled.DispChar('TH - REPL',5,32)
    oled.DispChar("ON - main.py",5,48)
    oled.show()
    while not eval("[/GetButtonExpr('pythonb')/]"):
        pass
    if eval("[/GetButtonExpr('py')/]"):
        Selset("PY - SeniorOS",5,16)
        gc.enable()
        oled.contrast(int(Core.Data.Get("text", "luminance")))
        __import__('SeniorOS.system.main')
        break
    elif eval("[/GetButtonExpr('on')/]"):
        Selset("ON - main.py",5,48)
        break
    elif eval("[/GetButtonExpr('th')/]"):
        Selset("TH - REPL",5,32,"屏幕缓冲区已清空")
        oled.fill(0)
        ClearVar() # 清空全局变量
        sys.exit(1)
    elif button_b.is_pressed():
        othersBuildMain = os.listdir('/SeniorOS/others_build/')
        if othersBuildMain != None:
            while not button_a.is_pressed():
                options = DayLight.Select.Style4(othersBuildMain, False, 'SeniorOS ROC')
                if options != None:
                    Selset("SeniorOS ROC - %s"%(othersBuildMain[options].replace('.mpy', '')),5,0)
                    Core.FullCollect()
                    __import__('SeniorOS.others_build.%s'%(othersBuildMain[options].replace('.mpy', '')))
                    break
