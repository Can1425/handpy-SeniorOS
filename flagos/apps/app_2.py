from mpython import *
import urequests
import flagos.system.core

Flag_plugins_num = 1

while not button_a.is_pressed():
    gc.enable()
    gc.collect()
    flagos.system.core.ui_app('Flag 线上插件')
    oled.DispChar(str('正在尝试获取应用信息'), 5, 18, 1, True)
    oled.show()
    _response = urequests.get('https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/list.fos', headers={})
    Flag_plugins_list = (_response.text.split(';'))
    _response = urequests.get('https://gitee.com/can1425/mPython_Flag-OS_Radient/raw/plugins/tip.fos', headers={})
    Flag_plugins_tip = (_response.text.split(';'))
    print(len(Flag_plugins_list))
    print(Flag_plugins_tip)
    gc.collect()
    break
while not button_a.is_pressed():
    flagos.system.core.ui_app('Flag 线上插件')
    oled.DispChar(str(('作者:' + str(Flag_plugins_tip[Flag_plugins_num]))), 5, 18, 1, True)
    oled.DispChar(str(Flag_plugins_list[Flag_plugins_num]), 5, 45, 1)
    oled.DispChar(str((''.join([str(x) for x in [Flag_plugins_num, '/', len(Flag_plugins_list)]]))), 105, 45, 1)
    oled.show()
    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
        Flag_plugins_num = Flag_plugins_num - 1
        time.sleep(0.5)
    if touchpad_o.is_pressed() and touchpad_n.is_pressed():
        Flag_plugins_num = Flag_plugins_num + 1
        time.sleep(0.5)
    if Flag_plugins_num < 1:
        Flag_plugins_num = 1
        time.sleep(0.5)
    if Flag_plugins_num > 4:
        Flag_plugins_num = 4
        time.sleep(0.5)
    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
        flagos.system.core.consani(64, 64, 0, 0, 0, 0, 128, 64)
        flagos.system.core.ui_app('Flag 线上插件')
        oled.DispChar(str('请稍等，正在获取源码'), 5, 18, 1, True)
        oled.DispChar(str('如A键无法退出，重启'), 5, 45, 1, True)
        oled.show()
        _response = urequests.get((''.join([str(x) for x in ['https://gitee.com/can1425/Flag-OS_plugins/raw/master/Flag_plugins/', Flag_plugins_num, '.fos']])), headers={})
        Flag_consani(64, 64, 0, 0, 0, 0, 128, 64)
        oled.fill(0)
        exec(_response.text)
        flagos.system.core.consani(0, 0, 0, 0, 0, 0, 128, 64)