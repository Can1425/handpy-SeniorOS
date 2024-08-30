from SeniorOS.lib.devlib import *
import SeniorOS.lib.pages_manager as PagesManager
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
image_picture = Image()
rgb.brightness(1.0)

def Main():
    mode = True
    while not button_a.is_pressed():
        DayLight.App.Style1('手电筒')
        if mode:
            oled.blit(image_picture.load('face/System/Dot_full.pbm', 0), 48, 20)
            oled.show()
            rgb.fill((int(255), int(255), int(255)))
            rgb.write()
            time.sleep_ms(1)
        else:
            oled.blit(image_picture.load('face/System/Dot_empty.pbm', 0), 48, 20)
            oled.show()
            rgb.fill( (0, 0, 0) )
            rgb.write()
        while not button_a.is_pressed():
            if eval("[/GetButtonExpr('py')/]"):
                mode = 1
                break
            if eval("[/GetButtonExpr('on')/]"):
                mode = 0
                break
    mode = 0
    rgb.fill( (0, 0, 0) )
    rgb.write()
    time.sleep_ms(1)