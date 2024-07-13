import SeniorOS.system.core as Core


class System:

    localAppName = ["设置","线上插件","文件","天气","手电筒","即时诗词"]

    homeStyle = int(Core.DataVariable.Get('home'))

    luminance = int(Core.DataVariable.Get('luminance'))

    lightMode = int(Core.DataVariable.Get('lightmode'))

    VastSeaSpeed = int(Core.DataVariable.Get('VastSea_speed'))

    VastSeaSwitch = int(Core.DataVariable.Get('VastSea_switch'))

class User:

    wifiName = ["WIFI 1 Name","WIFI 2 Name"]

    wifiPassword = ["WIFI 1 Password","WIFI 2 Password"]

    # wifiName 和 wifiPssword (即WIFI名称和密码) 填写时请一一对应

    signature = ""


class LocalApps:

    poetrySource = "https://v1.jinrishici.com/rensheng.txt"