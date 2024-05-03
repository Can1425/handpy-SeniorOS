# from mpython import *
# import SeniorOS.system.core as core
import uos as os;os.chdir('/')
import SeniorOS.system.pages as Pages
Pages.wifi_page()
returnData=Pages.home()
while not returnData:
    returnData=Pages.home()
print("回退到 SeniorOS 启动选择器")