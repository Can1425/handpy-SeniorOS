from mpython import *
import Flag_OS.system.core

def time():
    try:
        oled.fill(0)
        oled.DispChar(str('请稍等...'), 0, 0, 1)
        oled.show()
        ntptime.settime(8, "time.windows.com")
        oled.fill(0)
        oled.DispChar(str('成功'), 0, 0, 1)
        oled.show()
        Flag_OS.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
    except:
        Flag_OS.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
        oled.fill(0)
        oled.DispChar(str('失败'), 0, 0, 1)
        oled.show()
        flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)

def collect():
    try:
        oled.fill(0)
        oled.DispChar(str('请稍等...'), 0, 0, 1)
        oled.show()
        Flag_OS.system.core.collect()
        oled.fill(0)
        oled.DispChar(str('成功'), 0, 0, 1)
        oled.show()
        Flag_OS.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
    except:
        Flag_OS.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
        oled.fill(0)
        oled.DispChar(str('失败'), 0, 0, 1)
        oled.show()
        Flag_OS.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)