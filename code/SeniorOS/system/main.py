print(eval("[/Const('systemRunLog')/]") + "system/main.mpy")
import uos as os;os.chdir('/')
import SeniorOS.system.pages as Pages
Pages.WifiPages()
returnData=Pages.Home()

while not returnData:
    returnData=Pages.Home()
