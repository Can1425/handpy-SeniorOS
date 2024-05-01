from mpython import *
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight

def app_0():
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
                time.sleep_ms(5)
                DayLight.Select(['重连网络', '同步时间', '新建网络配置'],"网络与时间")
                app_0()
            elif settings_num == 1:
                DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
                app_0_time()
            elif settings_num == 2:
                DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
                Core.FullCollect()
            elif settings_num == 3:
                DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
                about()
            elif settings_num == 4:
                DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
                choosewifi()
    DayLight.consani(0, 0, 0, 0, 0, 0, 128, 64)

def app_0_time():
    try:
        oled.fill(0)
        oled.DispChar(str('请稍等...'), 0, 0, 1)
        oled.show()
        ntptime.settime(8, "time.windows.com")
        oled.fill(0)
        oled.DispChar(str('成功'), 0, 0, 1)
        oled.show()
        DayLight.consani(0, 0, 0, 0, 0, 0, 128, 64)
    except:
        DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
        oled.fill(0)
        oled.DispChar(str('失败'), 0, 0, 1)
        oled.show()
        DayLight.consani(0, 0, 0, 0, 0, 0, 128, 64)
        
def app_0_collect():
    try:
        oled.fill(0)
        oled.DispChar(str('请稍等...'), 0, 0, 1)
        oled.show()
        core.FullCollect()
        oled.fill(0)
        oled.DispChar(str('成功'), 0, 0, 1)
        oled.show()
        DayLight.consani(0, 0, 0, 0, 0, 0, 128, 64)
    except:
        DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
        oled.fill(0)
        oled.DispChar(str('失败'), 0, 0, 1)
        oled.show()
        DayLight.consani(0, 0, 0, 0, 0, 0, 128, 64)