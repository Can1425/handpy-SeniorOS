#from SeniorOS.data.lib import *

class System:
    import SeniorOS.system.core as core
    DataOperation=core.DataCtrl("/SeniorOS/data/variable/")

    logo = [0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X3C,0X00,0X00,0X00,0X30, 0X00,0X00,0X00,0X70,0X00,0X78,0X00,0X03,0XFE,0X00,0X00,0X00,0X70,0X00,0X00,0X03, 0XFE,0X03,0XFE,0X00,0X07,0XFC,0X00,0X00,0X00,0X30,0X00,0X00,0X07,0X8F,0X07,0XFE, 0X00,0X06,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X0E,0X03,0X86,0X00,0X00,0X06,0X00, 0X0E,0X03,0XE0,0X20,0X38,0X01,0X8C,0X01,0X8E,0X00,0X00,0X0E,0X00,0X3F,0X87,0XF8, 0X71,0XFE,0X0F,0X98,0X00,0XCE,0X00,0X00,0X0F,0X00,0X7B,0XC7,0XFC,0X71,0XFF,0X1F, 0X98,0X00,0XCE,0X00,0X00,0X07,0XF0,0X60,0XCE,0X0C,0X63,0X83,0X18,0X18,0X00,0XC7, 0XF0,0X00,0X03,0XFC,0XE0,0XCE,0X0C,0X63,0X03,0X38,0X18,0X00,0XC3,0XFC,0X00,0X00, 0X1C,0XFF,0XCE,0X0C,0X63,0X03,0X38,0X18,0X00,0XC0,0X1C,0X00,0X00,0X0C,0XFF,0XCC, 0X0C,0X67,0X03,0X30,0X18,0X00,0XC0,0X0C,0X00,0X00,0X0C,0XC0,0X0C,0X0C,0X67,0X03, 0X30,0X0C,0X01,0XC0,0X0C,0X00,0X00,0X1C,0XC0,0X0C,0X1C,0XE7,0X07,0X30,0X0E,0X03, 0X80,0X1C,0X00,0X00,0X3C,0XE0,0X0C,0X1C,0XE7,0X8E,0X30,0X07,0X8F,0X00,0X3C,0X00, 0X1F,0XF8,0X7F,0X8C,0X1C,0XE3,0XFE,0X30,0X03,0XFE,0X1F,0XF8,0X00,0X1F,0XE0,0X3F, 0X8C,0X18,0XC1,0XF8,0X30,0X00,0XF8,0X1F,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]

    localAppName = ["设置","线上插件","文件","天气","手电筒","即时诗词"]

    homeStyleName = ["起点","边界","新生"]

    homeStyleNum = int(DataOperation.Get('homeStyleNum'))

    barStyleName = ["默认","默认(显示电量)","仅标题","仅标题(居中)"]

    barStyleNum = int(DataOperation.Get('barStyleNum'))

    luminance = int(DataOperation.Get('luminance'))

    lightMode = int(DataOperation.Get('lightMode'))

    VastSeaSpeed = int(DataOperation.Get('VastSeaSpeed'))

    VastSeaSwitch = int(DataOperation.Get('VastSeaSwitch'))

class User:

    wifiName = ["TP-LINK_CD4A","Can1425"]

    wifiPassword = ["13697295123","12345678910"]

    # wifiName 和 wifiPssword (即WIFI名称和密码) 填写时请一一对应

    signature = ""


class LocalApps:

    class App0:

        list = ['网络与时间', '界面与动效', '缓存与运存', '系统与设备']

        tip = ['联网相关设置及信息', '界面动效参数及设置', '应用缓存与设备内存', '系统设备信息及更新']

        list0 = ['重连网络', '同步时间', '新建网络配置']

        list1 = ['日光模式', '动效开关','桌面风格','状态栏风格' '日光引擎信息']

        list2 = ['释放内存', '内存信息']

    poetrySource = "https://v1.jinrishici.com/rensheng.txt"

def Refresh():
    import SeniorOS.system.core as core
    DataOperation=core.DataCtrl("/SeniorOS/data/variable/")
    System.VastSeaSwitch = int(DataOperation.Get('VastSeaSwitch'))
    System.homeStyleNum = int(DataOperation.Get('homeStyleNum'))
    System.luminance = int(DataOperation.Get('luminance'))
    System.lightMode = int(DataOperation.Get('lightMode'))
    System.VastSeaSpeed = int(DataOperation.Get('VastSeaSpeed'))
    System.VastSeaSwitch = int(DataOperation.Get('VastSeaSwitch'))