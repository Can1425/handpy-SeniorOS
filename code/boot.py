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
        DayLight.VastSea.SeniorMove.Box("PY - SeniorOS",5,16)
        oled.fill(0)
        oled.DispChar('启动至 SeniorOS',5,0)
        oled.show()
        time.sleep(0.5)
        gc.enable()
        oled.contrast(int(Core.Data.Get("text", "luminance")))
        import SeniorOS.system.main
        break
    elif eval("[/GetButtonExpr('on')/]"):
        DayLight.VastSea.SeniorMove.Box("ON - main.py",5,48)
        oled.fill(0)
        oled.DispChar('启动至 main.py',5,0)
        oled.show()
        time.sleep(0.5)
        break
    elif eval("[/GetButtonExpr('th')/]"):
        DayLight.VastSea.SeniorMove.Box("TH - REPL",5,32)
        oled.fill(0)
        oled.DispChar('启动至 REPL',5,0)
        oled.DispChar("屏幕缓冲区已清空",5,16,out=3,return_x=5,maximum_x=126)
        oled.show()
        oled.fill(0)
        ClearVar() # 清空全局变量
        sys.exit(1)
    elif button_b.is_pressed():
        othersBuildMain = os.listdir('/SeniorOS/others_build/')
        if othersBuildMain != None:
            while not button_a.is_pressed():
                options = DayLight.Select.Style4(othersBuildMain, False, 'SeniorOS ROC')
                if options != None:
                    oled.fill(0)
                    oled.DispChar('启动至 ' + othersBuildMain[options].replace('.mpy', ''), 5, 0)
                    oled.show()
                    time.sleep(0.5)
                    Core.FullCollect()
                    __import__('SeniorOS.others_build.' + othersBuildMain[options].replace('.mpy', ''))
                    break
