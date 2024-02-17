from mpython import *
#import time #LP's PR:此处加载程序建议加一点点等待时间，否则下面显示加约等于没加，还浪费RAM
while True:#LP's PR:给点用户可选的启动啊喂，很烦的！！
    oled.DispChar('FlagOS 启动选择器',0,0)
    oled.DispChar('A - FlagOS',0,16)
    oled.DispChar('B - main.py',0,32)
    oled.hline(50, 62, 30, 1)
    while not eval("[/GetButtonExpr('thab')/]"):
        pass
    if button_a.is_pressed():
        oled.fill(0)
        oled.DispChar('将启动至FlagOS...',0,0)
        oled.show()
        #time.sleep(0.5) #详见PR的line2
        import Flag_OS.system.main
        break
    elif button_b.is_pressed():
        oled.fill(0)
        oled.DispChar('将启动至main.py...',0,0)
        oled.show()
        #time.sleep(0.5) #详见PR的line2
        break