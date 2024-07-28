from mpython import *
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import urequests

Poetry()
while not eval("[/GetButtonExpr('a')/]"):
    oled.fill(0)
    DayLight.app('即时诗词')
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        Poetry()
    try:
        oled.DispChar(poetry[0], 5, 18, 1)
        oled.DispChar(poetry[1], 5, 34, 1)
        oled.DispChar('TH - 刷新', 5, 50, 1)
    except:
        try:
            oled.DispChar(poetry[0], 5, 18, 1)
            oled.DispChar('TH - 刷新', 5, 50, 1)
        except:
            oled.DispChar('诗词走丢啦！', 5, 18, 1)
            oled.DispChar('TH - 刷新', 5, 50, 1)
    oled.show()


def Poetry():
    global poetry
    try:
        _response = urequests.get(Data.LocalApps.poetrySource, headers={})
        poetry = (_response.text.split('，'))
        return
    except:
        return