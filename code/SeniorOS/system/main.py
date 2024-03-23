# from mpython import *
# import SeniorOS.system.core as core
from mpython import wifi,oled
from mpython import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from mpython import button_a,button_b
import gc
import time,uos
runtimeDict={
        "oled":oled,"wifi":wifi(),
        "touchPad_P":touchPad_P,"touchPad_Y":touchPad_Y,"touchPad_H":touchPad_H,"touchPad_O":touchPad_O,"touchPad_N":touchPad_N,"touchPad_T":touchPad_T,
        "button_a":button_a,"button_b":button_b,
        "ntptime":__import__('ntptime'),
        "time":time,
        "gc":gc,
        "os":uos
}
# --SystemUniRuntime--
eval("[/hashtag/]");runtimeDict=runtimeDict
runtimeDict["runtimeDict"]=runtimeDict
# --SystemUniRuntime--

import SeniorOS.system.pages as Pages
Pages.wifi_page()
returnData=Pages.home()
while not returnData:
    returnData=Pages.home()
print("回退到 SeniorOS 启动选择器")