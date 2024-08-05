#######################################################################################
#      \                        \  |                                         
#     _ \    __ \   __ \       |\/ |   _` |  __ \    _` |   _` |   _ \   __| 
#    ___ \   |   |  |   |      |   |  (   |  |   |  (   |  (   |   __/  |    
#  _/    _\  .__/   .__/      _|  _| \__,_| _|  _| \__,_| \__, | \___| _|    
#           _|     _|                                     |___/           
#    
# App Manager
# For HandPy
# 
# By CycleBai
# Powered by:
# # devlib
# # SeniorOS
#
#######################################################################################

class ScreenError(Exception):
    pass

class AppError(Exception):
    pass

class AppManager:
    def __init__(self, app_name) -> None:
        self.appName = app_name
        self.appScreen = {}
        self.appData = {}
    
    def genAppDataDump(self) -> dict:
        dump = {}
        dump['ScreenData'] = self.appScreen
        dump['AppData'] = self.appData
        dump['AppName'] = self.appName
        return dump
    
    def RestoringAppDataDump(self, dump) -> None:
        if 'ScreenData' not in dump or 'AppData' not in dump or 'AppName' not in dump:
            raise RuntimeError('The dump file is incomplete.')

        self.appName = dump['AppName']
        self.appData = dump['AppData']
        self.appScreen = dump['ScreenData']

    def regScreen(self, screenName: str, override: bool = False, extra: dict = {}) -> None:
        def doReg(func):
            if screenName in self.appScreen and not override:
                raise ScreenError('Illegal definition of duplicate ScreenName')
            else:
                self.appScreen[screenName] = {
                    "extraData": extra,
                    "screenFunc": func
                }
            return func
        return doReg
    
    def readScreenExtraData(self, screenName: str, fullDict: bool = False, dataName: str = '') -> object:
        if screenName not in self.appScreen:
            raise ScreenError('ScreenName has not been defined, but an attempt was made to read screen data.')
        if not fullDict and dataName == '':
            raise ScreenError('When trying to read screen data, fullDict is False and dataName is empty.')
        if fullDict and dataName != '':
            raise ScreenError('When trying to read screen data, both dataName and fullDict are defined.')
        
        if not fullDict:
            return self.appScreen[screenName]['extraData'][dataName]
        else:
            return self.appScreen[screenName]['extraData']
        
    def setScreenExtraData(self, screenName: str, dataName: str, data: object) -> bool:
        if screenName not in self.appScreen:
            raise ScreenError('ScreenName has not been defined, but an attempt was made to set screen data.')
        
        try: 
            self.appScreen[screenName]['extraData'][dataName] = data
            return True
        except Exception as e:
            raise ScreenError(f'An uncaught error occurred while trying to set screen data: {e}')
        
    def setAppExtraData(self, dataName: str, data: object) -> bool:
        try: 
            self.appData['extraData'][dataName] = data
            return True
        except Exception as e:
            raise ScreenError(f'An uncaught error occurred while trying to set app data: {e}')
        
    def readAppExtraData(self, fullDict: bool = False, dataName: str = '') -> object:
        if not fullDict and dataName == '':
            raise ScreenError('When trying to read app data, fullDict is False and dataName is empty.')
        if fullDict and dataName != '':
            raise ScreenError('When trying to read app data, both dataName and fullDict are defined.')
        
        if not fullDict:
            return self.appData['extraData'][dataName]
        else:
            return self.appData['extraData']
    
    def setAppEntryPoint(self, override: bool = False) -> function:
        def setEntryPoint(func):
            if 'EntryPoint' in self.appData and not override:
                raise AppError('The application entry point is already set and cannot be redefined unless the override property is set to True.')
            
            self.appData['EntryPoint'] = func
        
        return setEntryPoint

    def changeScreen(self, screenName: str):
        if screenName not in self.appScreen:
            raise ScreenError('ScreenName has not been defined, but an attempt was made to change screen.')
        self.appScreen[screenName]['screenFunc']()

    def Run(self) -> None:
        if 'EntryPoint' not in self.appData:
            raise AppError('The application entry point was not set before running the application.')
        else:
            try:
                self.appData['EntryPoint']()
            except Exception as e:
                raise AppError(f'An uncaught error was encountered during application execution: {e}')