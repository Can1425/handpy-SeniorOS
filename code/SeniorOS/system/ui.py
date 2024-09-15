from SeniorOS.lib.devlib import *
import SeniorOS.system.daylight as Daylight

class radient_UI:
    def GetToFile_UI():
        import SeniorOS.system.radient as radient
        while radient.ShareVar.ui.DownloadExit:
            DownloadSpeed = str(radient.ShareVar.ui.DownloadSpeed)+"Bytes/s"
            oled.fill(0)
            oled.DispChar(DownloadSpeed, Daylight.AutoCenter(DownloadSpeed), 24, 1)
            oled.show()
        oled.fill(0)