from SeniorOS.lib.devlib import *
import SeniorOS.system.daylight as Daylight

class radient_UI:
    def GetToFile_UI():
        import SeniorOS.system.radient as radient
        while radient.ShareVar.ui.DownloadExit:
            if radient.ShareVar.ui.DownloadSpeed != None:
                if radient.ShareVar.ui.DownloadSpeed > 1024:
                    DownloadSpeed = str(radient.ShareVar.ui.DownloadSpeed/1024)+"KB/s / "+str(radient.ShareVar.ui.Downloadlength/1024)+"KB"
                else:
                    DownloadSpeed = str(radient.ShareVar.ui.DownloadSpeed)+"B/s / "+str(radient.ShareVar.ui.Downloadlength)+"B" 
            oled.fill(0)
            oled.DispChar(DownloadSpeed, Daylight.AutoCenter(DownloadSpeed), 24, 1)
            oled.show()
        oled.fill(0)

class SmartWifi_UI:
    def UI():
        oled.fill(0)
        oled.show()