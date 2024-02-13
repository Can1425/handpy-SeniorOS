from mpython import *
import ntptime
import network
import time
import os
import gc

# 闲话：DataCtrl和F＆P factory是瓦在外边旅游用十分鸡肋的蓝牙键盘在android手机上写的 有十分弱智的错误请在某个commit中偷偷改掉 plz（AidLinux倒还可以 有平板的可以试试 记得换一个对实体键盘兼容性高一点的输入法编码
# 这也是为什么这么多TODO的原因（）

# 适用于data下fos扩展名文件的信息读写操作
# TODO:将大部分使用了init_file write_file类函数而只对data文件夹下的数据作读写的代码替换为此处代码
class DataCtrl:
    def __init__(self,dataFolderPath): # 文件夹传参结尾必须要有反斜杠！！！
        self.data={}
        self.dataFolderPath=dataFolderPath
        for i in os.listdir(dataFolderPath):
            with open(dataFolderPath+i,'w',encoding='utf-8')as f:
                self.data[i.strip('.fos')]=f.read().strip('\r')
        # 反正几乎是内部API 所以编码 命名规则 换行符采用 自己手动改改（
    def Get(self,dataName):
        return self.data[dataName]
    def Write(self,dataName,dataValue,singleUseSet=False,needReboot=False):
        if singleUseSet: # singleUseSet参数:一次性设置 不会实际写入文件 此选参为True时 needReboot不生效
            self.data[dataName]=dataValue
            return
        with open(self.dataFolderPath+dataName+'.fos','w',encoding='utf-8') as f:
            f.write(dataValue)   
        if not needReboot: #needReboot参数:当该值为True时 不修改实际运行值 特别适用于类似 开机需要根据config作init的程序使用
            self.data[dataName]=dataValue                 
        
# 文件/路径 格式工厂
class File_Path_Factory:

    # 将所有的斜杠替换为反斜杠 便于统一路径
    def Replace2Backslash(path):
        return path.replace("\\","/").split("/")

    # 判断文件是否存在
    # 传入一绝对路径 返回1布尔值
    def FileIsExist(filePath:str)->bool:
        filePath=File_Path_Factory.Format.Replace2Backslash(filePath)
        if filePath[-1] in os.listdir("/"+filePath[:-1]):return True
        else:return False

    # 判断路径指向的文件对象是否是目录
    # 传入一绝对路径 返回1布尔值
    def IsDir(filePath:str)->bool:
        # 检查st_mode(第一项)中文件类型位
        try:return os.stat(filePath)[0] & 0o170000 == 0o040000
        # 如异常代表路径无效或不是目录
        except:return False

# 获取日期 ByGxxk
class GetTime:
    Year=lambda:time.localtime()[0]
    Month=lambda:time.localtime()[1]
    Week=lambda:time.localtime()[6]
    Day =lambda:time.localtime()[2]
    Hour=lambda:time.localtime()[3]
    Min =lambda:time.localtime()[4]
    Sec =lambda:time.localtime()[5]


def FullCollect():
    # 反复进行collect函数直至达到极限
    # 此代码来自 TaoLiSystem
    # POLA 已优化此函数
    m = gc.mem_free()
    n = 3
    while n > 0:
    gc.collect()
    if m != gc.mem_free():
        m = gc.mem_free()
        n = 3
    else:
        n -= 1
    return m