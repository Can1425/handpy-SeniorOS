from SeniorOS.system.devlib import *
import SeniorOS.system.daylight as DayLight
import time
import SeniorOS.fonts.misans
import SeniorOS.fonts.misans_16
import font.dvsmb_21
import font.dvsmb_12
import font.digiface_21
import font.digiface_11

DLTIME=DayLight.UITime(True)
#-----------------------------------------------------------------------------------#

def Style1():
    oled.fill(0)
    oled.DispChar_font(font.digiface_21,  DLTIME, 28, 10)
    oled.DispChar_font(font.digiface_11, (''.join([str(x) for x in [time.localtime()[0], '.', time.localtime()[1], '.', time.localtime()[2]]])), 40, 35)
    oled.show()
    return
#-----------------------------------------------------------------------------------#
def Style2():
    oled.fill(0)
    oled.DispChar_font(font.dvsmb_21, DLTIME, 8, 8)
    oled.DispChar_font(font.dvsmb_12, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 8, 28)
    oled.show()
    return
#-----------------------------------------------------------------------------------#
def Style3():
    oled.fill(0)
    oled.DispChar_font(SeniorOS.fonts.misans, DLTIME, 5, 10)
    oled.DispChar_font(SeniorOS.fonts.misans_16, (''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])), 5, 35)
    oled.show()
    return
#-----------------------------------------------------------------------------------#