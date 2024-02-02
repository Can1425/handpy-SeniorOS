from mpython import *
import flagos.system.core

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
            try:
                flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
                oled.fill(0)
                oled.DispChar(str('请稍等...'), 0, 0, 1)
                oled.show()
                ntptime.settime(8, "time.windows.com")
                oled.fill(0)
                oled.DispChar(str('成功'), 0, 0, 1)
                oled.show()
                flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
            except:
                flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
                oled.fill(0)
                oled.DispChar(str('失败'), 0, 0, 1)
                oled.show()
                flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
        elif Flag_settings_num == 3:
            try:
                flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
                oled.fill(0)
                oled.DispChar(str('请稍等...'), 0, 0, 1)
                oled.show()
                gc.enable()
                gc.collect()
                oled.fill(0)
                oled.DispChar(str('成功'), 0, 0, 1)
                oled.show()
                flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
            except:
                flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
                oled.fill(0)
                oled.DispChar(str('失败'), 0, 0, 1)
                oled.show()
                flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
        elif Flag_settings_num == 4:
            flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
            oled.fill(0)
            while not button_a.is_pressed():
                oled.Bitmap(32, 12, bytearray([0XFF,0X38,0X00,0X00,0X00,0X03,0X80,0X38,0XFF,0X38,0X00,0X00,0X00,0X0F,0XE0,0XFE, 0XFF,0X38,0X00,0X00,0X00,0X1E,0XF1,0XEF,0XE0,0X38,0X00,0X00,0X00,0X38,0X71,0X86, 0XE0,0X38,0XFC,0X3D,0X80,0X30,0X39,0X80,0XE0,0X38,0XFC,0X7F,0X80,0X30,0X39,0XE0, 0XFF,0X38,0X0E,0X63,0X80,0X30,0X38,0XFC,0XFF,0X38,0X3E,0X61,0X80,0X30,0X38,0X1E, 0XE0,0X38,0XFE,0X61,0X80,0X30,0X38,0X07,0XE0,0X39,0XCE,0X61,0X80,0X38,0X30,0X87, 0XE0,0X39,0X8E,0X73,0X80,0X3C,0XF1,0XC7,0XE0,0X3D,0XFE,0X3F,0X80,0X1F,0XE1,0XFE, 0XE0,0X1C,0XEE,0X1D,0X80,0X07,0XC0,0X78,0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X00, 0X00,0X00,0X00,0X73,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X3F,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X1C,0X00,0X00,0X00,0X00,]), 64, 18, 1)
                oled.DispChar(str('Flag OS 2.0 (240107008[mxDF])'), 0, 32, 1, True)
                oled.show()
            flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)
flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)