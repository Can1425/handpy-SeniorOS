from mpython import *
import SeniorOS.system.core as Core

def UITime(pages=True):
    h=str(Core.GetTime.Hour())
    m=str(Core.GetTime.Min())
    return ('0' + h if len(h)==1 else h) + \
             (':' if pages else "") + \
            ('0' + m if len(m)==1 else m)

def GetCharWidth(s):
    strWidth = 0
    for c in s:
        charData = oled.f.GetCharacterData(c)
        if charData is None:continue
        strWidth += ustruct.unpack('HH', charData[:4])[0] + 1
    return strWidth

AutoCenter=lambda string:64-GetCharWidth(string)//2