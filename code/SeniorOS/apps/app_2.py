from mpython import *
import urequests
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import json
def app_2():
    w1 = get_seni_weather("https://api.seniverse.com/v3/weather/daily.json?key=SMhSshUxuTL0GLVLS", "ip")
    w2 = get_seni_weather("https://api.seniverse.com/v3/life/suggestion.json?key=SMhSshUxuTL0GLVLS", "ip")
    oled.fill(0)
    while not button_a.is_pressed():
        DayLight.app('天气')
        oled.DispChar(str((''.join([str(x) for x in [w1["results"][0]["location"]["name"], '   ', w1["results"][0]["daily"][0]["text_day"], '   ', w1["results"][0]["daily"][0]["low"], '  - ', w1["results"][0]["daily"][0]["high"], ' 度']]))), 0, 16, 1)
        oled.DispChar(str(('运动指数 : ' + str(w2["results"][0]["suggestion"]["sport"]["brief"]))), 0, 32, 1)
        oled.DispChar(str(('紫外线指数 : ' + str(w2["results"][0]["suggestion"]["uv"]["brief"]))), 0, 48, 1)
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