#from mpython import *
#import Flag_OS.system.core as core
runtimeDict["runtimeDict"]=runtimeDict
Pages=__import__("Flag_OS.system.pages",runtimeDict)
Pages.wifi_page()
while True:
    Pages.home()