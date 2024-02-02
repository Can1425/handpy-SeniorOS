from mpython import *
import flagos.system.pages
import ntptime
import network
import time
import os

time_hour = 0
time_min = 0
sys_hour = 0
sys_min = 0

def ui_app(Flag_sys_ui_app_title):
    global time_hour, time_min, sys_hour, sys_min
    time_disposal()
    oled.fill(0)
    if str(get_file('./flagos/data/Flag_sys_ui_light.fos', '\r\n')) == 'Open':
        oled.invert(1)
    else:
        oled.invert(0)
    oled.fill_rect(1, 0, 126, 16, 1)
    oled.DispChar(str((str(Flag_sys_ui_app_title))), 5, 0, 2)
    oled.DispChar(str((''.join([str(x) for x in [time_hour, ':', time_min]]))), 93, 0, 2)
    oled.hline(50, 62, 30, 1)

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

def consani(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, consani_start_x, consani_start_y, consani_start_wide, consani_start_height):
    if str(get_file('./flagos/data/Flag_sys_ui_light.fos', '\r\n')) == 'Open':
        oled.invert(1)
    else:
        oled.invert(0)
    try:
      consani_done_wait = 3
      oled.fill(0)
      for count in range(7):
          oled.RoundRect(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, 2, 1)
          oled.fill(0)
          consani_done_x = (consani_done_x - consani_start_x) // 2
          consani_done_y = (consani_done_y - consani_start_y) // 2
          consani_done_wide = (consani_start_wide + consani_done_wide) // 2
          consani_done_height = (consani_start_height + consani_done_height) // 2
          oled.RoundRect(consani_done_x, consani_done_y, consani_done_wide, consani_done_height, 2, 1)
          oled.show()
    except:
        oled.DispChar(str(' :( 我们遇到了一些问题，将在 3 秒后返回'), 5, 25, 1, True)
        oled.show()
        return
        
    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
        return
    time.sleep_ms(consani_done_wait)

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

def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

def FullCollect():
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

def about():
    print("Flag OS 2.0 (240202006[mXDF])")