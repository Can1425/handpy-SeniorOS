from SeniorOS.system.devlib import *
import SeniorOS.system.pages_manager as PagesManager
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import urequests

source = "https://" + Core.Data.Get("text", "poetrySource")

def Poetry():
    global poetry, source
    _response = urequests.get(source, headers={})
    poetry = _response.text.split('，')

def Main():
    Poetry()
    while not button_a.is_pressed():
        oled.fill(0)
        DayLight.App.Style1('即时诗词')
        if eval("[/GetButtonExpr('th')/]"):
            Poetry()
        try:
            oled.DispChar(poetry[0], 5, 18, 1)
            oled.DispChar(poetry[1], 5, 34, 1)
            oled.DispChar('TH - 刷新', 5, 50, 1)
        except:
            # try:
            oled.DispChar(poetry[0], 5, 18, 1)
            oled.DispChar('TH - 刷新', 5, 50, 1)
            # except:
                # oled.DispChar('诗词走丢啦！', 5, 18, 1)
                # oled.DispChar('TH - 刷新', 5, 50, 1)
        oled.show()