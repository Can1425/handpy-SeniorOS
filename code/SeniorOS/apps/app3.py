from SeniorOS.system.devlib import *
import SeniorOS.system.core as Core
import SeniorOS.system.pages_manager as PagesManager
import SeniorOS.system.pages as Pages
import SeniorOS.system.daylight as DayLight
import urequests
import _thread

def GetSeniWeather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json
# Can，我觉得可以把SharedVar放到core.py里面,好，或许我们还可以拓展它的功能，不仅仅只限于服务于这个 确实，毕竟SharedVar原本是避免python的低内存变量传递复制行为而构建的一个类（里面的任何值在传递的时候都不会复制）
def Main():
    DayLight.App.Style1('天气')
    #等等，你没导入core（我还以为你在其他的库包含了，C++后遗症）
    Quit = Core.SharedVar.LoadQuit()
    Quit.value = False
    _thread.start_new_thread(Pages.LoadWait, (Quit, eval("[/Language('请稍等')/]"), False))
    try:
        w1 = GetSeniWeather("https://api.seniverse.com/v3/weather/daily.json?key=SMhSshUxuTL0GLVLS", "ip")
        w2 = GetSeniWeather("https://api.seniverse.com/v3/life/suggestion.json?key=SMhSshUxuTL0GLVLS", "ip")
    except:
        Quit.value = True
    Quit.value = True
    oled.fill(0)

    while not button_a.is_pressed():
        DayLight.App.Style1('天气')
        oled.DispChar(str((''.join([str(x) for x in [w1["results"][0]["location"]["name"], '   ', w1["results"][0]["daily"][0]["text_day"], '   ', w1["results"][0]["daily"][0]["low"], '  - ', w1["results"][0]["daily"][0]["high"], ' 度']]))), 5, 18, 1)
        oled.DispChar('运动指数 : ' + str(w2["results"][0]["suggestion"]["sport"]["brief"]), 5, 34, 1)
        oled.DispChar('紫外线指数 : ' + str(w2["results"][0]["suggestion"]["uv"]["brief"]), 5, 50, 1)
        oled.show()
    return