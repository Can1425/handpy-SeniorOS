# FTReader - by LP_OVER
# Copyright (c) 2024 LP_OVER
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from SeniorOS.system.devlib import *
import SeniorOS.system.core as Core
import SeniorOS.system.daylight as DayLight
import os
import gc,sys
import SeniorOS.system.log_manager as LogManager
Log = LogManager.Log

class animations:
    def ClearFromLeftSide(mode:bool = True):
        if mode:
            for i in range(13):
                times = i * i
                oled.vline(times, 0, 64, 1)
                oled.vline(times+1, 0, 64, 0)
                oled.fill_rect(0, 0, times, 64, 0)
                oled.show()
        else:
            for i in range(13):
                times = 13 - i
                times_squared = times * times
                oled.fill_rect(0, 0, 128, 64, 0)
                oled.vline(times_squared, 0, 64, 1)
                oled.vline(times_squared + 1, 0, 64, 0)
                oled.show()
    def textMove(text):
        Core.FullCollect()
        total=156
        for i in range(7):
            oled.fill_rect(total,0,128,16,0)
            oled.vline(total-1,2,12,1)
            oled.DispChar(text,total+1,0)
            total=total-((7-i)**2)
            oled.show()
    def lineMove():
        i=0
        for _ in range(7):
            oled.fill_rect(0,(64-i),128,64,0)
            oled.hline(49,(66-i),30,1)
            oled.show()
            i+=(64-i)//2
        oled.fill_rect(0,0,128,64,0)
        oled.hline(49,2,30,1)
        oled.show()
    def boxMove(text):
        boxlong=17+(len(text)*8)
        xb=128-boxlong
        yb=48
        for _ in range(7):
            oled.fill_rect(0,0,xb,yb,0)
            oled.rect(0,0,xb,yb,1)
            oled.show()
            xb=(128-xb)//2+xb
            yb=(64-yb)//2+yb
        oled.fill_rect(0,0,128,64,0)
        oled.rect(0,0,128,64,1)
        oled.show()
class picture:
    pathpic=bytearray([0X00,0X00,0X3E,0X00,0X41,0X00,0X80,0X80,0X81,0XFC,0XFE,0X02,0X80,0X01,0X80,0X01,0XFF,0XFF,0X80,0X01,0X80,0X01,0X80,0X01,0X80,0X01,0X80,0X01,0X40,0X02,0X3F,0XFC,])
    filepic=bytearray([0X00,0X00,0X3F,0XC0,0X20,0X60,0X2F,0X50,0X20,0X48,0X2F,0X7C,0X20,0X04,0X23,0XC4,0X22,0X04,0X23,0X84,0X22,0X04,0X22,0X04,0X22,0X04,0X20,0X04,0X3F,0XFC,0X00,0X00,])
    runpic=filepic
    picpic=bytearray([0XFF,0XFF,0X80,0X01,0X8C,0X01,0X92,0X01,0X92,0X09,0X8C,0X15,0X80,0X23,0X84,0X41,0X8A,0X81,0X91,0X01,0XA0,0X01,0XC0,0X01,0X80,0X01,0X80,0X01,0X80,0X01,0XFF,0XFF,])
class Textreader:
    def __init__(self, text, splitCfg="\n"):
        self.text = text.split(splitCfg)
    def showText(self,lines=0,offset=0,y=0):
        for i in [0,1,2]:
            try:oled.DispChar(self.text[i+lines],0-offset,i*16+y)
            except:continue
        return
    def text_info(self,info):
        if info:return int(len(self.text)/3)
        else:return len(self.text)%3
    
    def test2(self):
        self.showText()
        animations.ClearFromLeftSide()
            
    def Main(self):
        page_num=self.text_info(True)+self.text_info(False)
        n=0;offset=0
        while not (touchpad_t.is_pressed() or touchpad_h.is_pressed()):
            Core.FullCollect()
            oled.fill(0)
            self.showText(n,offset)
            oled.DispChar("<PY",0,48);oled.DispChar("ON>",104,48)
            oled.DispChar("{}/{}".format(int(n/3)+1,int(page_num)),52,48)
            oled.hline(0,48,128,1)
            oled.show()
            while not (touchpad_t.is_pressed() or touchpad_h.is_pressed()):
                if touchpad_p.is_pressed() or touchpad_y.is_pressed():
                    if n-3<0:n=0
                    else:n-=3
                    break
                elif touchpad_n.is_pressed() or touchpad_o.is_pressed():
                    if n+3>page_num*3:n=page_num*3
                    else:n+=3
                    break
                if button_b.is_pressed():
                    offset+=8
                    break
                elif button_a.is_pressed():
                    offset-=8
                    break


class FileViewer:
    def __init__(self):
        self.copy=""
    def Copy(self):
        self.copy=f"{path}/{self.Dir[num]}"
    def UseTextReader(self):
        global path,num
        with open("{}/{}".format(path,self.Dir[num]),"r") as f:
            readFile=Textreader(f.read())
            animations.ClearFromLeftSide()
            readFile.Main()
            readFile.test2()
        del readFile;gc.collect()
    def IsFile(self,f):
        if os.stat(f)[0]<20000:return "目录"
        else:return self.fileattribute(f)
    def fileattribute(self,f):
        last4=f[-4:]
        last3=f[-3:]
        if last3==".py":return "可执行文件"
        elif last4==".pbm" or last4==".bmp":return "图片"
        else:return "文件"
    def fileviewer(self,initpath:str):
        global path,num
        PictureMap={"目录":picture.pathpic,"文件":picture.filepic,
                    "可执行文件":picture.runpic,"图片":picture.picpic}
        path=initpath
        if path[:2]=="//":
            path=path[1:]
        def lastpath(path:str):
            return "/".join(path.split("/")[:-1])
        while not button_a.is_pressed():
            Core.FullCollect()
            self.Dir=os.listdir(path)
            self.Dir.append('..')
            TMPOFDDIRLEN=len(self.Dir)
            num=0
            while not button_a.is_pressed():
                t=self.IsFile("{}/{}".format(path,self.Dir[num]))
                oled.fill(0)
                oled.vline(16,2,12,1)
                oled.DispChar(self.Dir[num],18,0)
                oled.DispChar("属性:{}".format(t),0,16)
                oled.DispChar("TH)打开 B)其他方式",0,32)
                oled.DispChar("<PY          {}/{}          ON>".format(num+1,TMPOFDDIRLEN),1,48)
                oled.Bitmap(0,0,PictureMap[t],16,16,1)
                oled.hline(0,16,130,1)
                oled.show()
                while not button_a.is_pressed():
                    Core.FullCollect()
                    if button_b.is_pressed():
                        animations.boxMove("selset")
                        temp=["文本阅读器","复制","删除","粘贴"]
                        selset=DayLight.Select.Style4(temp, appTitle="选择操作")
                        def Delete():
                            fileORdir=f"{path}/{self.Dir[num]}"
                            if self.fileattribute(fileORdir)=="目录":
                                os.rmdir(fileORdir)
                            else:
                                os.remove(fileORdir)
                        def Paste():
                            if self.fileattribute(self.copy)=="目录":
                                print("[FileViewer/ERROR]目录暂时不支持粘贴")
                            else:
                                with open(self.copy,"r") as f:
                                    with open("{}/{}".format(path,self.copy),"w") as f2:
                                        f2.write(f.read())
                        mode = {
                            0: self.UseTextReader,
                            1: self.Copy,
                            2: Delete,
                            3: Paste,
                        }
                        if selset != None:
                            mode(selset)()
                            break
                        else:
                            DayLight.VastSea.Transition(False)
                            return
                    elif touchpad_t.is_pressed() or touchpad_h.is_pressed():
                        if self.Dir[num]=='..':
                            if path=="/":pass
                            path=lastpath(path)
                            self.Dir=os.listdir(path);num=0;TMPOFDDIRLEN=len(self.Dir)
                            animations.lineMove()
                        if t=="目录":
                            animations.boxMove(self.Dir[num])
                            path="{}/{}".format(path,self.Dir[num])
                            self.Dir=os.listdir(path);num=0;TMPOFDDIRLEN=len(self.Dir)
                        if t=="可执行文件":
                            libname=("{}/{}".format(path,self.Dir[num]))[:-3].replace("/",".")
                            while libname[0]==".":
                                libname=libname[1:]
                            try:
                                __import__(libname)
                                exec("del {}".format(libname));gc.collect()
                            except Exception as e:
                                print("导入失败，错误信息如下：\n",e.__class__.__name__,e)
                        if t=="图片":
                            animations.boxMove("image")
                            oled.fill(0)
                            oled.blit(Image().load('{}/{}'.format(path,self.Dir[num])), 0, 0)
                            oled.show()
                            while not (touchpad_t.is_pressed() or touchpad_h.is_pressed()):
                                pass
                            animations.lineMove()
                        if t=="文件":self.UseTextReader()
                        break
                    if touchpad_n.is_pressed() or touchpad_o.is_pressed():
                        try:
                            animations.textMove(self.Dir[num+1])
                        except:
                            animations.textMove(self.Dir[0])
                        num+=1
                        if num>=TMPOFDDIRLEN:num=0
                        break
                    elif touchpad_p.is_pressed() or touchpad_y.is_pressed():
                        try:
                            animations.textMove(self.Dir[num-1])
                        except:
                            animations.textMove(self.Dir[TMPOFDDIRLEN-1])
                        num-=1
                        if num<0:num=TMPOFDDIRLEN-1
                        break
        return 0
    #鸣谢名单
    #程序设计---LP_OVER/emofalling
    #界面设计---LP_OVER
    #bug修复/优化---emofalling
    #运行平台提供---W-Can1425

def Main():
    path='/'
    while not button_a.is_pressed():
        fileview=FileViewer()
        fileview.fileviewer(path)