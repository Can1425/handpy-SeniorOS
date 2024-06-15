# from mpython import *
# import SeniorOS.system.core as core
import uos as os;os.chdir('/')
import SeniorOS.system.pages as Pages
Pages.WifiPages()
returnData=Pages.Home()
while not returnData:
    returnData=Pages.Home()
print("回退到 SeniorOS 启动选择器")