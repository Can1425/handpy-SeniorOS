from SeniorOS.lib.devlib import *
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.pages as Pages
import SeniorOS.system.core as Core
import SeniorOS.system.radient as Radient
# import SeniorOS.lib.mrequests
import gc
import os
import _thread
import SeniorOS.lib.log_manager as LogManager
source = "https://" + Core.Data.Get("text", "radienPluginsSource")
Log = LogManager.Log

def Main():
    global source
    pluginsNum = 0
    gc.enable()
    Core.FullCollect()
    DayLight.App.Style1('线上插件')
    Quit = Core.SharedVar.LoadQuit()
    Quit.value = False
    _thread.start_new_thread(Pages.LoadWait, (Quit, eval("[/Language('请稍等')/]"), False))
    try:
        _response = Radient.Get(source + '/plugins/list.sros')
        pluginsList = (_response.text.split(';'))
        _response = Radient.Get(source + '/plugins/author.sros')
        pluginsTip = (_response.text.split(';'))
        _response = Radient.Get(source + '/plugins/tip.sros')
        pluginsTip2 = (_response.text.split(';'))
        Englist=((Radient.Get(source + '/plugins/list_English.sros')).text).split(';')
        Log.Debug(len(pluginsList))
        Log.Debug(pluginsTip)
    except IndexError as e:
        Core.FullCollect()
        Quit.value = True
        Log.Error(e)
        return
    Quit.value = True
    Core.FullCollect()
    while not button_a.is_pressed():
        pluginsNum = DayLight.Select.Style2(pluginsList, pluginsTip, 18, False, "线上插件")
        if eval("[/GetButtonExpr('th')/]"):
            options = DayLight.ListOptions(['获取并运行', '插件详情', '缓存该插件'], 8, False, "菜单")
            if options == 0:
                DayLight.VastSea.Off()
                DayLight.App.Style1('线上插件')
                DayLight.Text(eval("[/Language('请稍等')/]"), 5, 18, 2)
                # oled.DispChar(eval("[/Language('请稍等')/]"), 5, 18, 1, True)
                DayLight.Text('Tips - 由于适配问题，部分情况下A键无法退出，请尝试软重启解决', 5, 36, 1)
                oled.show()
                _response = Radient.Get((''.join([str(x) for x in [source + '/plugins/main/web_app', pluginsNum + 1, '.sros']])), headers={})
                oled.fill(0)
                exec(_response.text)
                DayLight.VastSea.Off()
            if options == 1:
                DayLight.VastSea.Off()
                while not button_a.is_pressed():
                    DayLight.App.Style1(str(pluginsList[pluginsNum]))
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
                _response = Radient.Get((''.join([str(x) for x in [source + '/plugins/main/web_app', pluginsNum + 1, '.sros']])), headers={})
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

