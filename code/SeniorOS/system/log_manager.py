# LogManager
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

log_level_list = ['DEBUG', 'INFO', 'MSG', 'WARN', 'ERROR', 'FATAL']

import time
import gc
import ntptime
import esp32
PYTHON = 'mpy' # 'cpy' or 'mpy'


def format_timestamp():
    t=time.localtime()
    return f'{t[0]}-{t[1]}-{t[2]} {t[3]}:{t[4]}:{t[5]}'

def getTime(format: bool = False):
    if PYTHON == 'cpy':
        # time = __import__('time', globals(), locals(), [], 0)
        nowTime = int(time.time())
    else:
        # time = __import__('time', globals(), locals(), [], 0)
        nowTime = int(time.time())
    if not format:
        return nowTime
    else:
        formatted_time = format_timestamp()
        return formatted_time

ntp_is_connect=False
def logFormatReplace(formatText:str,message:str,prefix:str='#',level:str='INFO') -> str:
    formatText=formatText.replace(f'{prefix}level{prefix}', level)\
       .replace(f'{prefix}format_time{prefix}', getTime(True))\
       .replace(f'{prefix}time{prefix}', str(getTime()))\
       .replace(f'{prefix}message{prefix}', message)
    formatText+=f"\nRam-info:{gc.mem_free()} B\nCPU:{esp32.raw_temperature()}°C"
    return formatText

class LogManager:
    def __init__(self, log_level: str = 'INFO', log_prefix: str = '#', log_format: str = '[#level#] #format_time#: #message#') -> None:
        if log_level not in log_level_list:
            raise ValueError('Invalid log level. Must be one of DEBUG, INFO, MSG, WARN, ERROR, FATAL ERROR.')
        
        self.logFormat = log_format
        self.logPrefix = log_prefix
        self.minLogLevelIndex = log_level_list.index(log_level)

    def log(self, text: str, level: str = 'INFO'):
        if level not in log_level_list:
            raise ValueError('Invalid log level. Must be one of DEBUG, INFO, MSG, WARN, ERROR, FATAL ERROR.')
        
        if log_level_list.index(level) >= self.minLogLevelIndex:
            log = logFormatReplace(self.logFormat, text, self.logPrefix, level)
            print(eval("[/Const('log')/]") + log)

    def Info(self, text: str):
        self.log(text, 'INFO')
    
    def Debug(self, text: str):
        self.log(text, 'DEBUG')
    
    def Message(self, text: str):
        self.log(text, 'MSG')
    
    def Warn(self, text: str):
        self.log(text, 'WARN')
    
    def Error(self, text: str):
        self.log(text, 'ERROR')
    
    def Fatal(self, text: str):
        self.log(text, 'FATAL')

lm = LogManager()
Output = lm.log
Log = lm