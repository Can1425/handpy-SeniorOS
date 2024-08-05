from SeniorOS.system.devlib import *
import SeniorOS.system.app_manager as ImportAppManager
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import urequests

def Poetry():
    global poetry
    try:
        _response = urequests.get(Core.Data.Get("text", "poetrySource"), headers={})
        poetry = (_response.text.split('，'))
        return
    except:
        return

AppManager = ImportAppManager.AppManager
manager = AppManager('即时诗词')

@manager.regScreen('main')
@manager.setAppEntryPoint()
def main():
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
            try:
                oled.DispChar(poetry[0], 5, 18, 1)
                oled.DispChar('TH - 刷新', 5, 50, 1)
            except:
                oled.DispChar('诗词走丢啦！', 5, 18, 1)
                oled.DispChar('TH - 刷新', 5, 50, 1)
        oled.show()

manager.Run()