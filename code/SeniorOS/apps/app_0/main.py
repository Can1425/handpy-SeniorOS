from mpython import *
import SeniorOS.system.core as syscore
import SeniorOS.system.daylight as DayLight
import SeniorOS.apps.app_0.core as core
import SeniorOS.system.pages as pages

time.sleep_ms(5)
settings_list = ['重连网络', '同步时间', '清理内存', '系统信息','新增wifi连接']
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
    oled.DispChar(str('暂无简介'), 5, 18, 1, True)
    oled.DispChar(str(settings_list[settings_num]), 5, 45, 1)
    oled.DispChar(''.join([str(settings_num + 1),'/',str(len(settings_list))]), 105, 45, 1)
    oled.show()
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        if settings_num == 0:
            DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
            pages.wifi_page()
        elif settings_num == 1:
            DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
            core.time()
        elif settings_num == 2:
            DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
            syscore.FullCollect()
        elif settings_num == 3:
            DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
            pages.about()
        elif settings_num == 4:
            DayLight.consani(64, 64, 0, 0, 0, 0, 128, 64)
            pages.choosewifi()
DayLight.consani(0, 0, 0, 0, 0, 0, 128, 64)