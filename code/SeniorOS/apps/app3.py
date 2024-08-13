from SeniorOS.system.devlib import *
import SeniorOS.system.pages_manager as PagesManager
import SeniorOS.system.pages as Pages
import SeniorOS.system.daylight as DayLight
import urequests

def GetSeniWeather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json

def Main():
    Pages.LoadWait()
    w1 = GetSeniWeather("https://api.seniverse.com/v3/weather/daily.json?key=SMhSshUxuTL0GLVLS", "ip")
    w2 = GetSeniWeather("https://api.seniverse.com/v3/life/suggestion.json?key=SMhSshUxuTL0GLVLS", "ip")
    oled.fill(0)

    while not button_a.is_pressed():
        DayLight.App.Style1('天气')
        oled.DispChar(str((''.join([str(x) for x in [w1["results"][0]["location"]["name"], '   ', w1["results"][0]["daily"][0]["text_day"], '   ', w1["results"][0]["daily"][0]["low"], '  - ', w1["results"][0]["daily"][0]["high"], ' 度']]))), 5, 18, 1)
        oled.DispChar('运动指数 : ' + str(w2["results"][0]["suggestion"]["sport"]["brief"]), 5, 34, 1)
        oled.DispChar('紫外线指数 : ' + str(w2["results"][0]["suggestion"]["uv"]["brief"]), 5, 50, 1)
        oled.show()
    return