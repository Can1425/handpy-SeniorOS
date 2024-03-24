import time
import os
import framebuf
from machine import unique_id
# --SystemUniRuntime--
eval('[/hashtag/]');gc=gc;wifi=wifi;oled=oled
# --SystemUniRuntime--

# 适用于data下fos扩展名文件的信息读写操作
# 将大部分使用了init_file write_file类函数而只对data文件夹下的数据作读写的代码替换为此处代码
# 初始化函数
class DataCtrl:
    # 初始化函数，传入文件夹路径
    def __init__(self,dataFolderPath): # 文件夹传参结尾必须要有反斜杠！！！
        self.data={}
        self.dataFolderPath=dataFolderPath
        for i in [f for f in os.listdir(dataFolderPath) if f.endswith('.fos')]:
            with open(dataFolderPath+i,'w',encoding='utf-8')as f:
                self.data[i.strip('.fos')]=f.read().strip('\r')
        # 反正几乎是内部API 所以编码 命名规则 换行符采用 自己手动改改（
        #print(self.data)
    # 获取数据
    def Get(self,dataName):
        with open("/SeniorOS/data/{}.fos".format(dataName),'r') as f:
            return f.read()
    # 写入数据
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
        return path.replace("\\","/")

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
    Hour=time.localtime()[3]
    Min =time.localtime()[4]
    Sec =lambda:time.localtime()[5]
    if len(str(Hour)) < 2:
        Hour = '0' + str(Hour)
    else:
        Hour = lambda:time.localtime()[3]
    if len(str(Min)) < 2:
        Min = '0' + str(Min)
    else:
        Min = lambda:time.localtime()[4]

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


def FullCollect():
    # 反复进行collect函数直至达到极限
    # 此代码来自 TaoLiSystem
    m=gc.mem_free()
    while True:
        gc.collect()
        if m != gc.mem_free():
            m = gc.mem_free()
        else:
            return m

# 获取设备ID
def GetDeviceID(mode=0):
    if mode==0:return "".join(str(wifi.sta.config('mac'))[2:len(str(wifi.sta.config('mac')))-1].split("\\x"))
    elif mode==1:return "".join(str(unique_id())[2:len(str(unique_id()))-1].split("\\x"))

# 支持2算法的截图
# 分别为 直接复制缓冲区数据(CopyFrameBuf) 和 枚举缓冲区数据(Enumerate)
# 在Enumerate中 又细分为 速度优先(fast) 与 内存占用最小(ram)
# 这里Enumerate部分使用的算法取决于构建阶段 对本代码作EXPR操作时 constData["screenMethod"] 的值是 fast 还是 ram
class Screenshot:
    def CopyFramebuf(path):
        bufb=bytearray(128*64)
        with open(path,"wb")as f:
            f.write(b"P4\n128 64\n")
            buf=framebuf.FrameBuffer(bufb,128,64,framebuf.MONO_HLSB)
            buf.blit(oled.buffer,0,0)
            f.write(bufb)
    def Enumerate(path):
        # 史上最nb的截屏方法！真神奇！哈哈哈
        if eval("[/Const('screenshotMethod')/]")=="fast":
            with open(path, 'wb') as f:
                f.write(b'P4\n128 64\n')
                for y in range(128):
                    row_data = bytearray(8) #缓冲区
                    for x in range(64):row_data[x//8]|=(oled.pixel(x, y))<<7-(x%8) #循环 算偏移量 然后转格式 写到缓冲区内
                    f.write(row_data)
        elif eval("[/Const('screenshotMethod')/]")=="ram":
            buffer = bytearray(1024)  # 创建缓冲区
            # 获取屏幕像素状态
            for y in range(64):
                for x in range(128):
                    buffer[x//8+y*16]|=oled.pixel(x,y)<<7-(x%8)
            # 保存为PBM文件
            with open('screenshot.pbm', 'wb') as f:
                # 写入PBM文件头
                f.write(b'P4\n128 64\n')
                f.write(buffer)  # 将缓冲区数据写入PBM文件