#from mpython import *
#import Flag_OS.system.core as core
# --SystemUniRuntime--
eval("[/hashtag/]");runtimeDict=runtimeDict
runtimeDict["runtimeDict"]=runtimeDict
# --SystemUniRuntime--

Pages=__import__("Flag_OS.system.pages",runtimeDict)
Pages.wifi_page()
returnData=Pages.home()
while not returnData:
    returnData=Pages.home()
print("回退到FOS启动选择器")