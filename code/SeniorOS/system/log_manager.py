#######################################################################################
#   |                     \  |                                         
#   |       _ \    _` |  |\/ |   _` |  __ \    _` |   _` |   _ \   __| 
#   |      (   |  (   |  |   |  (   |  |   |  (   |  (   |   __/  |    
#  _____| \___/  \__, | _|  _| \__,_| _|  _| \__,_| \__, | \___| _|    
#                |___/                              |___/              
#    
# Log Manager
# For HandPy
# 
# By CycleBai
# Powered by:
# # SeniorOS
#
#######################################################################################

log_level_list = ['DEBUG', 'INFO', 'MSG', 'WARN', 'ERROR', 'FATAL']

import time
import gc

PYTHON = 'mpy' # 'cpy' or 'mpy'

def is_leap_year(year):
    # 闰年的判断规则
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def format_timestamp(timestamp, timezone_offset=0):
    #ready-to-delete
    '''
    # 定义每个月的天数
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 秒，分钟，小时，天的计算单位
    SECONDS_IN_A_MINUTE = 60
    SECONDS_IN_AN_HOUR = 3600
    SECONDS_IN_A_DAY = 86400
    SECONDS_IN_A_YEAR = 31536000
    SECONDS_IN_A_LEAP_YEAR = 31622400
    
    # 调整时间戳以考虑时区偏移
    timestamp += timezone_offset * SECONDS_IN_AN_HOUR
    
    # 从1970年1月1日开始的年份
    year = 1970
    seconds = int(timestamp)
    
    # 计算年份
    while True:
        if is_leap_year(year):
            if seconds >= SECONDS_IN_A_LEAP_YEAR:
                seconds -= SECONDS_IN_A_LEAP_YEAR
                year += 1
            else:
                break
        else:
            if seconds >= SECONDS_IN_A_YEAR:
                seconds -= SECONDS_IN_A_YEAR
                year += 1
            else:
                break
    
    # 更新二月的天数
    if is_leap_year(year):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    
    # 计算月份
    month = 0
    while seconds >= days_in_month[month] * SECONDS_IN_A_DAY:
        seconds -= days_in_month[month] * SECONDS_IN_A_DAY
        month += 1
    
    month += 1  # 月份从1开始
    
    # 计算天数
    day = seconds // SECONDS_IN_A_DAY + 1
    seconds %= SECONDS_IN_A_DAY
    
    # 计算小时
    hour = seconds // SECONDS_IN_AN_HOUR
    seconds %= SECONDS_IN_AN_HOUR
    
    # 计算分钟
    minute = seconds // SECONDS_IN_A_MINUTE
    seconds %= SECONDS_IN_A_MINUTE
    
    # 剩余的就是秒数
    second = seconds
    
    return f'{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'
    '''
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
        formatted_time = format_timestamp(nowTime, 8)
        return formatted_time


def logFormatReplace(formatText:str,message:str,prefix:str='#',level:str='INFO') -> str:
    formatText=formatText.replace(f'{prefix}level{prefix}', level)\
       .replace(f'{prefix}format_time{prefix}', getTime(True))\
       .replace(f'{prefix}time{prefix}', str(getTime()))\
       .replace(f'{prefix}message{prefix}', message)
    formatText+=f" mem-info:{gc.mem_free()} B"
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

Output(str(gc.mem_alloc()), "MSG")