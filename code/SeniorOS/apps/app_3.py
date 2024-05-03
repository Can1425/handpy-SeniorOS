from mpython import *
import urequests
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import json
image_picture = Image()

def app_3():
    num = 1
    while not button_a.is_pressed():
        DayLight.app('手电筒')
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            num = 1
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            num = 0
        if num == 1:
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
    num = 0
    rgb.fill( (0, 0, 0) )
    rgb.write()
    time.sleep_ms(1)
    return