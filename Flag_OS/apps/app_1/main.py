from mpython import *
import Flag_OS.system.core
import Flag_OS.apps.app_1.core

time.sleep_ms(5)
settings_list = [' ', '重连网络', '同步时间', '清理内存', '系统信息', '- Flag OS -', '- End -', ' ']
settings_num = 1
while not button_a.is_pressed():
    if touchpad_o.is_pressed() and touchpad_n.is_pressed():
        settings_num = Flag_settings_num + 1
        if settings_num > len(settings_list) - 3:
            settings_num = len(settings_list) - 3
    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
        settings_num = settings_num + -1
        if settings_num < 1:
            settings_num = 1
    Flag_OS.system.ui.app("Setting")
    oled.DispChar(str('暂无简介'), 5, 18, 1, True)
    oled.DispChar(str(settings_list[settings_num]), 5, 45, 1)
    oled.DispChar(str((''.join([str(x) for x in [settings_num, '/', len(settings_list)]]))), 105, 45, 1)
    oled.show()
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        if settings_num == 1:
            Flag_OS.system.ui.consani(64, 64, 0, 0, 0, 0, 128, 64)
            wifi_page()
        elif settings_num == 2:
            Flag_OS.system.ui.consani(64, 64, 0, 0, 0, 0, 128, 64)
            Flag_OS.apps.app_1.core.time()
        elif settings_num == 3:
            Flag_OS.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
            Flag_OS.apps.app_1.core.collect()
        elif settings_num == 4:
            Flag_OS.system.ui.consani(64, 64, 0, 0, 0, 0, 128, 64)
            Flag_OS.system.pages.about()
Flag_OS.system.ui.consani(0, 0, 0, 0, 0, 0, 128, 64)