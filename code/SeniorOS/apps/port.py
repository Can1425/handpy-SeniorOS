from mpython import *
import SeniorOS.apps.logo as logo
import SeniorOS.system.daylight as DayLight
from SeniorOS.apps.main import *
import SeniorOS.system.core as Core

def app():
    ts = Core.Data.Get("app")
    app_list = (ts.split(','))
    home_movement_x = 40
    app_num = 0
    time.sleep_ms(20)
    while not button_a.is_pressed():
        try:
          oled.invert(int(Core.Data.Get('light')))
        except:
            pass
        if home_movement_x >= 0 and home_movement_x <= 224:
            if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
                home_movement_x = home_movement_x + 10
            elif touchPad_O.is_pressed() and touchPad_N.is_pressed():
                home_movement_x = home_movement_x + -10
        else:
            if home_movement_x <= 0:
                home_movement_x = 4
            elif home_movement_x >= 280:
                home_movement_x = 275
        oled.fill(0)
        oled.RoundRect(home_movement_x, 6, 36, 36, 3, 1)
        oled.RoundRect((home_movement_x - 40), 6, 36, 36, 3, 1)
        oled.RoundRect((home_movement_x - 80), 6, 36, 36, 3, 1)
        oled.RoundRect((home_movement_x - 120), 6, 36, 36, 3, 1)
        oled.RoundRect((home_movement_x - 160), 6, 36, 36, 3, 1)
        oled.RoundRect((home_movement_x - 200), 6, 36, 36, 3, 1)
        oled.Bitmap(home_movement_x + 5, 12, logo.app_0, 25, 25, 1)
        oled.Bitmap(home_movement_x - 40 + 5, 12, logo.app_1, 25, 25, 1)
        oled.Bitmap(home_movement_x - 80 + 5, 12, logo.app_3, 25, 25, 1)
        oled.Bitmap(home_movement_x - 120 + 5, 12, logo.app_3, 25, 25, 1)
        oled.Bitmap(home_movement_x - 160 + 5, 12, logo.app_4, 25, 25, 1)
        oled.Bitmap(home_movement_x - 200 + 5, 12, logo.app_5, 25, 25, 1)
        oled.DispChar(app_list[app_num],DayLight.AutoCenter(app_list[app_num]),45)
        oled.hline(50, 62, 30, 1)
        if home_movement_x >= 0 and home_movement_x <= 50:
            app_num = 0
            app_logo = logo.app_0
        elif home_movement_x >= 51 and home_movement_x <= 95:
            app_num = 1
            app_logo = logo.app_1
        elif home_movement_x >= 96 and home_movement_x <= 130:
            app_num = 2
            app_logo = logo.app_3
        elif home_movement_x >= 131 and home_movement_x <= 175:
            app_num = 3
            app_logo = logo.app_3
        elif home_movement_x >= 176 and home_movement_x <= 220:
            app_num = 4
            app_logo = logo.app_4
        elif home_movement_x >= 221 and home_movement_x <= 275:
            app_num = 5
            app_logo = logo.app_5
        oled.show()
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            DayLight.ConsaniAppOpen(home_movement_x, 6, 128, 36, 64, 36, 3, app_logo, home_movement_x + 5)
            class SeniorOSAPI:
                Core=Core
                DayLight=DayLight
            exec(str("app_"+ str(app_num) +"()"))
            DayLight.ConsaniAppClose(home_movement_x, 6, 128, 36, 64, 36, 3, app_logo, home_movement_x + 5)
    return