from SeniorOS.system.devlib import *
import time,uos
import SeniorOS.system.core as Core

def RenameCode():
    time.sleep(1.5)
    uos.rename('/main.py.bak','/main.py')
while True:
    oled.fill(0)
    oled.DispChar(eval("[/Language('SeniorOS 启动选择器')/]") ,5,0)
    oled.DispChar('PY - SeniorOS',5,16)
    oled.DispChar('TH - REPL',5,32)
    oled.DispChar("ON - main.py",5,48)
    oled.show()
    while not eval("[/GetButtonExpr('pythonb')/]"):
        pass
    if eval("[/GetButtonExpr('py','and')/]"):
        oled.fill(0)
        oled.DispChar('启动至 SeniorOS',5,0)
        oled.show()
        time.sleep(0.5)
        import gc;gc.enable()
        oled.contrast(int(Core.Data.Get("text", "luminance")))
        import SeniorOS.system.main
        break
    elif eval("[/GetButtonExpr('on','and')/]"):
        oled.fill(0)
        oled.DispChar('启动至 main.py',5,0)
        oled.show()
        time.sleep(0.5)
        break
    elif eval("[/GetButtonExpr('th','and')/]"):
        oled.fill(0)
        oled.DispChar('启动至 REPL',5,0)
        oled.DispChar("缓冲区下 屏幕已oled.fill(0)",5,16,out=3,return_x=5,maximum_x=126)
        oled.show()
        oled.fill(0)
        try:
            uos.rename('/main.py','/main.py.bak') # 先重命名main.py 直接进入REPL
            __import__("_thread").start_new_thread(RenameCode,()) # 开多线程 在1s后(已进入REPL)时重命名回去
        except:
            pass
        break