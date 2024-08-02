from mpython import *
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import machine
import esp32

list = ['网络与时间', '界面与动效', '缓存与运存', '系统与设备']
tip = ['联网相关设置及信息', '界面动效参数及设置', '应用缓存与设备内存', '系统设备信息及更新']
DayLight.UITools()
import SeniorOS.system.pages as Pages
import SeniorOS.style.port as Style
time.sleep_ms(5)

Settings0 = {
    0: Pages.WifiPages,
    1: Pages.Time,
    2: Pages.Choosewifi
}

Settings1 = {
    0: DayLight.LightModeSet,
    1:DayLight.LuminanceSet,
    2: DayLight.VastSea.Switch,
    3: Style.homeStyleSet,
    4: Style.barStyleSet,
    5: DayLight.About,
}

Settings2 = {
    0: Pages.Collect,
    1: Pages.Collect,
}

Settings3 = {
    0: Pages.About,
    1: Pages.About,
}


while not button_a.value()==0:
    settingsNum = DayLight.Select.Style2(list, tip, 18, False, "设置")
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        options = eval('DayLight.Select.Style1(list{}, 28, True, "选择")'.format(settingsNum),
                        {'list0':['重连网络', '同步时间', '新建网络配置'],
                        'list1':['日光模式','亮度调节','动效开关','桌面风格','状态栏风格' '日光引擎信息'],
                        'list2':['释放内存', '内存信息'],
                        'DayLight':DayLight}
                    )
        if settingsNum == 0:
            DayLight.VastSea.Progressive(True)
            if options == None:
                pass
            else:
                Settings0.get(options)()
            DayLight.VastSea.Progressive(True)
        elif settingsNum == 1:
            DayLight.VastSea.Progressive(True)
            if options == None:
                pass
            else:
                Settings1.get(options)()
            DayLight.VastSea.Progressive(True)
        elif settingsNum == 2:
            DayLight.VastSea.Progressive(True)
            if options == None:
                pass
            else:
                Settings2.get(options)()
            DayLight.VastSea.Progressive(True)
        elif settingsNum == 3:
            DayLight.VastSea.Progressive(True)
            if options == None:
                pass
            else:
                Settings3.get(options)()
            DayLight.VastSea.Progressive(True)
        else:
            pass