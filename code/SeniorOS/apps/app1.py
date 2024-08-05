from SeniorOS.system.devlib import *
import SeniorOS.system.app_manager as ImportAppManager
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import urequests
import gc

AppManager = ImportAppManager.AppManager
manager = AppManager('线上插件')

@manager.regScreen('main')
@manager.setAppEntryPoint()
def main():
    pluginsNum = 0
    gc.enable()
    Core.FullCollect()
    DayLight.App.Style1('线上插件')
    oled.DispChar('正在尝试获取插件信息', 5, 18, 1, True)
    oled.show()
    _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/list.fos', headers={})
    pluginsList = (_response.text.split(';'))
    _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/tip.fos', headers={})
    pluginsTip = (_response.text.split(';'))
    _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/web-app/tip.fos', headers={})
    pluginsTip2 = (_response.text.split(';'))
    print(len(pluginsList))
    print(pluginsTip)
    Core.FullCollect()
    while not button_a.is_pressed():
        settingsNum = DayLight.Select.Style2(pluginsList, pluginsTip, 18, False, "线上插件")
        if eval("[/GetButtonExpr('th')/]"):
            options = DayLight.ListOptions(['获取并运行', '插件详情', '缓存该插件'], 8, True, "None")
            if options == 0:
                DayLight.VastSea.Off()
                DayLight.app('线上插件')
                oled.DispChar('请稍等，正在获取源码', 5, 18, 1, True)
                oled.DispChar('如A键无法退出，重启', 5, 45, 1, True)
                oled.show()
                _response = urequests.get((''.join([str(x) for x in ['https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/web-app/', pluginsNum + 1, '.fos']])), headers={})
                oled.fill(0)
                exec(_response.text)
                DayLight.VastSea.Off()
            if options == 1:
                DayLight.VastSea.Off()
                while not button_a.is_pressed():
                    DayLight.app(str(pluginsList[pluginsNum]))
                    oled.DispChar(str(pluginsTip2[pluginsNum]), 5, 18, 1, True)
                    oled.show()
                DayLight.VastSea.Off()

manager.Run()