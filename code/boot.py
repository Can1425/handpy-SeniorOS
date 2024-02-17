from mpython import oled

while True:
    oled.fill(0)
    oled.DispChar('FlagOS 启动选择器',0,0)
    oled.DispChar('A - FlagOS',0,16)
    oled.DispChar('B - main.py',0,32)
    oled.hline(50, 62, 30, 1)
    oled.show()
    while not eval("[/GetButtonExpr('thab')/]"):
        pass
    if button_a.is_pressed():
        oled.fill(0)
        oled.DispChar('将启动至FlagOS...',0,0)
        oled.show()
        from mpython import wifi
        from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
        from mpython import button_a,button_b
        import gc;gc.enable()
        runtimeDict={
                "oled":oled,"wifi":wifi(),
                "touchPad_P":touchPad_P,"touchPad_Y":touchPad_Y,"touchPad_H":touchPad_H,"touchPad_O":touchPad_O,"touchPad_N":touchPad_N,"touchPad_T":touchPad_T,
                "button_a":button_a,"button_b":button_b,
                "ntptime":__import__('ntptime'),
                "time":__import__('time'),
                "gc":gc
        }
        runtimeDict["runtimeDict"]=runtimeDict
        __import__("Flag_OS.system.main",runtimeDict)
        break
    elif button_b.is_pressed():
        oled.fill(0)
        oled.DispChar('将启动至main.py...',0,0)
        oled.show()
        break