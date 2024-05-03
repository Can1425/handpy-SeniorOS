# Daylight-常用UI操作方法汇总
# 主要放一些处在 交互/绘制 中间层的东西
# 或者交互与UI难舍难分的内容

import SeniorOS.system.core as Core
from SeniorOS.system.daylight.draw import App_BaseUI
from mpython import *
import time
#命名中的Auto是基于配置文件的自动翻转像素 

def AutoInvert():
    try:
        oled.invert(int(Core.Data.Get('light')))
    except:
        pass

def GetCharWidth(s):
    strWidth = 0
    for c in s:
        charData = oled.f.GetCharacterData(c)
        if charData is None:continue
        strWidth += ustruct.unpack('HH', charData[:4])[0] + 1
    return strWidth
AutoCenter=lambda string:64-GetCharWidth(string)//2

def UITime(connectChar=":",
        firstData=str(Core.GetTime.Hour()),
        secondData=str(Core.GetTime.Min())):
    return ('0' + firstData if len(h)==1 else firstData) + \
            connectChar + \
            ('0' + secondData if len(m)==1 else secondData)

def Select(dispContent:list,appTitle:str):
    selectNum = 0
    while True:
        oled.fill(0)
        App_BaseUI(appTitle)
        oled.rect(2, 4, 124, 16, 1)
        oled.RoundRect(2, 2, 124, 55, 2, 1)
        oled.DispChar(dispContent[selectNum], AutoCenter(dispContent[selectNum]), 20, 1)
        oled.DispChar( ''.join([str(selectNum + 1),'/',str(len(dispContent))]) , 105, 40, 1)
        oled.DispChar('TH-确认', 5, 40, 1)
        oled.show()
        while not eval("[/GetButtonExpr('apython')/]"):pass
        if touchPad_O.is_pressed() and touchPad_N.is_pressed():
            selectNum = selectNum + 1
            if selectNum + 1 > len(dispContent):
                selectNum = len(dispContent) - 1
        elif touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            selectNum = selectNum - 1
            if selectNum < 0:
                selectNum = 0
        elif touchPad_T.is_pressed() and touchPad_H.is_pressed():
            return selectNum
        elif button_a.is_pressed():
            time.sleep_ms(5)
            return