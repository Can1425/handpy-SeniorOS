from SeniorOS.system.devlib import *
import SeniorOS.system.pages_manager as PagesManager
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import urequests
import gc
import os
source = Core.Data.Get("text", "radienPluginsSource")

Manager = PagesManager.main('apps/app1.mpy')

@Manager.regScreen('AppMain')
@Manager.setAppEntryPoint()


def Main():
    global source
    pluginsNum = 0
    gc.enable()
    Core.FullCollect()
    DayLight.App.Style1('线上插件')
    oled.DispChar('请稍等', 5, 18, 1, True)
    oled.show()
    _response = urequests.get(source + '/raw/plugins/list.fos', headers={})
    pluginsList = (_response.text.split(';'))
    _response = urequests.get(source + '/raw/plugins/app/tip.sros', headers={})
    pluginsTip = (_response.text.split(';'))
    _response = urequests.get(source + '/raw/plugins/app/tip.sros', headers={})
    pluginsTip2 = (_response.text.split(';'))
    Englist=((urequests.get(source + '/raw/plugins/list_English.sros',headers={})).text).split(';')
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
                DayLight.Text(eval("[/Language('请稍等')/]"), 5, 18, 2)
                # oled.DispChar(eval("[/Language('请稍等')/]"), 5, 18, 1, True)
                DayLight.Text('Tips - 由于适配问题，部分情况下A键无法退出，请尝试软重启解决', 5, 36, 2)
                oled.show()
                _response = urequests.get((''.join([str(x) for x in [source + '/raw/plugins/app/web_app', pluginsNum + 1, '.sros']])), headers={})
                oled.fill(0)
                exec(_response.text)
                DayLight.VastSea.Off()
            if options == 1:
                DayLight.VastSea.Off()
                while not button_a.is_pressed():
                    DayLight.app(str(pluginsList[pluginsNum]))
                    DayLight.Text(str(pluginsTip2[pluginsNum]), 5, 18, 2)
                    # oled.DispChar(str(pluginsTip2[pluginsNum]), 5, 18, 1, True)
                    oled.show()
            if options == 2:
                DayLight.VastSea.Off()
                DayLight.app('线上插件')
                DayLight.Text(eval("[/Language('请稍等')/]"), 5, 18, 2)
                # oled.DispChar(eval("[/Language('请稍等')/]"), 5, 18, 1, True)
                DayLight.Text(eval("[/Language('正在进行操作')/]"), 5, 36, 2)
                oled.show()
                _response = urequests.get((''.join([str(x) for x in [source + '/raw/plugins/app/web_app', pluginsNum + 1, '.sros']])), headers={})
                try:
                    os.chdir("/SeniorOS/downloads")
                except:
                    os.mkdir("/SeniorOS/downloads")
                    os.chdir("/SeniorOS/downloads")
                with open(f"{Englist[pluginsNum+1]}.py","w") as file:
                    file.write(_response)
                os.chdir("/")
                oled.fill(0)
                DayLight.VastSea.Off()
                DayLight.VastSea.Off()

