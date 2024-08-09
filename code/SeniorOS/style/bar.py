from SeniorOS.system.devlib import wifi,oled
from SeniorOS.system.devlib import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from SeniorOS.system.devlib import button_a,button_b
from SeniorOS.apps.port import *
import time
#-----------------------------------------------------------------------------------#
def Style1(appTitle):
    import SeniorOS.system.daylight as DayLight
    DayLight.Text(appTitle, 5, 0, 3, 90)
    # oled.DispChar(appTitle, 5, 0, 1)
    oled.DispChar(DayLight.UITime(True), 93, 0, 1)
#-----------------------------------------------------------------------------------#
def Style2(appTitle):
    pass
#-----------------------------------------------------------------------------------#
def Style3(appTitle):
    oled.DispChar(appTitle, 5, 0, 1)
#-----------------------------------------------------------------------------------#
def Style4(appTitle):
    oled.DispChar(appTitle, DayLight.AutoCenter(appTitle), 0, 1)