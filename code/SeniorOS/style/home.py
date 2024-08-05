from SeniorOS.system.devlib import *
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
    oled.DispChar_font(font.digiface_21,  DayLight.UITime(True), 28, 10)
    oled.DispChar_font(font.digiface_11, (''.join([str(x) for x in [time.localtime()[0], '.', time.localtime()[1], '.', time.localtime()[2]]])), 40, 35)
    oled.show()
#-----------------------------------------------------------------------------------#
def Style2():
    oled.fill(0)
    oled.DispChar_font(font.dvsmb_21, DayLight.UITime(True), 8, 8)
    oled.DispChar_font(font.dvsmb_12, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 8, 28)
    oled.show()
#-----------------------------------------------------------------------------------#
def Style3():
    oled.fill(0)
    oled.DispChar_font(SeniorOS.fonts.misans, DayLight.UITime(True), 5, 10)
    oled.DispChar_font(SeniorOS.fonts.misans_16, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 5, 35)
    oled.show()
#-----------------------------------------------------------------------------------#
def Style4():
    oled.fill(0)
    oled.DispChar_font(SeniorOS.fonts.HarmonyOS_sans_bold, DayLight.UITime(True), 20, 20)
    oled.DispChar_font(font.dvsmb_12, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), DayLight.AutoCenter((''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]]))), 45)
    oled.show()