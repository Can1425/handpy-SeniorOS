from mpython import *
import time,uos
import SeniorOS.system.core as Core
import audio

audio.stop()
audio.player_init()

def RenameCode():
    time.sleep(1.5)
    uos.rename('/main.py.bak','/main.py')
while True:
    oled.fill(0)
    oled.DispChar('SeniorOS 启动选择器',0,0)
    oled.DispChar('A - SeniorOS',0,16)
    oled.DispChar('B - main.py',0,32)
    oled.DispChar("TH - REPL",0,48)
    oled.show()
    while not eval("[/GetButtonExpr('thab')/]"):
        pass
    if button_a.is_pressed():
        oled.fill(0)
        oled.DispChar('启动至 SeniorOS',0,0)
        oled.show()
        time.sleep(0.5)
        from mpython import wifi
        from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
        from mpython import button_a,button_b
        import gc;gc.enable()
        global runtimeDict
        runtimeDict={
                "oled":oled,"wifi":wifi(),
                "touchPad_P":touchPad_P,"touchPad_Y":touchPad_Y,"touchPad_H":touchPad_H,"touchPad_O":touchPad_O,"touchPad_N":touchPad_N,"touchPad_T":touchPad_T,
                "button_a":button_a,"button_b":button_b,
                "ntptime":__import__('ntptime'),
                "time":time,
                "gc":gc,
                "os":uos
        }
        runtimeDict["runtimeDict"]=runtimeDict # 因为这玩意是要一直传下去的 总不能互相干扰对方命名空间
        oled.contrast(int(Core.Data.Get('luminance')))
        import SeniorOS.system.main
        break
    elif button_b.is_pressed():
        oled.fill(0)
        oled.DispChar('启动至 main.py',0,0)
        oled.show()
        time.sleep(0.5)
        break
    elif eval("[/GetButtonExpr('th','and')/]"):
        oled.fill(0)
        oled.DispChar('启动至REPL...',0,0)
        oled.DispChar("缓冲区下 屏幕已oled.fill(0)",0,16,auto_return=True)
        oled.show()
        oled.fill(0)
        uos.rename('/main.py','/main.py.bak') # 先重命名main.py 直接进入REPL
        __import__("_thread").start_new_thread(RenameCode,()) # 开多线程 在1s后(已进入REPL)时重命名回去
        break