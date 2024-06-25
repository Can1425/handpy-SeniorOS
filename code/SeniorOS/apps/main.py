from mpython import *
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import machine
import esp32
import os
import json
import urequests
#-----------------------------------------------------------------------------------#
def app_0():
    DayLight.UITools()
    from SeniorOS.system.pages import about,WifiPages,choosewifi
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
        DayLight.app("设置")
        oled.DispChar(str(settings_tip[settings_num]), 5, 18, 1, True)
        oled.DispChar(str(settings_list[settings_num]), 5, 45, 1)
        oled.DispChar(''.join([str(settings_num + 1),'/',str(len(settings_list))]), 105, 45, 1)
        oled.show()
        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
            if settings_num == 0:
                DayLight.ConsaniSideslip(True)
                settings0Num = DayLight.Select(['重连网络', '同步时间', '新建网络配置'], 28, True, "选择")
                DayLight.ConsaniSideslip(False)
                if settings0Num == 0:
                    DayLight.ConsaniSideslip(True)
                    WifiPages()
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
                settings1Num = DayLight.Select(['日光模式', '动效开关', '日光引擎信息'], 28, True, "选择")
                DayLight.ConsaniSideslip(False)
                if settings1Num == 0:
                    DayLight.ConsaniSideslip(True)
                    App0DayLightMode()
                    DayLight.ConsaniSideslip(False)
                elif settings1Num == 1:
                    DayLight.ConsaniSideslip(True)
                    App0DynamicEffectSwitch()
                    DayLight.ConsaniSideslip(False)
                elif settings1Num == 2:
                    DayLight.ConsaniSideslip(True)
                    DayLight.About()
                    DayLight.ConsaniSideslip(False)
            elif settings_num == 2:
                DayLight.ConsaniSideslip(True)
                settings3Num = DayLight.Select(['释放内存', '内存信息'], 28, True, "选择")
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
    options = DayLight.ListOptions(['软重启', '关闭显示器', '休眠'], 8, True, "None")
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
            oled.show()
        except:
            try:
                oled.DispChar(poetry[0], 5, 18, 1)
                oled.DispChar('轻触任意触摸键退出', 5, 50, 1)
                oled.show()
            except:
                pass
        machine.lightsleep()
        DayLight.UITools()
        DayLight.ConsaniSideslip(False)

def App0DynamicEffectSwitch():
    while not button_a.is_pressed():
        oled.fill(0)
        DayLight.UITools()
        oled.DispChar(str('动效开关'), 5, 5, 1)
        time.sleep_ms(5)
        if Core.Data.Get('VastSea_switch') == "1":
            get = '开启'
        else:
            get = '关闭'
        oled.DispChar(get, 5, 18, 1)
        oled.show()
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            Core.Data.Write('VastSea_switch','1',False,False)
            oled.show()
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            Core.Data.Write('VastSea_switch','0',False,False)
            oled.show()
    return
#-----------------------------------------------------------------------------------#
def app_1():
    plugins_num = 0
    while not button_a.is_pressed():
        gc.enable()
        gc.collect()
        DayLight.app('线上插件')
        oled.DispChar(str('正在尝试获取插件信息'), 5, 18, 1, True)
        oled.show()
        _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/list.fos', headers={})
        plugins_list = (_response.text.split(';'))
        _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/tip.fos', headers={})
        plugins_tip = (_response.text.split(';'))
        _response = urequests.get('https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/web-app/tip.fos', headers={})
        plugins_tip2 = (_response.text.split(';'))
        print(len(plugins_list))
        print(plugins_tip)
        gc.collect()
        break
    while not button_a.is_pressed():
        DayLight.app('线上插件')
        oled.DispChar(str(('作者:' + str(plugins_tip[plugins_num]))), 5, 18, 1, True)
        oled.DispChar(str(plugins_list[plugins_num]), 5, 45, 1)
        oled.DispChar(str((''.join([str(x) for x in [plugins_num + 1, '/', len(plugins_list)]]))), 105, 45, 1)
        oled.show()
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            plugins_num = plugins_num - 1
            time.sleep(0.5)
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            plugins_num = plugins_num + 1
            time.sleep(0.5)
        if plugins_num < 0:
            plugins_num = 0
            time.sleep(0.5)
        if plugins_num +1  > len(plugins_list):
            plugins_num = len(plugins_list) - 1
            time.sleep(0.5)
        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
            options = DayLight.ListOptions(['获取并运行', '插件详情', '缓存该插件'], 8, True, "None")
            if options == 0:
                DayLight.ConsaniSideslip(True)
                DayLight.app('线上插件')
                oled.DispChar(str('请稍等，正在获取源码'), 5, 18, 1, True)
                oled.DispChar(str('如A键无法退出，重启'), 5, 45, 1, True)
                oled.show()
                _response = urequests.get((''.join([str(x) for x in ['https://gitee.com/can1425/mpython-senioros-radient/raw/plugins/web-app/', plugins_num + 1, '.fos']])), headers={})
                oled.fill(0)
                exec(_response.text)
                DayLight.ConsaniSideslip(False)
            if options == 1:
                DayLight.ConsaniSideslip(True)
                while not button_a.is_pressed():
                    DayLight.app(str(plugins_list[plugins_num]))
                    oled.DispChar(str(plugins_tip2[plugins_num]), 5, 18, 1, True)
                    oled.show()
                DayLight.ConsaniSideslip(False)
#-----------------------------------------------------------------------------------#
def app_2():
    get = os.listdir()
    while not button_a.is_pressed():
        options = DayLight.ListOptions(get, 20, False, "侧载运行器")
#-----------------------------------------------------------------------------------#
def app_3():
    w1 = get_seni_weather("https://api.seniverse.com/v3/weather/daily.json?key=SMhSshUxuTL0GLVLS", "ip")
    w2 = get_seni_weather("https://api.seniverse.com/v3/life/suggestion.json?key=SMhSshUxuTL0GLVLS", "ip")
    oled.fill(0)
    while not button_a.is_pressed():
        DayLight.app('天气')
        oled.DispChar(str((''.join([str(x) for x in [w1["results"][0]["location"]["name"], '   ', w1["results"][0]["daily"][0]["text_day"], '   ', w1["results"][0]["daily"][0]["low"], '  - ', w1["results"][0]["daily"][0]["high"], ' 度']]))), 5, 18, 1)
        oled.DispChar(str(('运动指数 : ' + str(w2["results"][0]["suggestion"]["sport"]["brief"]))), 5, 34, 1)
        oled.DispChar(str(('紫外线指数 : ' + str(w2["results"][0]["suggestion"]["uv"]["brief"]))), 5, 50, 1)
        oled.show()
    return

def get_seni_weather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json


def get_seni_weather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json
#-----------------------------------------------------------------------------------#
image_picture = Image()

def app_4():
    num = 1
    while not button_a.is_pressed():
        DayLight.app('手电筒')
        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
            num = 1
        if touchpad_o.is_pressed() and touchpad_n.is_pressed():
            num = 0
        if num == 1:
            oled.blit(image_picture.load('face/System/Dot_full.pbm', 0), 48, 20)
            oled.show()
            rgb.fill((int(255), int(255), int(255)))
            rgb.write()
            time.sleep_ms(1)
        else:
            oled.blit(image_picture.load('face/System/Dot_empty.pbm', 0), 48, 20)
            oled.show()
            rgb.fill( (0, 0, 0) )
            rgb.write()
    num = 0
    rgb.fill( (0, 0, 0) )
    rgb.write()
    time.sleep_ms(1)
    return
#-----------------------------------------------------------------------------------#
poetry = None
def app_5():
    Poetry()
    while not button_a.is_pressed():
        oled.fill(0)
        DayLight.app('即时诗词')
        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
            Poetry()
        try:
            oled.DispChar(poetry[0], 5, 18, 1)
            oled.DispChar(poetry[1], 5, 34, 1)
            oled.DispChar('TH - 刷新', 5, 50, 1)
        except:
            try:
                oled.DispChar(poetry[0], 5, 18, 1)
                oled.DispChar('TH - 刷新', 5, 50, 1)
            except:
                oled.DispChar('诗词走丢啦！', 5, 18, 1)
                oled.DispChar('TH - 刷新', 5, 50, 1)
        oled.show()
    return

def Poetry():
    global poetry
    try:
        _response = urequests.get(str(Core.Data.Get('poetrySource')), headers={})
        poetry = (_response.text.split('，'))
        return
    except:
        return
#--------------------------------------------------------------------------------#
from mpython import*
import os
import time
def IsFile(f):
    print(f)
    if os.stat(f)[0]<20000:return "目录"
    else:
        return fileattribute(f)
def fileattribute(f):
    last4=f[-4:]
    last3=f[-3:]
    if last3==".py":
        return "可执行文件"
    elif last4==".pbm" or last4==".bmp":
        return "图片"
    else:
        return "文件"
def waitkey(**kwargs):
    while True:
        for value,key in kwargs.items():
            if key.is_pressed():
                return value
pathpic=bytearray([0X00,0X00,0X3E,0X00,
                   0X41,0X00,0X80,0X80,
                   0X81,0XFC,0XFE,0X02,
                   0X80,0X01,0X80,0X01,
                   0XFF,0XFF,0X80,0X01,
                   0X80,0X01,0X80,0X01,
                   0X80,0X01,0X80,0X01,
                   0X40,0X02,0X3F,0XFC,])
filepic=bytearray([0X00,0X00,0X3F,0XC0,
                   0X20,0X60,0X2F,0X50,
                   0X20,0X48,0X2F,0X7C,
                   0X20,0X04,0X23,0XC4,
                   0X22,0X04,0X23,0X84,
                   0X22,0X04,0X22,0X04,
                   0X22,0X04,0X20,0X04,
                   0X3F,0XFC,0X00,0X00,])
runpic=bytearray([0X00,0X00,0X3F,0XC0,
                  0X20,0X60,0X2F,0X50,
                  0X20,0X48,0X2F,0X7C,
                  0X20,0X04,0X23,0XC4,
                  0X22,0X04,0X23,0X84,
                  0X22,0X04,0X22,0X04,
                  0X22,0X04,0X20,0X04,
                  0X3F,0XFC,0X00,0X00,])
picpic=bytearray([0XFF,0XFF,0X80,0X01,
                  0X8C,0X01,0X92,0X01,
                  0X92,0X09,0X8C,0X15,
                  0X80,0X23,0X84,0X41,
                  0X8A,0X81,0X91,0X01,
                  0XA0,0X01,0XC0,0X01,
                  0X80,0X01,0X80,0X01,
                  0X80,0X01,0XFF,0XFF,])
def fileviewer(initpath:str):
    path=initpath
    if path[:2]=="//":
        path=path[1:]
    Pathpic=pathpic
    Filepic=filepic
    Runpic=runpic
    Picpic=picpic
    def lastpath(path:str):
        return "/".join(path.split("/")[:-1])
    while True:
        Dir=os.listdir(path)
        DIRlen=len(Dir)
        num=0
        while True:
            t=IsFile("{}/{}".format(path,Dir[num]))
            oled.fill(0)
            oled.DispChar(Dir[num],16,0)
            oled.DispChar("属性:{}".format(t),0,16)
            oled.DispChar("<P           {}/{}           N>".format(num+1,DIRlen),1,48)
            if t=="目录":
                oled.Bitmap(0, 0,Pathpic, 16, 16, 1)
            elif t=="文件":
                oled.Bitmap(0,0,Filepic,16,16,1)
            elif t=="可执行文件":
                oled.Bitmap(0,0,Runpic,16,16,1)
            elif t=="图片":
                oled.Bitmap(0,0,Picpic,16,16,1)
            oled.hline(0,16,130,1)
            oled.show()
            key=waitkey(A=button_a,B=button_b,Y=touchpad_y,T=touchpad_t,H=touchpad_h,O=touchpad_o,N=touchpad_n,P=touchpad_p)
            if key=="T" or key=="H":
                if path=="/":
                    #print("已经是根目录")
                    continue
                path=lastpath(path)
                #print("返回上一级目录:{}".format(path))
                break
            elif key=="B":
                if t=="目录":
                    #print("进入目录:{}".format(Dir[num]))
                    #print("正在加载......可能需要几秒钟")
                    #print("Path: {}/{}".format(path,Dir[num]))
                    path="{}/{}".format(path,Dir[num])
                    break
                elif t=="文件":
                    oled.fill(0)
                    oled.DispChar("暂时不支持文件预览",0,0)
                    oled.DispChar("1秒后返回",0,16)
                    oled.show()
                    time.sleep(1)
                    break
                elif t=="可执行文件":
                    libname=("{}/{}".format(path,Dir[num]))[:-3].replace("/",".")
                    while libname[0]==".":
                        libname=libname[1:]
                    try:
                        __import__(libname)
                    except Exception as e:
                        print("导入失败，错误信息如下：\n",e.__class__.__name__,e)
                    else:
                        #print("导入成功")
                        pass
                elif t=="图片":
                    oled.fill(0)
                    image_picture = Image()
                    oled.blit(image_picture.load('{}/{}'.format(path,Dir[num])), 0, 0)
                    oled.show()
                    while not key=="T" or key=="H":
                        pass
            elif key=="N":
                num+=1
                if num>=DIRlen:num=0
            elif key=="P":
                num-=1
                if num<0:num=DIRlen-1
def app_6():
    path='/'
    fileviewer(path)
#鸣谢名单
#程序设计---LP_OVER/emofalling
#界面设计---LP_OVER
#bug修复/优化---emofalling
#运行平台提供---Can1425
#感谢各位的付出!
#fileviewer  -by LP_OVER/emofalling
#-------------------------------------------------------------------------------------------#