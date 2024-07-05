import os
import framebuf
import network
import gc
import time
from machine import unique_id
from mpython import *

class DataCtrl:
    """
    控制数据操作的类，支持读取和写入特定格式文件（.fos）。

    Attributes:
        data (dict): 存储数据的字典。
        dataFolderPath (str): 数据文件夹路径。

    Methods:
        __init__(dataFolderPath: str): 初始化函数，读取所有 .fos 文件到内存。
        Get(dataName: str) -> str: 根据数据名称获取数据值。
        Write(dataName: str, dataValue: str, singleUseSet: bool = False, needReboot: bool = False) -> None:
            写入数据到文件，并更新内存中的数据值。
    """
    def __init__(self, dataFolderPath: str):
        self.data = {}
        self.dataFolderPath = dataFolderPath
        for file_name in os.listdir(dataFolderPath):
            if file_name.endswith('.fos'):
                with open(os.path.join(dataFolderPath, file_name), 'r', encoding='utf-8') as f:
                    self.data[file_name[:-4]] = f.read().strip('\r')

    def Get(self, dataName: str) -> str:
        """根据数据名称获取数据值。"""
        return self.data[dataName]

    def Write(self, dataName: str, dataValue: str, singleUseSet: bool = False, needReboot: bool = False) -> None:
        """
        写入数据到文件，并更新内存中的数据值。

        Args:
            dataName (str): 数据名称。
            dataValue (str): 数据值。
            singleUseSet (bool, optional): 是否只是临时设置数据，不写入文件。默认为False。
            needReboot (bool, optional): 是否需要重启后生效。默认为False。
        """
        if singleUseSet:
            self.data[dataName] = dataValue
            return
        with open(os.path.join(self.dataFolderPath, dataName + '.fos'), 'w', encoding='utf-8') as f:
            f.write(dataValue)
        if not needReboot:
            self.data[dataName] = dataValue

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
                f.write(buffer)
