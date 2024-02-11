from mpython import *
import ntptime
import network
import time
import os

time_hour = 0
time_min = 0
sys_hour = 0
sys_min = 0

'''
# 闲话：DataCtrl和F＆P factory是瓦在外边旅游用十分鸡肋的蓝牙键盘在android手机上写的 有十分弱智的错误请在某个commit中偷偷改掉 plz（AidLinux倒还可以 有平板的可以试试 记得换一个对实体键盘兼容性高一点的输入法编码
# 这也是为什么这么多TODO的原因（）

# 适用于data下fos扩展名文件的信息读写操作
# TODO:将大部分使用了init_file write_file类函数而只对data文件夹下的数据作读写的代码替换为此处代码
class DataCtrl:
    def __init__(self,dataFolderPath):
        self.data={}
        self.dataFolderPath=dataFolderPath
        for i in os.listdir(dataFolderPath):
            with open(File_Path_Factory.JoinPath(dataFolderPath,i)),'w',encoding='utf-8')as f:
            	self.data[i]=f.read().strip('\r')
        # 反正几乎是内部API 所以编码 命名规则 换行符采用 自己手动改改（
    def Get(self,dataName):
        return self.data[dataName]
    def Write(self,dataName,dataValue,singleUseSet=False,needReboot=False):
        if singleUseSet: # singleUseSet参数:一次性设置 不会实际写入文件 此选参为True时 needReboot不生效
            self.data[dataName]=dataValue
            return
		with open(File_Path_Factory.JoinPath(self.dataFolderPath,dataName+'.fos'),'w',encoding='utf-8') as f:
            f.write(dataValue)   
        if not needReboot: #needReboot参数:当该值为True时 不修改实际运行值 特别适用于类似 开机需要根据config作init的程序使用
            self.data[dataName]=dataValue                 
        
# 文件/路径 格式工厂
class File_Path_Factory:

	# TODO:判断文件是否存在
	# 传入一绝对路径 返回1布尔值
	def FileIsExist(filePath):
    	...

	# TODO:判断路径指向的文件对象是否是目录
	# 传入一绝对路径 返回1布尔值
	def IsDir(filePath):
    	...

	# TODO:相对路径转绝对路径
	# dir是需要转化的路径 workDir是这个路径在执行代码是的路径 默认用os.getcwd获取
	def RelativePath2AbsPath(path,workDir=os.getcwd()):
        ...

	# TODO:链接两个路径
    # 两个参数 folderPath和filePath
    # 前者文件夹参数在于反斜杠和斜杠的统一
	def JoinPath(folderPath,filePath):
        ...
'''

def time_disposal():
    global time_hour, time_min, sys_hour, sys_min
    time_hour = str(time.localtime()[3])
    time_min = str(time.localtime()[4])
    sys_hour = str(time.localtime()[3])
    sys_min = str(time.localtime()[4])
    if len(sys_hour) < 2:
        time_hour = '0' + str(sys_hour)
    else:
        time_hour = sys_hour
    if len(sys_min) < 2:
        time_min = '0' + str(sys_min)
    else:
        time_min = sys_min

def init_file(_path):
    f = open(_path, 'w')
    f.close()

def get_file(_path, _sep):
    f = open(_path, 'r')
    result = f.read().split(_sep)
    f.close()
    return result

def write_file(_path, _data, _sep):
    f = open(_path, 'a')
    f.write(_data + _sep)
    f.close()

def full_collect():
    # 反复进行collect函数直至达到极限
    # 此代码来自 TaoLiSystem
    m = gc.mem_free()
    n = 3
    gc.collect()
    while n > 0:
        if m == gc.mem_free():
            gc.collect()
            n -= 1
        else:
            m = gc.mem_free()
            gc.collect()
            n = 3
    return m