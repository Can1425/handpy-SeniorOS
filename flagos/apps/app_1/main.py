from mpython import *
import flagos.system.core
import flagos.apps.app_1.core

time.sleep_ms(5)
Flag_settings_list = [' ', '重连网络', '同步时间', '清理内存', '系统信息', '- Flag OS -', '- End -', ' ']
Flag_settings_num = 1
while not button_a.is_pressed():
    if touchpad_o.is_pressed() and touchpad_n.is_pressed():
        Flag_settings_num = Flag_settings_num + 1
        if Flag_settings_num > len(Flag_settings_list) - 3:
            Flag_settings_num = len(Flag_settings_list) - 3
    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
        Flag_settings_num = Flag_settings_num + -1
        if Flag_settings_num < 1:
            Flag_settings_num = 1
    flagos.system.core.ui_app("Setting")
    oled.DispChar(str('暂无简介'), 5, 18, 1, True)
    oled.DispChar(str(Flag_settings_list[Flag_settings_num]), 5, 45, 1)
    oled.DispChar(str((''.join([str(x) for x in [Flag_settings_num, '/', len(Flag_settings_list)]]))), 105, 45, 1)
    oled.show()
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        if Flag_settings_num == 1:
            flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
            wifi()
        elif Flag_settings_num == 2:
            flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
            flagos.apps.app_1.core.time()
        elif Flag_settings_num == 3:
            flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
            flagos.apps.app_1.core.collect()
        elif Flag_settings_num == 4:
            flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
            flagos.system.pages.about()
flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)