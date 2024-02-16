#from mpython import *
import ntptime
import network
import time
import os
import gc

# 适用于data下fos扩展名文件的信息读写操作
# 将大部分使用了init_file write_file类函数而只对data文件夹下的数据作读写的代码替换为此处代码
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
    m=gc.mem_free()
    while True:
        gc.collect()
        if m != gc.mem_free():
            m = gc.mem_free()
        else:
            return m

class Screenshot:
    def copyFramebuf():
        pass
    def screenshot(mode=4,path=False,RA=128,RB=64,RX=0,RY=0):
        if mode==1 and path!=False:print("[GxxkAPI]警告：模式一只会返回一个二位数组，path参数无法使用")
        if mode!=3 and (RA or RB or RX or RY):print("[GxxkAPI]警告：除模式三以外的模式均不需要标注")
        else:GxxkAPI_Error("截屏时启用除模式1以外的模式需要指定写入路径")
        # 方法1: 强行直接扫，速度快但是占用内存大- by Gxxk
        if mode==1:
            print("[GxxkAPI]尝试截取缓冲区内容用于截取屏幕内容（模式1-列表生成器，返回一个数组-By Gxxk-速度优先）")
            return [[oled.pixel(j,i) for j in range(128)] for i in range(64)]
        # 方法2：逐行扫描，逐行写入，慢但是占用资源小，掌控版可读取-By emo
        elif mode==2:
            if path==False:raise GxxkAPI_Error("截屏时启用模式2需要指定写入路径")
            print("[GxxkAPI]尝试逐列截取屏幕内容并写入至文件"+path+"内（模式2-无返回内容-By emo的程序大神-协议P1）")
            f=open(path,"w")
            f.write("P1\n#Screenshot\n128 64\n")
            for y in range(64):
                for x in range(0,127):
                    f.write(str(oled.pixel(x,y)))
                    f.write(" ")
                f.write(str(oled.pixel(127,y)))
                f.write("\n")
            f.write("#screenshot by emofalling")
            f.close()
        # 方法3：未知，写的有点玄乎，看不懂-可设定截屏范围-by LP
        elif mode==3:
            if path==False:raise GxxkAPI_Error("截屏时启用模式3需要指定写入路径和截图起始点（RX/RY），图片长/宽（RA/RB）")
            print("[GxxkAPI]尝试单像素截取屏幕内容并写入至文件"+path+"内（模式3-无返回内容-可设置截屏范围-By LP-协议P1）")
            file = open("screenshot.pbm","w")
            file.write("P1" + "\n" + RA + " " + RB + "\n")
            for i in range(int(RB)):
                for j in range(int(RA)):
                    file.write(str(oled.pixel(RX,RY)))
                    file.write(str(" "))
                    RX += 1
                file.write("\n")
                RY += 1
            file.write("#Screenshot by LP_OVERROR")
        # 史上最nb的截屏方法！真神奇！哈哈哈
        elif mode==4:
            if path==False:raise GxxkAPI_Error("截屏时启用模式4需要指定写入路径")
            print("[GxxkAPI]尝试逐列截取屏幕内容并以64像素点为单位写入进缓冲区内（模式4-无返回内容-速度/占用平衡-默认选项）")
            with open(path, 'wb') as f:
                f.write(b'P4\n128 64\n')
                for y in range(128):
                    row_data = bytearray(8) #缓冲区
                    for x in range(64):row_data[x//8]|=(oled.pixel(x, y)&1)<<7-(x%8) #循环 算偏移量 然后转格式 写到缓冲区内
                    f.write(row_data)
                f.write(b'# screenshot func by Gxxk')
        # 第三种的ram占用问题最优解（话说本来4and这个本来内存占用似乎就还行 30kb剩余都能截）
        elif mode==5:
            if path==False:raise GxxkAPI_Error("截屏时启用模式5需要指定写入路径")
            print("[GxxkAPI]尝试逐列截取屏幕内容（模式5-无返回内容-By ChatGPT&Gxxk-内存优先）")
            buffer = bytearray(1024)  # 创建缓冲区
            # 获取屏幕像素状态
            for y in range(64):
                for x in range(128):
                    pixel = oled.pixel(x, y)  # 获取屏幕像素状态
                    bit_pos = 7 - (x % 8)
                    buffer[x // 8 + y * (128 // 8)] |= (pixel & 1) << bit_pos  # 将像素状态写入缓冲区
            # 保存为PBM文件
            print("[GxxkAPI]尝试写入缓冲区内容")
            with open('screenshot.pbm', 'wb') as f:
                # 写入PBM文件头
                f.write(b'P4\n128 64\n')
                f.write(buffer)  # 将缓冲区数据写入PBM文件
                f.write(b'# screenshot func by Gxxk')