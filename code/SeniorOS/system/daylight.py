import SeniorOS.system.core as Core
import SeniorOS.apps.logo as Logo
import ntptime
import network
import time
import ustruct
import framebuf
from mpython import wifi, oled, touchPad_P, touchPad_Y, touchPad_H, touchPad_O, touchPad_N, touchPad_T, button_a, button_b
import gc
import uos
import math
import urequests

# 添加类型注释和优化代码结构

def UITime(pages: bool = True) -> str:
    """返回当前时间的字符串表示形式，格式为HH:MM。"""
    h: str = str(Core.GetTime.Hour())
    m: str = str(Core.GetTime.Min())
    return ('0' + h if len(h) == 1 else h) + (':' if pages else '') + ('0' + m if len(m) == 1 else m)

def Consani(
    consani_done_x: int, consani_done_y: int, consani_done_wide: int, consani_done_height: int,
    consani_start_x: int, consani_start_y: int, consani_start_wide: int, consani_start_height: int
) -> None:
    """
    执行动画效果。

    Args:
    consani_done_x: 完成位置的x坐标。
    consani_done_y: 完成位置的y坐标。
    consani_done_wide: 完成位置的宽度。
    consani_done_height: 完成位置的高度。
    consani_start_x: 开始位置的x坐标。
    consani_start_y: 开始位置的y坐标。
    consani_start_wide: 开始位置的宽度。
    consani_start_height: 开始位置的高度。
    """
    UITools()
    consani_done_wait: int = 3
    if int(Core.Data.Get('VastSea_switch')) == 1:
        try:
            oled.fill(0)
            for _ in range(7):
                oled.RoundRect(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, 2, 1)
                oled.fill(0)
                consani_done_x = (consani_done_x - consani_start_x) // 2
                consani_done_y = (consani_done_y - consani_start_y) // 2
                consani_done_wide = (consani_start_wide + consani_done_wide) // 2
                consani_done_height = (consani_start_height + consani_done_height) // 2
                oled.RoundRect(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, 2, 1)
                oled.show()
        except Exception as e:
            # 显示错误消息并等待一段时间
            oled.DispChar(' :( 我们遇到了一些问题，将在 3 秒后返回', 5, 25, 1, True)
            oled.show()
            return
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            return
        time.sleep_ms(consani_done_wait)
        consani_done_wait += 3
    else:
        VastSea.Off()

def ConsaniSideslip(side: bool) -> None:
    """
    执行侧滑动作。

    Args:
    side: 是否为侧滑动作，True表示右侧，False表示左侧。
    """
    if int(Core.Data.Get('VastSea_switch')) == 1:
        t: int = 10
        if side:
            x: int = 128
            for count in range(3):
                oled.fill(0)
                oled.RoundRect(x, (-1), 130, 66, 2, 1)
                oled.show()
                x = int((x - 3 * math.sqrt(t)))
                time.sleep_ms(t)
            for count in range(7):
                oled.fill(0)
                oled.RoundRect(x, (-1), 130, 66, 2, 1)
                oled.show()
                x //= 2
                t += 3
                time.sleep_ms(t)
        else:
            x: int = 0
            for count in range(3):
                oled.fill(0)
                oled.RoundRect(x, (-1), 130, 66, 2, 1)
                oled.show()
                x = int((x + 3 * math.sqrt(t)))
                t += -3
                time.sleep_ms(t)
            for count in range(7):
                oled.fill(0)
                oled.RoundRect(x, (-1), 130, 66, 2, 1)
                oled.show()
                x += (128 - x) // 2
                time.sleep_ms(t)
    else:
        VastSea.Off()

def GetCharWidth(s: str) -> int:
    """
    返回给定字符串的宽度。

    Args:
    s: 输入的字符串。

    Returns:
    int: 字符串的宽度。
    """
    strWidth: int = 0
    for c in s:
        charData = oled.f.GetCharacterData(c)
        if charData is not None:
            strWidth += ustruct.unpack('HH', charData[:4])[0] + 1
    return strWidth

AutoCenter = lambda string: 64 - GetCharWidth(string) // 2
HomeTimeAutoCenter = lambda string: 64 - GetCharWidth(string) // 2 - 22

def app(appTitle: str) -> None:
    """显示应用程序标题和当前时间。"""
    oled.fill(0)
    UITools()
    oled.DispChar(appTitle, 5, 0, 1)
    oled.DispChar(UITime(True), 93, 0, 1)

def DisplayFont(_font, _str, _x, _y, _wrap, _z=0) -> None:
    """
    显示字体内容。

    Args:
    _font: 字体数据。
    _str: 要显示的字符串。
    _x: x坐标。
    _y: y坐标。
    _wrap: 是否自动换行。
    _z: 额外参数，具体作用未明。
    """
    _start: int = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]:
            _x = _start
            _y += _d[1]
        if _c == '1' and _z > 0:
            oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1], framebuf.MONO_HLSB), (_x + int(_d[2] / _z)) if _c == '1' and _z > 0 else _x, _y)
        _x += _d[2]

def Select(dispContent:list, y:int, window:False, appTitle:str):
    UITools()
    selectNum = 0

    if appTitle == "None":
        pass
    else:
        if window == False:
            app(appTitle)
        else:
            oled.DispChar(appTitle, 5, 5, 1)
            oled.DispChar(UITime(True), 93, 5, 1)
    oled.show()
    while not button_a.is_pressed():
        oled.fill_rect(0, 20, 128, 45, 0)
        oled.DispChar(dispContent[selectNum], AutoCenter(dispContent[selectNum]), y, 1)
        oled.DispChar(''.join([str(selectNum + 1),'/',str(len(dispContent))]), 105, 40, 1)
        if window == True:
            oled.RoundRect(2, y - 26, 124, 55, 2, 1)
        else:
            pass
        oled.show()
        if touchPad_O.is_pressed() and touchPad_N.is_pressed():
            selectNum = selectNum + 1
            if selectNum + 1 > len(dispContent):
                selectNum = len(dispContent) - 1
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            selectNum = selectNum - 1
            if selectNum < 0:
                selectNum = 0
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            return selectNum
        time.sleep_ms(300)
    time.sleep_ms(300)
    return

def ListOptions(dispContent: list, y: int, window: bool, appTitle: str) -> int:
    """显示列表选项，并返回用户选择的索引。"""
    UITools()
    listNum: int = 0
    oled.fill(0)
    if appTitle != "None":
        app(appTitle)
    oled.show()
    while not button_a.is_pressed():
        oled.fill_rect(0, 20, 128, 45, 0)
        oled.DispChar(''.join([str(listNum + 1), '/', str(len(dispContent))]), 105, 40, 1)
        try:
            oled.DispChar(str(dispContent[listNum]), 5, y, 2)
            oled.DispChar(str(dispContent[listNum + 1]), 5, y + 15, 1)
            oled.DispChar(str(dispContent[listNum + 2]), 5, y + 30, 1)
        except:
            try:
                oled.DispChar(str(dispContent[listNum]), 5, y, 2)
                oled.DispChar(str(dispContent[listNum + 1]), 5, y + 15, 1)
            except:
                oled.DispChar(str(dispContent[listNum]), 5, y, 2)
        if window:
            oled.RoundRect(2, y - 6, 124, 55, 2, 1)
        oled.show()
        if touchPad_O.is_pressed() and touchPad_N.is_pressed():
            listNum += 1
            if listNum + 1 > len(dispContent):
                listNum = len(dispContent) - 1
        if touchPad_P.is_pressed() and touchPad_Y.is_pressed():
            listNum -= 1
            if listNum < 0:
                listNum = 0
        if touchPad_T.is_pressed() and touchPad_H.is_pressed():
            return listNum

def message(content: str) -> None:
    """显示消息，并等待用户按下按钮。"""
    content += "   按A键确认   "
    while not button_a.is_pressed:
        oled.fill(0)
        oled.fill_rect(1, 0, 126, 16, 1)
        oled.DispChar(content, 0, 0, 2)
        oled.show()
        time.sleep(0.2)
        content = content[1:] + content[0]

class VastSea:
    speed: int = int(Core.Data.Get('VastSea_speed'))  # 3, 6, 12

    @staticmethod
    def Off() -> None:
        oled.fill(0)
        oled.show()
        time.sleep_ms(VastSea.speed * 90)

    class SeniorMove:
        @staticmethod
        def Line(nowX1: int, nowY1: int, nowX2: int, nowY2: int, newX1: int, newY1: int, newX2: int, newY2: int) -> None:
            """绘制线条并执行移动操作。"""
            oled.line(nowX1, nowY1, nowX2, nowY2, 1)
            oled.show()
            if int(Core.Data.Get('VastSea_switch')) == 1:
                for count in range(3):
                    nowX1 += (newX1 - nowX1) // VastSea.speed
                    nowY1 -= (nowY1 - newY1) // VastSea.speed + (newY1 - newY1 // 2)
                    nowX2 += (newX2 - nowX2) // VastSea.speed
                    nowY2 -= (nowY2 - newY2) // VastSea.speed + (newY2 - newY2 // 2)
                    oled.fill(0)
                    oled.line(nowX1, nowY1, nowX2, nowY2, 1)
                    oled.show()
            else:
                VastSea.Off()
            oled.fill(0)
            time.sleep_ms(300)

        @staticmethod
        def Text(text, nowX: int, nowY: int, newX: int, newY: int) -> None:
            """显示文本并执行移动操作。"""
            if int(Core.Data.Get('VastSea_switch')) == 1:
                oled.DispChar(str(text), nowX, nowY)
                oled.show()
                for count in range(VastSea.speed):
                    nowX += (newX - nowX) // VastSea.speed
                    nowY -= (nowY - newY) // VastSea.speed + (newY - newY // 2)
                    oled.fill(0)
                    oled.DispChar(str(text), nowX, nowY)
                    oled.show()
            else:
                VastSea.Off()
            oled.fill(0)
            time.sleep_ms(300)

def UITools() -> None:
    """根据设置调整屏幕的亮度和对比度。"""
    try:
        oled.invert(int(Core.Data.Get('light')))
        oled.contrast(int(Core.Data.Get('luminance')))
    except Exception as e:
        pass

def About() -> None:
    """显示关于信息，并等待用户按下按钮。"""
    while not button_a.is_pressed():
        oled.fill(0)
        UITools()
        oled.DispChar(str('关于日光引擎'), 5, 5, 1)
        oled.DispChar("这是一个 GUI 框架，", 5, 20, 1)
        oled.DispChar("负责渲染部分特有 GUI", 5, 35, 1)
        oled.DispChar("鸣谢POLA在的巨大贡献", 5, 50, 1)
        oled.show()
    return
