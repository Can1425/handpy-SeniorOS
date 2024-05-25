from mpython import *
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import machine
import esp32
from SeniorOS.apps.app_4 import Poetry

def app_0():
    DayLight.UITools()
    from SeniorOS.system.pages import about,wifi_page,choosewifi
    time.sleep_ms(5)
    settings_list = ['网络与时间', '界面与动效', '缓存与运存', '系统与设备']
    settings_tip = ['联网相关设置及信息', '界面动效参数及设置', '应用缓存与设备内存', '系统设备信息及更新']
    settings_num = 0
    while not button_a.is_pressed():
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            settings_num = settings_num + 1
            if settings_num + 1 > len(settings_list):
                settings_num = len(settings_list) - 1
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            settings_num = settings_num - 1
            if settings_num < 0:
                settings_num = 0
        DayLight.app("Setting")
        oled.DispChar(str(settings_tip[settings_num]), 5, 18, 1, True)
        oled.DispChar(str(settings_list[settings_num]), 5, 45, 1)
        oled.DispChar(''.join([str(settings_num + 1),'/',str(len(settings_list))]), 105, 45, 1)
        oled.show()
        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
            if settings_num == 0:
                DayLight.ConsaniSideslip(True)
                settings0Num = DayLight.Select(['重连网络', '同步时间', '新建网络配置'],"选择")
                DayLight.ConsaniSideslip(False)
                if settings0Num == 0:
                    DayLight.ConsaniSideslip(True)
                    wifi_page()
                    DayLight.ConsaniSideslip(False)
                elif settings0Num == 1:
                    DayLight.ConsaniSideslip(True)
                    App0Time()
                    DayLight.ConsaniSideslip(False)
                elif settings0Num == 2:
                    DayLight.ConsaniSideslip(True)
                    choosewifi()
                    DayLight.ConsaniSideslip(False)
            elif settings_num == 1:
                DayLight.ConsaniSideslip(True)
                settings1Num = DayLight.Select(['日光模式', '动效开关', '日光引擎信息'],"选择")
                DayLight.ConsaniSideslip(False)
                if settings1Num == 0:
                    DayLight.ConsaniSideslip(True)
                    App0DayLightMode()
                    DayLight.ConsaniSideslip(False)
                elif settings1Num == 1:
                    DayLight.ConsaniSideslip(True)
                    DayLight.ConsaniSideslip(False)
                elif settings1Num == 2:
                    DayLight.ConsaniSideslip(True)
                    DayLight.About()
                    DayLight.ConsaniSideslip(False)
            elif settings_num == 2:
                DayLight.ConsaniSideslip(True)
                settings3Num = DayLight.Select(['释放内存', '内存信息'],"选择")
                DayLight.ConsaniSideslip(False)
                if settings3Num == 0:
                    DayLight.ConsaniSideslip(True)
                    App0Collect()
                    DayLight.ConsaniSideslip(False)
                elif settings0Num == 1:
                    DayLight.ConsaniSideslip(True)
                    DayLight.ConsaniSideslip(False)
            elif settings_num == 3:
                DayLight.ConsaniSideslip(True)
                about()
                DayLight.ConsaniSideslip(False)
            elif settings_num == 4:
                pass

def App0Time():
    DayLight.UITools()
    try:
        oled.fill(0)
        oled.DispChar(str('请稍等'), 5, 5, 1)
        time.sleep_ms(5)
        oled.DispChar(str('尝试进行时间同步'), 5, 18, 1)
        oled.show()
        ntptime.settime(8, "time.windows.com")
        oled.DispChar(str('成功'), 5, 45, 1)
        time.sleep_ms(5)
        oled.show()
        return True
    except:
        oled.DispChar(str('失败'), 5, 45, 1)
        oled.show()
        
def App0Collect():
    oled.fill(0)
    DayLight.UITools()
    try:
        oled.DispChar(str('请稍等'), 5, 5, 1)
        time.sleep_ms(5)
        oled.DispChar(str('尝试进行清理'), 5, 18, 1)
        oled.show()
        Core.FullCollect()
        oled.DispChar(str('成功'), 5, 45, 1)
        time.sleep_ms(5)
        oled.show()
        return True
    except:
        oled.DispChar(str('失败'), 5, 45, 1)
        oled.show()

def App0DayLightMode():
    while not button_a.is_pressed():
        oled.fill(0)
        DayLight.UITools()
        oled.DispChar(str('日光模式'), 5, 5, 1)
        time.sleep_ms(5)
        if Core.Data.Get('light') == "1":
            get = '开启'
        else:
            get = '关闭'
        oled.DispChar(get, 5, 18, 1)
        oled.show()
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            Core.Data.Write('light','1',False,False)
            oled.invert(1)
            oled.show()
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            Core.Data.Write('light','0',False,False)
            oled.invert(0)
            oled.show()
    return

def App0Light():
    b = int(Core.Data.Get('luminance'))
    oled.contrast(b)
    DayLight.UITools()
    while not button_a.is_pressed():
        oled.contrast(b)
        oled.fill(0)
        oled.DispChar(str('亮度调节'), 5, 5, 1)
        time.sleep_ms(5)
        oled.DispChar("当前亮度"+ str(b), 5, 18, 1)
        oled.show()
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            b = b + 5
            if b > 255:
                b = 255
            oled.contrast(b)
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            b = b - 5
            if b < 0:
                b = 0
            oled.contrast(b)
    oled.contrast(b)
    Core.Data.Write('luminance',str(b),False,False)
    return

def App0PowerOptions():
    options = DayLight.ListOptions(['软重启', '关闭显示器', '休眠'])
    if options == 0:
        DayLight.ConsaniSideslip(True)
        exec(machine.reset())
        DayLight.ConsaniSideslip(False)
    elif options == 1:
        DayLight.ConsaniSideslip(True)
        oled.poweroff()
        if button_b.is_pressed():
            oled.poweron()
        return
        DayLight.ConsaniSideslip(False)
    elif options == 2:
        DayLight.ConsaniSideslip(True)
        esp32.wake_on_touch(True)
        oled.fill(0)
        oled.DispChar('休眠状态已启动', 5, 0, 1)
        oled.contrast(0)
        oled.invert(0)
        Poetry()
        try:
            oled.DispChar(poetry[0], 5, 18, 1)
            oled.DispChar(poetry[1], 5, 34, 1)
            oled.DispChar('轻触任意触摸键退出', 5, 50, 1)
        except:
            try:
                oled.DispChar(poetry[0], 5, 18, 1)
                oled.DispChar('轻触任意触摸键退出', 5, 50, 1)
            except:
                pass
        oled.show()
        machine.lightsleep()
        DayLight.UITools()
        DayLight.ConsaniSideslip(False)
