from mpython import wifi,oled
from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from mpython import button_a,button_b
from SeniorOS.style.port import *
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import time

import SeniorOS.fonts.misans
import SeniorOS.fonts.misans_16
import SeniorOS.fonts.HarmonyOS_sans_bold
import font.dvsmb_21
import font.dvsmb_12
import font.digiface_21
import font.digiface_11

#-----------------------------------------------------------------------------------#

def Style1():
    oled.fill(0)
    DayLight.DisplayFont(font.digiface_21,  DayLight.UITime(True), 28, 10, False, 2)
    DayLight.DisplayFont(font.digiface_11, (''.join([str(x) for x in [time.localtime()[0], '.', time.localtime()[1], '.', time.localtime()[2]]])), 40, 35, False, 2)
    oled.show()
#-----------------------------------------------------------------------------------#
def Style2():
    oled.fill(0)
    DayLight.DisplayFont(font.dvsmb_21, DayLight.UITime(True), 8, 8, False)
    DayLight.DisplayFont(font.dvsmb_12, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 8, 28, False)
    oled.show()
#-----------------------------------------------------------------------------------#
def Style3():
    oled.fill(0)
    DayLight.DisplayFont(SeniorOS.fonts.misans, DayLight.UITime(True), 5, 10, False)
    DayLight.DisplayFont(SeniorOS.fonts.misans_16, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 5, 35, False)
    oled.show()
#-----------------------------------------------------------------------------------#
def Style4():
    oled.fill(0)
    DayLight.DisplayFont(SeniorOS.fonts.HarmonyOS_sans_bold, DayLight.UITime(True), 20, 20, False)
    DayLight.DisplayFont(font.dvsmb_12, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), DayLight.AutoCenter((''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]]))), 45, False)
    oled.show()