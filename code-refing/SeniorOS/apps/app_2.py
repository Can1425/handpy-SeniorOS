from mpython import *
import urequests
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight

def app_2():
    musicNum = 0
    while not button_a.is_pressed():
        gc.enable()
        gc.collect()
        DayLight.app('线上音乐')
        oled.DispChar(str('正在尝试获取应用信息'), 5, 18, 1, True)
        oled.show()
        _response = urequests.get(Core.Data.Get('MusicSource') + '/raw/music/namelist.fos', headers={})
        musicNameList = (_response.text.split(';'))
        _response = urequests.get(Core.Data.Get('MusicSource') + '/raw/music/tip.fos', headers={})
        musicTip = (_response.text.split(';'))
        _response = urequests.get(Core.Data.Get('MusicSource') + '/raw/music/linklist.fos', headers={})
        musicLinkList = (_response.text.split(';'))
        print(len(musicNameList))
        print(musicTip)
        gc.collect()
        break
    while not button_a.is_pressed():
        DayLight.app('线上音乐')
        oled.DispChar(str((str(musicTip[musicNum]))), 5, 18, 1, True)
        oled.DispChar(str(musicNameList[musicNum]), 5, 45, 1)
        oled.DispChar(str((''.join([str(x) for x in [plugins_num, '/', len(plugins_list) - 1]]))), 105, 45, 1)
        oled.show()
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            musicNum = musicNum - 1
            time.sleep(0.5)
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            musicNum = musicNum + 1
            time.sleep(0.5)
        if musicNum < 0:
            musicNum = 0
            time.sleep(0.5)
        if musicNum + 1 > len(musicNameList):
            musicNum = len(musicNameList) - 1
            time.sleep(0.5)
        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
            audio.player_init()
            audio.play(str(musicLinkList[musicNum]))