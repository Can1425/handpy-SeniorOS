from mpython import *

while True:
    oled.DispChar('FlagOS 启动选择器',0,0)
    oled.DispChar('A - FlagOS',0,16)
    oled.DispChar('B - main.py',0,32)
    oled.hline(50, 62, 30, 1)
    while not (button_a.value()==0 or button_b.value()==0):
        pass
    if button_a.is_pressed():
        oled.fill(0)
        oled.DispChar('将启动至FlagOS...',0,0)
        oled.show()
        import Flag_OS.system.main
        break
    elif button_b.is_pressed():
        oled.fill(0)
        oled.DispChar('将启动至main.py...',0,0)
        oled.show()
        break