print(eval("[/Const('systemRunLog')/]") + "system/core.mpy")
import time
import os
import sys
import framebuf
import network
import gc
import time
import urequests
import json
import SeniorOS
from machine import unique_id
from mpython import *

# 适用于 data/ 下 .sros 扩展名文件的信息读写操作
# 将大部分使用了 init_file write_file 类函数而只对 data 文件夹下的数据作读写的代码替换为此处代码

# 初始化函数
class DataCtrl:
    # 初始化函数，传入文件夹路径
    def __init__(self,dataFolderPath): # 文件夹传参结尾必须要有反斜杠！！！
        self.data={}
        self.dataFolderPath=dataFolderPath
        print(eval("[/Const('systemRunLog')/]") + "SystemData 初始化")
        eval("[/EnableDebugMsg('Core.DataCtrl.__init__')/]");print([f for f in os.listdir(dataFolderPath) if f.endswith('.sros')])
        for i in [f for f in os.listdir(dataFolderPath) if f.endswith('.sros')]:
            with open(dataFolderPath+i,'r',encoding='utf-8')as f:
                self.data[i.strip('.sros')]=f.read().strip('\r')
                eval("[/EnableDebugMsg('Core.DataCtrl.__init__')/]");print(self.data[i.strip('.sros')])
        # 反正几乎是内部API 所以编码 命名规则 换行符采用 自己手动改改（
        eval("[/EnableDebugMsg('Core.DataCtrl.__init__')/]")

    # 获取数据
    def GetOriginal(self,dataName):
        return self.data[dataName]
    # 写入数据
    def WriteOriginal(self,dataName,dataValue,singleUseSet=False,needReboot=False):
        if singleUseSet: # singleUseSet参数:一次性设置 不会实际写入文件 此选参为True时 needReboot不生效
            self.data[dataName]=dataValue
            return
        with open(self.dataFolderPath+dataName+'.sros','w',encoding='utf-8') as f:
            f.write(dataValue)
            self.data[dataName]=dataValue
        if not needReboot: #needReboot参数:当该值为True时 不修改实际运行值 特别适用于类似 开机需要根据config作init的程序使用
            self.data[dataName]=dataValue

    def Get(self, controls, dataName):
        if controls == "text":
            ConfigRead = Data.GetOriginal("text")
            Config=ConfigRead.split('\n')
            data=[]
            TSList2=[]
            for i in range(len(Config)):
                TSList1=Config[i].split(':')
                TSList2.append(TSList1[0])
                data.append(TSList1[1])
            try: index = TSList2.index(dataName)
            except: index = 0
            return data[index].strip("\r")
        if controls == "list":
            ConfigRead = Data.GetOriginal("list")
            Config=ConfigRead.split('\n')
            data=[]
            TSList2=[]
            for i in range(len(Config)):
                TSList1=Config[i].split(':')
                TSList2.append(TSList1[0])
                data.append(TSList1[1])
            try: index = TSList2.index(dataName)
            except: index = 0
            return data[index].split(';')
    def Write(self, controls, dataName, dataValue):
        if controls == "text":
            ConfigRead = Data.GetOriginal("text")
            Config=ConfigRead.split('\n')
            TSList2=[]
            for i in range(len(Config)):
                TSList1=Config[i].split(':')
                TSList2.append(TSList1[0])
            try: index = TSList2.index(dataName)
            except: index = 0
            Config[index] = dataName + ":" + dataValue
            
            with open(self.dataFolderPath + 'text' + '.sros','w') as f:
                f.write('\n'.join(Config))
                self.data[controls]='\n'.join(Config)
                print(Config)
            with open(self.dataFolderPath + 'text' + '.sros','r') as f:
                print(f.read())
            return

Data=DataCtrl("/SeniorOS/data/")

class File_Path_Factory:
    """
    处理文件和路径操作的工厂类。

    Methods:
        Replace2Backslash(path: str) -> str: 将路径中的斜杠替换为反斜杠。
        FileIsExist(filePath: str) -> bool: 检查文件是否存在。
        IsDir(filePath: str) -> bool: 判断路径指向的是否是目录。
    """
    @staticmethod
    def Replace2Backslash(path: str) -> str:
        """将路径中的斜杠替换为反斜杠。"""
        return path.replace("\\", "/")

    @staticmethod
    def FileIsExist(filePath: str) -> bool:
        """检查文件是否存在。"""
        filePath = File_Path_Factory.Replace2Backslash(filePath)
        return os.path.isfile(filePath)

    @staticmethod
    def IsDir(filePath: str) -> bool:
        """判断路径指向的是否是目录。"""
        try:
            return os.stat(filePath)[0] & 0o170000 == 0o040000
        except OSError:
            return False

class GetTime:
    """获取时间相关信息的静态类。"""
    @staticmethod
    def Year() -> int:
        """获取当前年份。"""
        return time.localtime()[0]

    @staticmethod
    def Month() -> int:
        """获取当前月份。"""
        return time.localtime()[1]

    @staticmethod
    def Week() -> int:
        """获取当前星期几（0-6）。"""
        return time.localtime()[6]

    @staticmethod
    def Day() -> int:
        """获取当前日期。"""
        return time.localtime()[2]

    @staticmethod
    def Hour() -> int:
        """获取当前小时。"""
        return time.localtime()[3]

    @staticmethod
    def Min() -> int:
        """获取当前分钟。"""
        return time.localtime()[4]

    @staticmethod
    def Sec() -> int:
        """获取当前秒数。"""
        return time.localtime()[5]

def FullCollect() -> int:
    """执行垃圾回收，直到内存不再变化，并返回最终的空闲内存大小。"""
    m = gc.mem_free()
    while True:
        gc.collect()
        if m != gc.mem_free():
            m = gc.mem_free()
        else:
            return m

def GetDeviceID(wifiStaObj: network.WLAN = network.WLAN(network.STA_IF), mode: int = 1) -> str:
    """
    获取设备唯一标识符（MAC地址或者唯一ID）。

    Returns:
        str: 设备唯一标识符。
    """
    if mode == 0:
        return str(wifiStaObj.config('mac'))[2:-1].replace("\\x", "")
    elif mode == 1:
        return str(unique_id())[2:-1].replace("\\x", "")

class Screenshot:
    """
    截图操作相关的静态类，支持不同的截图算法。

    Methods:
        CopyFramebuf(path: str, oledObj) -> None: 复制帧缓冲区数据到文件。
        Enumerate(path: str, oledObj) -> None: 枚举缓冲区数据并保存到文件，支持两种算法。
    """
    @staticmethod
    def CopyFramebuf(path: str, oledObj=__import__("mpython").oled) -> None:
        """
        复制帧缓冲区数据到文件。

        Args:
            path (str): 保存截图的文件路径。
            oledObj: 带有缓冲区的对象，默认为 mpython.oled。
        """
        buf = bytearray(128 * 64)
        with open(path, "wb") as f:
            f.write(b"P4\n128 64\n")
            buf = framebuf.FrameBuffer(buf, 128, 64, framebuf.MONO_HLSB)
            buf.blit(oledObj.buffer, 0, 0)
            f.write(buf)

    @staticmethod
    def Enumerate(path: str, oledObj=__import__("mpython").oled) -> None:
        """
        枚举缓冲区数据并保存到文件，支持两种算法。

        Args:
            path (str): 保存截图的文件路径。
            oledObj: 带有缓冲区的对象，默认为 mpython.oled。
        """
        if ConstData.screenMethod == "fast":
            with open(path, 'wb') as f:
                f.write(b'P4\n128 64\n')
                for y in range(128):
                    row_data = bytearray(8)
                    for x in range(64):
                        row_data[x // 8] |= (oledObj.pixel(x, y)) << 7 - (x % 8)
                    f.write(row_data)
        elif ConstData.screenMethod == "ram":
            buffer = bytearray(1024)
            for y in range(64):
                for x in range(128):
                    buffer[x // 8 + y * 16] |= oledObj.pixel(x, y) << 7 - (x % 8)
            with open('screenshot.pbm', 'wb') as f:
                f.write(b'P4\n128 64\n')
                f.write(buffer)  # 将缓冲区数据写入PBM文件

def Tree(path="/",prt=print,_tabs=0):
    lst=os.listdir(path)
    dirs=[]
    files=[]
    l=0
    for i in lst:
        pti=path+'/'+i
        if os.stat(pti)[0] & 0x4000:
            dirs.append(i)
        else:
            files.append(i)
        l+=1
    lk="├"
    ldirs=len(dirs)
    for n,i in enumerate(dirs+files,1):
        if n==l:
            lk="└"
        prt("│"*_tabs+lk+i)
        if n<ldirs:
            Tree(path+'/'+i,prt,_tabs+1)

class ModuleRunner:
    def __init__(self, modulePath):
        # 对 modulePath 进行处理，意味着你只需要填写模块所在的目录名称
        self.modulePath = eval("[/Const('systemName')/]") + '.' + modulePath +'.'
    def Load(self, moduleName, print=False):
        moduleName = self.modulePath + moduleName
        # 动态加载模块
        module = __import__(moduleName, globals(), locals(), -1)
        # print(module)
        if functionName == None:
            pass
        else:
            # print(functionName)
    def Run(self, moduleName, functionName=None):
            eval(moduleName + '.' + functionName + "()", globals(), locals())
