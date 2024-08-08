from SeniorOS.system.devlib import wifi,oled
from SeniorOS.system.devlib import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from SeniorOS.system.devlib import button_a,button_b
from SeniorOS.apps.port import *
import SeniorOS.system.pages_manager as PagesManager
import SeniorOS.system.dynamic_run_page as DynamicRun
import time
Manager = PagesManager.main('style/bar.mpy')
#-----------------------------------------------------------------------------------#
@Manager.regScreen('Style1')
@Manager.setPagesEntryPoint()
def Style1(appTitle):
    import SeniorOS.system.daylight as DayLight
    DayLight.Text(appTitle, 5, 0, 3, 90)
    # oled.DispChar(appTitle, 5, 0, 1)
    oled.DispChar(DayLight.UITime(True), 93, 0, 1)
#-----------------------------------------------------------------------------------#
@Manager.regScreen('Style1')
@Manager.setPagesEntryPoint()
def Style2(appTitle):
    pass
#-----------------------------------------------------------------------------------#
@Manager.regScreen('Style1')
@Manager.setPagesEntryPoint()
def Style3(appTitle):
    oled.DispChar(appTitle, 5, 0, 1)
#-----------------------------------------------------------------------------------#
@Manager.regScreen('Style1')
@Manager.setPagesEntryPoint()
def Style4(appTitle):
    oled.DispChar(appTitle, DayLight.AutoCenter(appTitle), 0, 1)