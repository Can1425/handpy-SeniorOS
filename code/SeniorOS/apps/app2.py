import SeniorOS.system.ftreader as FTReader
import SeniorOS.system.pages_manager as PagesManager

Manager = PagesManager.main('apps/app2.mpy')

@Manager.regScreen('AppMain')
@Manager.setAppEntryPoint()
def Main():
    FTReader.main