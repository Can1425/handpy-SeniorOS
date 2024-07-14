import time
import os
import framebuf
import network
import gc
from machine import unique_id
from mpython import *

class DataCtrl:
    # 初始化函数，传入文件夹路径
    def __init__(self,dataFolderPath): # 文件夹传参结尾必须要有反斜杠！！！
        self.data={}
        self.dataFolderPath=dataFolderPath
        eval("[/EnableDebugMsg('Core.DataCtrl.__init__')/]");print([f for f in os.listdir(dataFolderPath) if f.endswith('.sros')])
        for i in [f for f in os.listdir(dataFolderPath) if f.endswith('.sros')]:
            with open(dataFolderPath+i,'r',encoding='utf-8')as f:
                self.data[i.strip('.sros')]=f.read().strip('\r')
                eval("[/EnableDebugMsg('Core.DataCtrl.__init__')/]");print(self.data[i.strip('.sros')])
        # 反正几乎是内部API 所以编码 命名规则 换行符采用 自己手动改改（
        eval("[/EnableDebugMsg('Core.DataCtrl.__init__')/]");print(self.data)
    # 获取数据
    def Get(self,dataName):
        return self.data[dataName]   
DataOperation=DataCtrl("/SeniorOS/data/variable/")