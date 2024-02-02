from mpython import *
import flagos.system.pages
import ntptime
import network
import time

time_hour = 0
time_min = 0
sys_hour = 0
sys_min = 0

def ui_app(Flag_sys_ui_app_title):
    global time_hour, time_min, sys_hour, sys_min
    time_disposal()
    oled.fill(0)
    if str(get_file('./flagos/data/Flag_sys_ui_light.fos', '\r\n')) == 'Open':
        oled.invert(1)
    else:
        oled.invert(0)
    oled.fill_rect(1, 0, 126, 16, 1)
    oled.DispChar(str((str(Flag_sys_ui_app_title))), 5, 0, 2)
    oled.DispChar(str((''.join([str(x) for x in [time_hour, ':', time_min]]))), 93, 0, 2)
    oled.hline(50, 62, 30, 1)

def consani(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, consani_start_x, consani_start_y, consani_start_wide, consani_start_height):
    if str(get_file('./flagos/data/Flag_sys_ui_light.fos', '\r\n')) == 'Open':
        oled.invert(1)
    else:
        oled.invert(0)
    try:
      consani_done_wait = 3
      oled.fill(0)
      for count in range(7):
          oled.RoundRect(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, 2, 1)
          oled.fill(0)
          consani_done_x = (consani_done_x - consani_start_x) // 2
          consani_done_y = (consani_done_y - consani_start_y) // 2
          consani_done_wide = (consani_start_wide + consani_done_wide) // 2
          consani_done_height = (consani_start_height + consani_done_height) // 2
          oled.RoundRect(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, 2, 1)
          oled.show()
    except:
        oled.DispChar(str(' :( 我们遇到了一些问题，将在 3 秒后返回'), 5, 25, 1, True)
        oled.show()
        return
        
    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
        return
    time.sleep_ms(consani_done_wait)

def time_disposal():
    global time_hour, time_min, sys_hour, sys_min
    time_hour = str(time.localtime()[3])
    time_min = str(time.localtime()[4])
    sys_hour = str(time.localtime()[3])
    sys_min = str(time.localtime()[4])
    if len(sys_hour) < 2:
        time_hour = '0' + str(sys_hour)
    else:
        time_hour = sys_hour
    if len(sys_min) < 2:
        time_min = '0' + str(sys_min)
    else:
        time_min = sys_min

def init_file(_path):
    f = open(_path, 'w')
    f.close()

def get_file(_path, _sep):
    f = open(_path, 'r')
    result = f.read().split(_sep)
    f.close()
    return result

def write_file(_path, _data, _sep):
    f = open(_path, 'a')
    f.write(_data + _sep)
    f.close()

def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]