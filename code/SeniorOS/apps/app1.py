from mpython import *
import SeniorOS.system.daylight as DayLight
import urequests
import gc

pluginsNum = 0
while not eval("[/GetButtonExpr('a')/]"):
    gc.enable()
    gc.collect()
    DayLight.app('线上插件')
    oled.DispChar(str('正在尝试获取插件信息'), 5, 18, 1, True)
    oled.show()
    _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/list.fos', headers={})
    pluginsList = (_response.text.split(';'))
    _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/tip.fos', headers={})
    pluginsTip = (_response.text.split(';'))
    _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/web-app/tip.fos', headers={})
    pluginsTip2 = (_response.text.split(';'))
    print(len(pluginsList))
    print(pluginsTip)
    gc.collect()
    break
while not eval("[/GetButtonExpr('a')/]"):
    settingsNum = DayLight.Select.Style2(pluginsList, pluginsTip, 18, False, "线上插件")
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        options = DayLight.ListOptions(['获取并运行', '插件详情', '缓存该插件'], 8, True, "None")
        if options == 0:
            DayLight.VastSea.Off()
            DayLight.app('线上插件')
            oled.DispChar(str('请稍等，正在获取源码'), 5, 18, 1, True)
            oled.DispChar(str('如A键无法退出，重启'), 5, 45, 1, True)
            oled.show()
            _response = urequests.get((''.join([str(x) for x in ['https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/web-app/', plugins_num + 1, '.fos']])), headers={})
            oled.fill(0)
            exec(_response.text)
            DayLight.VastSea.Off()
        if options == 1:
            DayLight.VastSea.Off()
            while not eval("[/GetButtonExpr('a')/]"):
                DayLight.app(str(pluginsList[pluginsNum]))
                oled.DispChar(str(pluginsTip2[pluginsNum]), 5, 18, 1, True)
                oled.show()
            DayLight.VastSea.Off()