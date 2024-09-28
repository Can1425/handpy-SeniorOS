from SeniorOS.lib.devlib import *
import SeniorOS.system.core as Core
import SeniorOS.system.pages as Pages
import SeniorOS.system.daylight as DayLight
import SeniorOS.system.radient as Radient
import _thread,json

def GetSeniWeather(_url, _location):
    return json.loads(Radient.Get(_url + "&location=" + _location.replace(" ", "%20"))[1].encode())
def Main():
    DayLight.App.Style1('天气')
    #等等，你没导入core（我还以为你在其他的库包含了，C++后遗症）
    Quit = Core.SharedVar.LoadQuit()
    Quit.value = False
    _thread.start_new_thread(Pages.LoadWait, (Quit, eval("[/Language('请稍等')/]"), False))
    try:
        w1 = GetSeniWeather("https://api.seniverse.com/v3/weather/daily.json?key=SMhSshUxuTL0GLVLS", "ip")
        w2 = GetSeniWeather("https://api.seniverse.com/v3/life/suggestion.json?key=SMhSshUxuTL0GLVLS", "ip")
    except Exception as e:
        __import__("sys").print_exception(e)
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