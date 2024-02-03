from mpython import *
while True:
    oled.fill(0)
    oled.invert(0)
    oled.DispChar(str('Flag OS BIOS'), 5, 5, 1, True)
    oled.DispChar(str('A - System'), 5, 18, 1, True)
    oled.DispChar(str('B - User(main.py)'), 5, 32, 1)
    oled.hline(50, 62, 30, 1)
    oled.show()
    if button_a.is_pressed():
        oled.fill(0)
        oled.DispChar(str('Attempting to boot to System...'), 0, 0, 1, True)
        oled.show()
        import flagos.system.main
        break
    elif button_b.is_pressed():
        oled.fill(0)
        oled.DispChar(str('Attempting to boot to User(main.py)...'), 0, 0, 1, True)
        oled.show()
        break


