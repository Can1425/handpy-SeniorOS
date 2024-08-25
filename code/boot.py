from SeniorOS.system.devlib import oled,touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
import time
import uos
import gc
import sys
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
Core.FullCollect()

def RenameCode():
    uos.rename('/main.py.bak','/main.py')
def ClearVar():
    Core.FullCollect()
    for var in sys.modules:
        if not var in ('Core', 'DayLight', 'time', 'NeoPixel', '__name__', 'gc', 'uos', 'bdev', 'machine', 'count', 'oled', 'touchPad_P', 'touchPad_Y', 'touchPad_H', 'touchPad_O', 'touchPad_N', 'touchPad_T', 'sys'):
            del sys.modules[var]
    gc.collect()
while True:
    oled.fill(0)
    oled.DispChar(eval("[/Language('SeniorOS 启动选择器')/]") ,5,0)
    oled.DispChar('PY - SeniorOS',5,16)
    oled.DispChar('TH - REPL',5,32)
    oled.DispChar("ON - main.py",5,48)
    oled.show()
    while not eval("[/GetButtonExpr('python')/]"):
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
        ClearVar()
        time.sleep(0.5)
        break
    elif eval("[/GetButtonExpr('th')/]"):
        DayLight.VastSea.SeniorMove.Box("TH - REPL",5,32)
        oled.fill(0)
        oled.DispChar('启动至 REPL',5,0)
        oled.DispChar("屏幕缓冲区已清空",5,16,out=3,return_x=5,maximum_x=126)
        oled.show()
        oled.fill(0)
        try:
            uos.rename('/main.py','/main.py.bak') # 先重命名main.py 直接进入REPL
            __import__("_thread").start_new_thread(RenameCode,()) # 开多线程 在1s后(已进入REPL)时重命名回去
        except:
            pass
        ClearVar() # 清空全局变量
        break