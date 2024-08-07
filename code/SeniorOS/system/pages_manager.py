# PagesManager
# Copyright (C) 2024 CycleBai
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import SeniorOS.system.log_manager as LogManager

def DynamicImport(module_name, class_name):
    module_spec = __import__(module_name, fromlist=[class_name])
    return getattr(module_spec, class_name)

class ScreenError(Exception):
    pass

class PagesError(Exception):
    pass

class main:
    def __init__(self, pages_name) -> None:
        self.pagesName = pages_name
        self.pagesScreen = {}
        self.pagesData = {}
    
    def genPagesDataDump(self) -> dict:
        dump = {}
        dump['ScreenData'] = self.pagesScreen
        dump['PagesData'] = self.pagesData
        dump['PagesName'] = self.pagesName
        return dump
    
    def RestoringPagesDataDump(self, dump) -> None:
        if 'ScreenData' not in dump or 'PagesData' not in dump or 'PagesName' not in dump:
            LogManager.Output(self.pagesName + " > RuntimeError: The dump file is incomplete.","ERROR")
            return

        self.pagesName = dump['PagesName']
        self.pagesData = dump['PagesData']
        self.pagesScreen = dump['ScreenData']

    def regScreen(self, screenName: str, override: bool = False, extra: dict = {}) -> None:
        def doReg(func):
            if screenName in self.pagesScreen and not override:
                LogManager.Output(self.pagesName + " > ScreenError: Illegal definition of duplicate ScreenName.", "ERROR")
                return func
            else:
                self.pagesScreen[screenName] = {
                    "extraData": extra,
                    "screenFunc": func
                }
            return func
        return doReg
    
    def readScreenExtraData(self, screenName: str, fullDict: bool = False, dataName: str = '') -> object:
        if screenName not in self.pagesScreen:
            LogManager.Output(self.pagesName + " > ScreenError: ScreenName has not been defined, but an attempt was made to read screen data.", "ERROR")
            return None
        if not fullDict and dataName == '':
            LogManager.Output(self.pagesName + " > ScreenError: When trying to read screen data, fullDict is False and dataName is empty.", "ERROR")
            return None
        if fullDict and dataName != '':
            LogManager.Output(self.pagesName + " > ScreenError: When trying to read screen data, both dataName and fullDict are defined.", "ERROR")
            return None
        
        if not fullDict:
            return self.pagesScreen[screenName]['extraData'][dataName]
        else:
            return self.pagesScreen[screenName]['extraData']
        
    def setScreenExtraData(self, screenName: str, dataName: str, data: object) -> bool:
        if screenName not in self.pagesScreen:
            raise ScreenError('ScreenName has not been defined, but an attempt was made to set screen data.')
        
        try: 
            self.pagesScreen[screenName]['extraData'][dataName] = data
            return True
        except Exception as e:
            raise ScreenError(f'An uncaught error occurred while trying to set screen data: {e}')
        
    def setPagesExtraData(self, dataName: str, data: object) -> bool:
        try: 
            self.pagesData['extraData'][dataName] = data
            return True
        except Exception as e:
            raise ScreenError(f'An uncaught error occurred while trying to set pages data: {e}')
        
    def readPagesExtraData(self, fullDict: bool = False, dataName: str = '') -> object:
        if not fullDict and dataName == '':
            raise ScreenError('When trying to read pages data, fullDict is False and dataName is empty.')
        if fullDict and dataName != '':
            raise ScreenError('When trying to read pages data, both dataName and fullDict are defined.')
        
        if not fullDict:
            return self.pagesData['extraData'][dataName]
        else:
            return self.pagesData['extraData']
    
    def setPagesEntryPoint(self, override: bool = False) -> function:
        def setEntryPoint(func):
            if 'EntryPoint' in self.pagesData and not override:
                raise PagesError('The pageslication entry point is already set and cannot be redefined unless the override property is set to True.')
            
            self.pagesData['EntryPoint'] = func
        
        return setEntryPoint

    def changeScreen(self, screenName: str):
        if screenName not in self.pagesScreen:
            raise ScreenError('ScreenName has not been defined, but an attempt was made to change screen.')
        self.pagesScreen[screenName]['screenFunc']()

    def Run(self) -> None:
        if 'EntryPoint' not in self.pagesData:
            raise PagesError('The pageslication entry point was not set before running the pageslication.')
        else:
            try:
                self.pagesData['EntryPoint']()
            except Exception as e:
                raise PagesError('An uncaught error was encountered during pageslication execution: {}'.format(e))
