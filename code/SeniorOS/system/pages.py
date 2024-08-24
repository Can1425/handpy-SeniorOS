import SeniorOS.system.daylight as DayLight
import SeniorOS.system.core as Core
import SeniorOS.system.typer as Typer
import SeniorOS.system.ftreader as FTReader
import urequests
import ntptime
import micropython
from SeniorOS.system.devlib import wifi,oled
from SeniorOS.system.devlib import touchPad_P,touchPad_Y,touchPad_H,touchPad_O,touchPad_N,touchPad_T
from SeniorOS.system.devlib import button_a,button_b
import gc
import time
import machine
import SeniorOS.system.log_manager as LogManager
import SeniorOS.system.pages_manager as PagesManager
import _thread
import os

source = "https://" + Core.Data.Get("text", "radienPluginsSource")
Log = LogManager.Log
Log.Info("system/pages.mpy")
wifi=wifi()

def ConfigureWLAN(ssid, password):
    oled.fill(0)
    oled.Bitmap(16, 20, bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X3C,0X00,0X00,0X00,0X30, 0X00,0X00,0X00,0X70,0X00,0X78,0X00,0X03,0XFE,0X00,0X00,0X00,0X70,0X00,0X00,0X03, 0XFE,0X03,0XFE,0X00,0X07,0XFC,0X00,0X00,0X00,0X30,0X00,0X00,0X07,0X8F,0X07,0XFE, 0X00,0X06,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X0E,0X03,0X86,0X00,0X00,0X06,0X00, 0X0E,0X03,0XE0,0X20,0X38,0X01,0X8C,0X01,0X8E,0X00,0X00,0X0E,0X00,0X3F,0X87,0XF8, 0X71,0XFE,0X0F,0X98,0X00,0XCE,0X00,0X00,0X0F,0X00,0X7B,0XC7,0XFC,0X71,0XFF,0X1F, 0X98,0X00,0XCE,0X00,0X00,0X07,0XF0,0X60,0XCE,0X0C,0X63,0X83,0X18,0X18,0X00,0XC7, 0XF0,0X00,0X03,0XFC,0XE0,0XCE,0X0C,0X63,0X03,0X38,0X18,0X00,0XC3,0XFC,0X00,0X00, 0X1C,0XFF,0XCE,0X0C,0X63,0X03,0X38,0X18,0X00,0XC0,0X1C,0X00,0X00,0X0C,0XFF,0XCC, 0X0C,0X67,0X03,0X30,0X18,0X00,0XC0,0X0C,0X00,0X00,0X0C,0XC0,0X0C,0X0C,0X67,0X03, 0X30,0X0C,0X01,0XC0,0X0C,0X00,0X00,0X1C,0XC0,0X0C,0X1C,0XE7,0X07,0X30,0X0E,0X03, 0X80,0X1C,0X00,0X00,0X3C,0XE0,0X0C,0X1C,0XE7,0X8E,0X30,0X07,0X8F,0X00,0X3C,0X00, 0X1F,0XF8,0X7F,0X8C,0X1C,0XE3,0XFE,0X30,0X03,0XFE,0X1F,0XF8,0X00,0X1F,0XE0,0X3F, 0X8C,0X18,0XC1,0XF8,0X30,0X00,0XF8,0X1F,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
    oled.show()
    Quit = Core.SharedVar.LoadQuit()
    Quit.value = False
    _thread.start_new_thread(LoadWait,(Quit,"None",False))
    try:
        wifi.connectWiFi(ssid, password)
        ntptime.settime(8,"time.windows.com")
        time.sleep(2)
        Quit.value = True
        return True
    except: 
        time.sleep(2)
        Quit.value = True
        return False

def WifiPages():
    oled.fill(0)
    DayLight.VastSea.Off()
    while not eval("[/GetButtonExpr('th')/]"):
        wifiNum = DayLight.ListOptions(Core.Data.Get("list", "wifiName"), False, eval("[/Language('请选择配置')/]"))
    oled.show()
    ConfigureWLAN((Core.Data.Get("list", "wifiName")[wifiNum]), (Core.Data.Get("list", "wifiPassword")[wifiNum]))


def CloudNotification():
    time.sleep_ms(int(eval("[/Const('interval')/]")))
    DayLight.App.Style1(eval("[/Language('云端通知')/]"))
    Quit = Core.SharedVar.LoadQuit()
    Quit.value = False
    _thread.start_new_thread(LoadWait, (Quit, eval("[/Language('请稍等')/]"), False))
    oled.show()
    try:
        _response = urequests.get(source + '/Notifications.sros', headers={})
        notifications = (_response.text.split(';'))
    except:
        Quit.value = True
        return
    Quit.value = True
    while not button_a.is_pressed():
        DayLight.App.Style1(eval("[/Language('云端通知')/]"))
        oled.DispChar(notifications[1], 5, 18)
        oled.DispChar(notifications[2], 5, 32)
        oled.DispChar(notifications[3], 5, 45)
        oled.show()
    return

def EquipmentPanel(): 
    def HS_CPU():
        oled.fill(0)
        oled.DispChar("目前频率:{} MHZ".format(str(machine.freq()/1000000)),0,32)
        oled.DispChar("CPU - ESP32",0,0)
        oled.DispChar("NORMAL 160HZ",0,16)
        oled.show()
        while True:
            if button_a.is_pressed():return
    def HS_Ram():
        while not button_a.is_pressed():
            oled.fill(0)
            oled.DispChar("Ram - total:520kb",0,0)
            oled.DispChar(f"内存可用:{str(gc.mem_free())} Bytes",0,16)
            oled.DispChar("触摸键释放内存",0,32)
            oled.show()
            if eval("[/GetButtonExpr('python')/]"):
                Collect()
        return 0
    def HS_flash():
        fileSystemStatus=os.statvfs("/")
        fileSystemFree=fileSystemStatus[3] * fileSystemStatus[1]
        oled.fill(0)
        oled.DispChar("Flash - total: 8MB",5,0)
        oled.DispChar("可用:{} MB".format(fileSystemFree/81920),5,16)
        DayLight.ProgressBoxMove(5,32,100,10,((100 - 0) / (8 - 0)) * ((fileSystemFree / 81920) - 0) + 0)
        oled.show()
        while not button_a.is_pressed():
            if button_a.is_pressed():
                del fileSystemStatus,fileSystemFree
                gc.collect()    
                return 0
    def PeripheralPanel():
        PeripheralList = ["引脚控制","UART控制"]
        PeripheralPin = ["Pin.P0","Pin.P1","Pin.P2","Pin.P3","Pin.P8","Pin.P9","Pin.P13","Pin.P14","Pin.P15","Pin.P16"]
        #PeripheralUART = ["Pin.13","Pin.14","Pin.15","Pin.16"]
        while not button_a.is_pressed():
            options = DayLight.Select.Style4(PeripheralList, False, "控制面板")
            if options == 0:
                DayLight.VastSea.Transition() 
                options = DayLight.Select.Style4(PeripheralPin, False, "选择引脚")
                if options!=None:
                    DayLight.VastSea.Transition() 
                    selsetPin=PeripheralPin[options]
                else: 
                    DayLight.VastSea.Transition(False)
                    return
                SS=DayLight.Select.Style4(["输出","输入"], False, "选择模式")
                try:
                    if SS == 0:
                        while not button_a.is_pressed():
                            oled.fill(0)
                            oled.DispChar("引脚 {} 的值为".format(selsetPin),5,0)
                            PIN=eval("Pin({},Pin.IN)".format(selsetPin))
                            oled.DispChar(str(PIN.value()),5,16)
                            oled.show()
                        DayLight.VastSea.Transition(False)
                        return
                    else:
                        while not button_a.is_pressed():
                            val=DayLight.Select.Style4(["高","低"], False, "选择{}电平".format(selsetPin))
                            if val != None:
                                DayLight.VastSea.Transition()
                                PIN=eval("Pin({},Pin.OUT)".format(selsetPin))
                                if val == 0:PIN.on()
                                else:PIN.off()
                            else:
                                DayLight.VastSea.Transition(False)
                                return
                        return 
                except:
                    while not button_a.is_pressed():
                        oled.fill(0)
                        DayLight.Text("引脚状态获取失败，请尝试检查外设是否正确连接",5, 5, 1)
                        oled.show()
                    DayLight.VastSea.Transition(False)
                    return
            elif options == 1:
                while not button_a.is_pressed():
                    oled.fill(0)
                    DayLight.Text("暂不可用",5, 5, 1)
                    oled.show()
                DayLight.VastSea.Transition(False)
                return
            else:
                DayLight.VastSea.Transition(False)
                return
                

    ListOperation = {
    0: HS_CPU,
    1: HS_Ram,
    2: HS_flash,
    3: PeripheralPanel
    }
    hardware=["CPU","RAM","Flash","外设控制"]
    while not button_a.is_pressed():
        options = DayLight.Select.Style4(hardware, False, "设备面板")
        if options != None:
            DayLight.VastSea.Transition()
            ListOperation.get(options)()
            DayLight.VastSea.Transition(False)
        else:
            return
        
def Home():
    oled.fill(0)
    time.sleep_ms(int(eval("[/Const('interval')/]")))
    while not eval("[/GetButtonExpr('pythonab')/]"):
        PagesManager.Main.Import('SeniorOS.style.home', 'Style' + Core.Data.Get("text", "homeStyleNum"), False)
    if button_a.is_pressed():
        DayLight.VastSea.SeniorMove.Text(eval("[/Language('云端通知')/]"),-10,-20,5,0)
        PagesManager.Main.Import("SeniorOS.system.pages", "CloudNotification")
        DayLight.VastSea.SeniorMove.Text(eval("[/Language('云端通知')/]"),5,0,-10,-20)
    elif button_b.is_pressed():
        DayLight.VastSea.SeniorMove.Text(eval("[/Language('设备面板')/]"),138,-20,5,0)
        PagesManager.Main.Import("SeniorOS.system.pages", "EquipmentPanel")
        DayLight.VastSea.SeniorMove.Text(eval("[/Language('设备面板')/]"),5,0,138,-20)
    elif eval("[/GetButtonExpr('th')/]"):
        DayLight.VastSea.SeniorMove.Line(128, 0, 0, 0, 0, 46, 128, 46)
        PagesManager.Main.Import("SeniorOS.apps.port", "App")
        DayLight.VastSea.SeniorMove.Line(0, 46, 128, 46, 128, 0, 0, 0)
    elif eval("[/GetButtonExpr('ab')/]"):
        pass
    elif eval("[/GetButtonExpr('py')/]"):
        PagesManager.Main.Import('{}.apps.{}'.format(eval("[/Const('systemName')/]"), Core.Data.Get("list", "homePlug-in")[0]), "Main")
    elif eval("[/GetButtonExpr('on')/]"):
        PagesManager.Main.Import('{}.apps.{}'.format(eval("[/Const('systemName')/]"), Core.Data.Get("list", "homePlug-in")[1]), "Main")

def HomeomePlugInSet():
    while not button_a.is_pressed():
        options = DayLight.Select.Style4(["快捷启动1", "快捷启动2"], False, "桌面快捷启动")
        if options != None:
            DayLight.VastSea.Transition()
            set = DayLight.Select.Style1(Core.Data.Get("list", "localAppName"), 25, False, "选择")
            if set != None:
                Core.Data.Write("list", "homePlugIn", "app{}".format(str(set)), options)
                Message('好耶，设置成功')
                return True
            else:
                DayLight.VastSea.Transition(False)

def About():
    oled.fill(0)
    while not button_a.is_pressed():
        oled.Bitmap(16, 15, bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X3C,0X00,0X00,0X00,0X30, 0X00,0X00,0X00,0X70,0X00,0X78,0X00,0X03,0XFE,0X00,0X00,0X00,0X70,0X00,0X00,0X03, 0XFE,0X03,0XFE,0X00,0X07,0XFC,0X00,0X00,0X00,0X30,0X00,0X00,0X07,0X8F,0X07,0XFE, 0X00,0X06,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X0E,0X03,0X86,0X00,0X00,0X06,0X00, 0X0E,0X03,0XE0,0X20,0X38,0X01,0X8C,0X01,0X8E,0X00,0X00,0X0E,0X00,0X3F,0X87,0XF8, 0X71,0XFE,0X0F,0X98,0X00,0XCE,0X00,0X00,0X0F,0X00,0X7B,0XC7,0XFC,0X71,0XFF,0X1F, 0X98,0X00,0XCE,0X00,0X00,0X07,0XF0,0X60,0XCE,0X0C,0X63,0X83,0X18,0X18,0X00,0XC7, 0XF0,0X00,0X03,0XFC,0XE0,0XCE,0X0C,0X63,0X03,0X38,0X18,0X00,0XC3,0XFC,0X00,0X00, 0X1C,0XFF,0XCE,0X0C,0X63,0X03,0X38,0X18,0X00,0XC0,0X1C,0X00,0X00,0X0C,0XFF,0XCC, 0X0C,0X67,0X03,0X30,0X18,0X00,0XC0,0X0C,0X00,0X00,0X0C,0XC0,0X0C,0X0C,0X67,0X03, 0X30,0X0C,0X01,0XC0,0X0C,0X00,0X00,0X1C,0XC0,0X0C,0X1C,0XE7,0X07,0X30,0X0E,0X03, 0X80,0X1C,0X00,0X00,0X3C,0XE0,0X0C,0X1C,0XE7,0X8E,0X30,0X07,0X8F,0X00,0X3C,0X00, 0X1F,0XF8,0X7F,0X8C,0X1C,0XE3,0XFE,0X30,0X03,0XFE,0X1F,0XF8,0X00,0X1F,0XE0,0X3F, 0X8C,0X18,0XC1,0XF8,0X30,0X00,0XF8,0X1F,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00, 0X00,0X00,0X00,0X00,]), 98, 20, 1)
        version = 'V' + eval("[/Const('version')/]")
        DayLight.Text(version, DayLight.AutoCenter(version), 40, 3)
        oled.show()
        if eval("[/GetButtonExpr('on')/]"):
            DayLight.VastSea.Transition()
            FTReader.Textreader(Core.Data.GetOriginal('Hello_World')).Main()
            DayLight.VastSea.Transition(False)

def Wlanscan():
    #定义扫描WiFi函数
    import network
    wlan = network.WLAN()#定义类
    wlan.active(True)#打开
    return [i[0].decode() for i in network.WLAN().scan()]#返回

def Choosewifi() -> bool:
    while not button_a.is_pressed():
        oled.fill(0)
        wifiList = Wlanscan()
        num = DayLight.Select.Style4(wifiList, False, "请选择")
        if num == None:
            DayLight.VastSea.Transition(False)
            return
        wifiName = wifiList[num]
        wifiPassword = Typer.main()
        Quit = Core.SharedVar.LoadQuit()
        Quit.value = False
        _thread.start_new_thread(LoadWait,(Quit, "正在尝试建立连接", True))
        try:
            wifi.connectWiFi(wifiName, wifiPassword)
            Core.Data.Write('list', 'wifiName', wifiName)
            Core.Data.Write('list', 'wifiPassword', wifiPassword)
            Quit.value = True
            Message('好耶，添加成功')
            return True
        except:
            Quit.value = True
            Message('添加失败')
            return False
    
def Collect():
    oled.fill(0)
    DayLight.UITools()
    try:
        oled.DispChar(eval("[/Language('请稍等')/]"), 5, 5, 1)
        time.sleep_ms(5)
        oled.DispChar(eval("[/Language('正在进行操作')/]"), 5, 18, 1)
        oled.show()
        Core.FullCollect()
        oled.DispChar(eval("[/Language('加载成功')/]"), 5, 45, 1)
        time.sleep_ms(5)
        oled.show()
        return True
    except:
        oled.DispChar(eval("[/Language('加载失败')/]"), 5, 45, 1)
        oled.show()

def Time():
    DayLight.UITools()
    try:
        oled.fill(0)
        oled.DispChar(eval("[/Language('请稍等')/]"), 5, 5, 1)
        time.sleep_ms(5)
        oled.DispChar(eval("[/Language('正在进行操作')/]"), 5, 18, 1)
        oled.show()
        ntptime.settime(8, Core.Data.Get("text", "timingServer"))
        oled.DispChar(eval("[/Language('加载成功')/]"), 5, 45, 1)
        time.sleep_ms(5)
        oled.show()
        return True
    except:
        oled.DispChar(eval("[/Language('加载失败')/]"), 5, 45, 1)
        oled.show()

def ConnectWiFiMode():
    mode = ['预配置选择','自动连接预配置','SmartWiFi']
    oled.fill(0)
    while not button_a.is_pressed():
        options = DayLight.Select.Style4(mode, False, '网络连接方式')
        if options != None:
            Core.Data.Write('text', 'connectWifiMode', str(options))
            Message('好耶，设置成功')
        else:
            DayLight.VastSea.Transition(False)
            return

def LoadWait(WhetherToQuit:Core.SharedVar.LoadQuit, text:str="None", fill:bool=False):
    if fill:
        oled.fill(0)
    while not WhetherToQuit:
        if text != "None":
            DayLight.Text(text, DayLight.AutoCenter(text), 28, 2)
        DayLight.VastSea.SeniorMove.Line(0,63,0,63,0,63,128,63,False)
        DayLight.VastSea.SeniorMove.Line(0,63,128,63,128,63,128,63,False)
        oled.show()
    #_thread.exit() （会自动退出的）

def Message(text) -> bool:
    DayLight.Box(1, 1, 126, 62, True)
    oled.DispChar('消息', DayLight.AutoCenter('一个消息'), 5)
    DayLight.Text(text, 5, 24, 1)
    Log.Message(text)
    oled.show()
    time.sleep_ms(3000)
    return True