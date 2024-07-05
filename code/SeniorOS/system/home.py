from mpython import wifi, oled, touchPad_P, touchPad_Y, touchPad_H, touchPad_O, touchPad_N, touchPad_T, button_a, button_b
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import time

import SeniorOS.fonts.quantum
import font.dvsmb_21
import font.dvsmb_12

def HomeStyleSet() -> None:
    """设置桌面风格的函数。"""
    while not button_a.is_pressed():
        oled.fill(0)
        DayLight.UITools()
        time.sleep_ms(5)
        oled.DispChar('桌面风格', 5, 5, 1)
        oled.DispChar('P-默认，Y-经典', 5, 18, 1)
        oled.show()

        if touchPad_P.is_pressed():
            Select(1)
        elif touchPad_Y.is_pressed():
            Select(2)

def Select(styleNum: int) -> None:
    """根据传入的styleNum选择桌面风格，并保存用户选择。"""
    exec("import style" + str(styleNum))  # 动态导入对应的桌面风格模块
    oled.DispChar('桌面风格', 5, 5, 1)
    oled.DispChar('TH-确认', 5, 40, 1)
    oled.show()

    for count in range(100000):
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            Core.Data.Write('home', str(styleNum), False, False)  # 保存用户选择
            return

def Style1() -> None:
    """第一种桌面风格。"""
    oled.fill(0)
    DayLight.DisplayFont(SeniorOS.fonts.quantum, DayLight.UITime(False), DayLight.HomeTimeAutoCenter(DayLight.UITime(False)), 20, False)
    oled.show()

def Style2() -> None:
    """第二种桌面风格。"""
    oled.fill(0)
    DayLight.DisplayFont(font.dvsmb_21, DayLight.UITime(True), 8, 8, False)
    DayLight.DisplayFont(font.dvsmb_12, ''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]]), 8, 28, False)
    oled.show()
