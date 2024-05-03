# DayLight-UI绘制
from mpython import *
import ustruct
import framebuf
import SeniorOS.system.daylight.commonMethod as CommonMethod
import SeniorOS.system.core as Core
import time
import SeniorOS

def Consani(done_x=0, done_y=0, done_wide=0, done_height=0, start_x=0, start_y=0, start_wide=128, start_height=64, logo=None, logo_x=None):
    CommonMethod.AutoInvert()
    for i in range(7):
        oled.fill(0)
        done_x = (done_x - start_x) // 2
        done_y = (done_y - start_y) // 2
        done_wide = (start_wide + done_wide) // 2
        done_height = (start_height + done_height) // 2
        oled.RoundRect(done_x, done_y, done_wide, done_height, 2, 1)
        if not(logo==None):
            logo_x = (logo_x + 52) //2
            oled.Bitmap(logo_x, 20, logo, 25, 25, 1)
        oled.show()

def App_BaseUI(app_title:str):
    oled.fill(0)
    oled.fill_rect(1, 0, 126, 16, 1)
    oled.DispChar(app_title, 5, 0, 2)
    oled.DispChar(CommonMethod.ConvertTime(), 93, 0, 2)
    oled.hline(50, 62, 30, 1)

# 以指定字体[_font]在某处[_x]/[_y]绘制文本[_str]
def DisplayFont(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

def ShowMessage(dispContent:list):
    oled.fill(0)
    oled.rect(1,1,127,60,1)
    for i in range(len(dispContent)):
        oled.DispChar(dispContent[i], 5, 5+16*i, 1)
    # 然而这里实测只能放两排（
    oled.Dispchar("PY-明白", 42, 45)
    oled.show()

def Tti(mode=True):
    """if mode is True then Draw the Left Transition animation
Else Draw the Left Transition animation
time=380ms
"""
    ckt=128
    ckr=0
    if mode:
        for i in range(10):
            ckt=ckt/2
            ckr=ckr + ckt
            oled.fill_rect(0, 0,round(ckr), 64, 0)
            oled.show()
            #time.sleep_ms(10)
    else:
        for i in range(10):
            ckt=ckt/2
            oled.fill_rect(int(ckt), 0, 128, 64, 0)
            oled.show()
            #time.sleep_ms(10)

class Page:
    class WLAN:
        def Config(stage:int):
            if stage==0:
                oled.fill(0)
                oled.Bitmap(16, 20, bytearray([0X07,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X00,0X7C,0X00,0X0F,0XFC,0X00, 0X00,0X00,0X00,0X00,0X00,0X01,0XFE,0X00,0XFE,0X00,0X1F,0XFC,0X00,0X00,0X00,0X00, 0X00,0X00,0X07,0XFF,0X01,0XFF,0X80,0X3C,0X00,0X00,0X00,0X01,0X00,0X00,0X00,0X0F, 0X07,0X83,0X83,0X80,0X38,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X1C,0X01,0XC3,0X81, 0X80,0X30,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X38,0X00,0XE3,0X00,0X00,0X30,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X38,0X00,0XE3,0X80,0X00,0X38,0X00,0X18,0X1F,0XE0, 0X0F,0XFC,0X3E,0X30,0X00,0X63,0XC0,0X00,0X3F,0X00,0X7E,0X1F,0XF1,0X9F,0XFC,0X7E, 0X70,0X00,0X71,0XF0,0X00,0X1F,0XF0,0XE7,0X1C,0X39,0X9C,0X0C,0XE0,0X70,0X00,0X70, 0XFE,0X00,0X07,0XF9,0XC3,0X18,0X19,0X98,0X0C,0XC0,0X70,0X00,0X70,0X1F,0X80,0X00, 0X79,0XC3,0X98,0X19,0X98,0X0C,0XC0,0X30,0X00,0X70,0X03,0X80,0X00,0X39,0XFF,0X98, 0X19,0X88,0X04,0XC0,0X30,0X00,0X60,0X01,0XC0,0X00,0X39,0XFF,0X18,0X19,0X80,0X00, 0XC0,0X38,0X00,0XE0,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X88,0X0C,0XC0,0X1C,0X01, 0XC2,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X8C,0X0C,0XC0,0X1E,0X03,0XC7,0X01,0XC0, 0X71,0XF0,0XC3,0X18,0X19,0X8E,0X0C,0XC0,0X0F,0XDF,0X83,0XC3,0X80,0XFF,0XE0,0X7F, 0X18,0X19,0X87,0XFC,0X40,0X07,0XFF,0X01,0XFF,0X00,0XFF,0XC0,0X3C,0X18,0X19,0X83, 0XFC,0X40,0X01,0XFC,0X00,0X7E,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
            oled.fill_rect(0, 48, 128, 16, 0)
            text=["请稍等...","配置成功","配置失败"]
            oled.DispChar(text[stage], CommonMethod.AutoCenter(text[stage]), 48, 1)
            oled.show()
        def Main(wlanSSIDList):
            oled.fill(0)
            #oled.Bitmap(16, 20, bytearray([0X07,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X00,0X7C,0X00,0X0F,0XFC,0X00, 0X00,0X00,0X00,0X00,0X00,0X01,0XFE,0X00,0XFE,0X00,0X1F,0XFC,0X00,0X00,0X00,0X00, 0X00,0X00,0X07,0XFF,0X01,0XFF,0X80,0X3C,0X00,0X00,0X00,0X01,0X00,0X00,0X00,0X0F, 0X07,0X83,0X83,0X80,0X38,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X1C,0X01,0XC3,0X81, 0X80,0X30,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X38,0X00,0XE3,0X00,0X00,0X30,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X38,0X00,0XE3,0X80,0X00,0X38,0X00,0X18,0X1F,0XE0, 0X0F,0XFC,0X3E,0X30,0X00,0X63,0XC0,0X00,0X3F,0X00,0X7E,0X1F,0XF1,0X9F,0XFC,0X7E, 0X70,0X00,0X71,0XF0,0X00,0X1F,0XF0,0XE7,0X1C,0X39,0X9C,0X0C,0XE0,0X70,0X00,0X70, 0XFE,0X00,0X07,0XF9,0XC3,0X18,0X19,0X98,0X0C,0XC0,0X70,0X00,0X70,0X1F,0X80,0X00, 0X79,0XC3,0X98,0X19,0X98,0X0C,0XC0,0X30,0X00,0X70,0X03,0X80,0X00,0X39,0XFF,0X98, 0X19,0X88,0X04,0XC0,0X30,0X00,0X60,0X01,0XC0,0X00,0X39,0XFF,0X18,0X19,0X80,0X00, 0XC0,0X38,0X00,0XE0,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X88,0X0C,0XC0,0X1C,0X01, 0XC2,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X8C,0X0C,0XC0,0X1E,0X03,0XC7,0X01,0XC0, 0X71,0XF0,0XC3,0X18,0X19,0X8E,0X0C,0XC0,0X0F,0XDF,0X83,0XC3,0X80,0XFF,0XE0,0X7F, 0X18,0X19,0X87,0XFC,0X40,0X07,0XFF,0X01,0XFF,0X00,0XFF,0XC0,0X3C,0X18,0X19,0X83, 0XFC,0X40,0X01,0XFC,0X00,0X7E,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
            for i in range(len(wlanSSIDList)):
                if i<4:oled.DispChar(wlanSSIDList[i],0,i*16)
            #oled.Bitmap(16, 20, bytearray([0X07,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X00,0X7C,0X00,0X0F,0XFC,0X00, 0X00,0X00,0X00,0X00,0X00,0X01,0XFE,0X00,0XFE,0X00,0X1F,0XFC,0X00,0X00,0X00,0X00, 0X00,0X00,0X07,0XFF,0X01,0XFF,0X80,0X3C,0X00,0X00,0X00,0X01,0X00,0X00,0X00,0X0F, 0X07,0X83,0X83,0X80,0X38,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X1C,0X01,0XC3,0X81, 0X80,0X30,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X38,0X00,0XE3,0X00,0X00,0X30,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X38,0X00,0XE3,0X80,0X00,0X38,0X00,0X18,0X1F,0XE0, 0X0F,0XFC,0X3E,0X30,0X00,0X63,0XC0,0X00,0X3F,0X00,0X7E,0X1F,0XF1,0X9F,0XFC,0X7E, 0X70,0X00,0X71,0XF0,0X00,0X1F,0XF0,0XE7,0X1C,0X39,0X9C,0X0C,0XE0,0X70,0X00,0X70, 0XFE,0X00,0X07,0XF9,0XC3,0X18,0X19,0X98,0X0C,0XC0,0X70,0X00,0X70,0X1F,0X80,0X00, 0X79,0XC3,0X98,0X19,0X98,0X0C,0XC0,0X30,0X00,0X70,0X03,0X80,0X00,0X39,0XFF,0X98, 0X19,0X88,0X04,0XC0,0X30,0X00,0X60,0X01,0XC0,0X00,0X39,0XFF,0X18,0X19,0X80,0X00, 0XC0,0X38,0X00,0XE0,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X88,0X0C,0XC0,0X1C,0X01, 0XC2,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X8C,0X0C,0XC0,0X1E,0X03,0XC7,0X01,0XC0, 0X71,0XF0,0XC3,0X18,0X19,0X8E,0X0C,0XC0,0X0F,0XDF,0X83,0XC3,0X80,0XFF,0XE0,0X7F, 0X18,0X19,0X87,0XFC,0X40,0X07,0XFF,0X01,0XFF,0X00,0XFF,0XC0,0X3C,0X18,0X19,0X83, 0XFC,0X40,0X01,0XFC,0X00,0X7E,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
            oled.DispChar("请选择 WiFi 配置", CommonMethod.AutoCenter("请选择 WiFi 配置"), 48, 1)
            oled.show()
    class Desktop:
        class CloudMessage:
            def Loading():
                time.sleep(0.2)
                Consani()
                App_BaseUI('云端通知')
                oled.DispChar('正在从云端获取', 5, 18, 2)
                oled.show()
            def Error(errorObj):
                if type(errorObj)==int: # 对错误类型进行判断 
                    # errorObj类型为int 代表传入的是HTTP状态码
                    oled.DispChar('ERR HTTP CODE '+str(errorObj), 5, 18, 2)
                    oled.show()
                    return
                else:
                    # 反之 则传入的是try/except捕获的错误对象
                    oled.DispChar('连接超时' if errorObj.args[0]==113 else "发生了未知错误", 5, 18, 2)
                    oled.DispChar("OSError "+errorObj.args[0] if errorObj.args[0]==113 else str(errorObj), 5, 34, 2)
                    oled.show()
                    return
            def Show(messages):
                App_BaseUI('云端通知')
                oled.DispChar(messages[1], 5, 18)
                oled.DispChar(messages[2], 5, 32)
                oled.DispChar(messages[3], 5, 45)
                oled.show()
        class Home:
            def ShowTime():
                oled.fill(0)
                DisplayFont(SeniorOS.fonts.quantum, CommonMethod.UITime()[:2] , 30, 18, False)
                DisplayFont(SeniorOS.fonts.quantum, CommonMethod.UITime()[-2:], 64, 18, False)
                oled.hline(50, 62, 30, 1)
                oled.show()
            def ExitConfirm():
                App_BaseUI('退出确认')
                oled.DispChar("你同时按下了AB",5,18)
                oled.DispChar("将回到启动选择器",5,32)
                oled.DispChar("同时按下PN确认",0,45)
                oled.show()
    class About:
        def SeniorOS():
            oled.fill(0)
            oled.Bitmap(16, 20, bytearray([0X07,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X00,0X7C,0X00,0X0F,0XFC,0X00, 0X00,0X00,0X00,0X00,0X00,0X01,0XFE,0X00,0XFE,0X00,0X1F,0XFC,0X00,0X00,0X00,0X00, 0X00,0X00,0X07,0XFF,0X01,0XFF,0X80,0X3C,0X00,0X00,0X00,0X01,0X00,0X00,0X00,0X0F, 0X07,0X83,0X83,0X80,0X38,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X1C,0X01,0XC3,0X81, 0X80,0X30,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X38,0X00,0XE3,0X00,0X00,0X30,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X38,0X00,0XE3,0X80,0X00,0X38,0X00,0X18,0X1F,0XE0, 0X0F,0XFC,0X3E,0X30,0X00,0X63,0XC0,0X00,0X3F,0X00,0X7E,0X1F,0XF1,0X9F,0XFC,0X7E, 0X70,0X00,0X71,0XF0,0X00,0X1F,0XF0,0XE7,0X1C,0X39,0X9C,0X0C,0XE0,0X70,0X00,0X70, 0XFE,0X00,0X07,0XF9,0XC3,0X18,0X19,0X98,0X0C,0XC0,0X70,0X00,0X70,0X1F,0X80,0X00, 0X79,0XC3,0X98,0X19,0X98,0X0C,0XC0,0X30,0X00,0X70,0X03,0X80,0X00,0X39,0XFF,0X98, 0X19,0X88,0X04,0XC0,0X30,0X00,0X60,0X01,0XC0,0X00,0X39,0XFF,0X18,0X19,0X80,0X00, 0XC0,0X38,0X00,0XE0,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X88,0X0C,0XC0,0X1C,0X01, 0XC2,0X01,0XC0,0X00,0X39,0X80,0X18,0X19,0X8C,0X0C,0XC0,0X1E,0X03,0XC7,0X01,0XC0, 0X71,0XF0,0XC3,0X18,0X19,0X8E,0X0C,0XC0,0X0F,0XDF,0X83,0XC3,0X80,0XFF,0XE0,0X7F, 0X18,0X19,0X87,0XFC,0X40,0X07,0XFF,0X01,0XFF,0X00,0XFF,0XC0,0X3C,0X18,0X19,0X83, 0XFC,0X40,0X01,0XFC,0X00,0X7E,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 64, 18, 1)
            oled.DispChar("SeniorOS-by Can1425",5,45)
            oled.show()
        def Daylight():
            oled.fill(0)
            oled.DispChar('关于日光引擎', 5, 5, 1)
            oled.DispChar("这是一个 GUI 框架，", 5, 20, 1)
            oled.DispChar("负责SeniorOS的UI渲染/逻辑处理", 5,35 , 1)
            oled.DispChar("鸣谢POLA的巨大贡献", 5, 50, 1)
            oled.show()
    