# FTReader - by LP_OVER
# Copyright (c) 2024 LP_OVER
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from SeniorOS.system.devlib import *
import SeniorOS.system.core as Core
import os
import gc
import time
class animations:
    def clearFromLeftSide():
        for i in range(13):
            times = i * i
            oled.vline(times, 0, 64, 1)
            oled.vline(times+1, 0, 64, 0)
            oled.fill_rect(0, 0, times, 64, 0)
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
            except:return
            return
    def text_info(self,info):
        if info == "len":
            return int(len(self.text)/3)
        elif info == "len3":
            return len(self.text)%3
    
    def test2(self):
        self.showText()
        animations.clearFromLeftSide()
            
    def Main(self):
        page_num=self.text_info("len")+self.text_info("len3")
        n=0;offset=0
        while not (touchpad_t.is_pressed() or touchpad_h.is_pressed()):
            Core.FullCollect()
            oled.fill(0)
            self.showText(n,offset)
            oled.DispChar("<PY",0,48);oled.DispChar("ON>",104,48)
            oled.DispChar("{}/{}".format(int(n/3),int(page_num/3)),52,48)
            oled.hline(0,48,128,1)
            oled.show()
            while not (touchpad_t.is_pressed() or touchpad_h.is_pressed()):
                if touchpad_p.is_pressed() or touchpad_y.is_pressed():
                    if n-3<0:
                        n=0
                    else:
                        n-=3
                    break
                elif touchpad_n.is_pressed() or touchpad_o.is_pressed():
                    if n+3>page_num:
                        n=page_num#-self.text_info("len3")
                    else:
                        n+=3
                    break
                if button_a.is_pressed():
                    offset+=8
                    if offset > 512:
                        offset = 512
                    break
                elif button_b.is_pressed():
                    offset-=8
                    if offset < 0:
                        offset = 0
                    break

class FileViewer:
    def __init__(self):
        self.copy=""
    def IsFile(self,f):
        if os.stat(f)[0]<20000:return "目录"
        else:
            return self.fileattribute(f)
    def fileattribute(self,f):
        last4=f[-4:]
        last3=f[-3:]
        if last3==".py":
            return "可执行文件"
        elif last4==".pbm" or last4==".bmp":
            return "图片"
        else:
            return "文件"
    def selsetbox(self,textlist:str):
        selsetlist=textlist.split(";")
        selset_num=0
        while not button_a.is_pressed():
            oled.fill(0)
            Textreader(textlist,";").showText(offset=-4)
            oled.rect(2,(selset_num*16),oled.DispChar(selsetlist[selset_num],0,0,Colormode.noshow)[0][0]+2,16,1)
            oled.show()
            if touchpad_p.is_pressed():
                if selset_num+1>len(selsetlist)-1:
                    selset_num=len(selsetlist)-1
                else:
                    selset_num+=1
            elif touchpad_n.is_pressed():
                if selset_num-1<0:selset_num=0
                else:
                    selset_num-=1
            time.sleep(0.1)
        return selsetlist[selset_num]
    def fileviewer(self,initpath:str):
        path=initpath
        if path[:2]=="//":
            path=path[1:]
        def lastpath(path:str):
            return "/".join(path.split("/")[:-1])
        while not button_a.is_pressed():
            Core.FullCollect()
            Dir=os.listdir(path)
            DIRlen=len(Dir)
            num=0
            while not button_a.is_pressed():
                t=self.IsFile("{}/{}".format(path,Dir[num]))
                oled.fill(0)
                oled.vline(16,2,12,1)
                oled.DispChar(Dir[num],18,0)
                oled.DispChar("属性:{}".format(t),0,16)
                oled.DispChar("B)默认打开 O)其他方式",0,32)
                oled.DispChar("<P           {}/{}           N>".format(num+1,DIRlen),1,48)
                if t=="目录":
                    oled.Bitmap(0, 0,picture.pathpic, 16, 16, 1)
                elif t=="文件":
                    oled.Bitmap(0,0,picture.filepic,16,16,1)
                elif t=="可执行文件":
                    oled.Bitmap(0,0,picture.runpic,16,16,1)
                elif t=="图片":
                    oled.Bitmap(0,0,picture.picpic,16,16,1)
                oled.hline(0,16,130,1)
                oled.show()
                while not button_a.is_pressed():
                    Core.FullCollect()
                    if touchpad_t.is_pressed() or touchpad_h.is_pressed():
                        if path=="/":
                            break
                        path=lastpath(path)
                        Dir=os.listdir(path);num=0;DIRlen=len(Dir)
                        animations.lineMove()
                        break
                    elif touchpad_o.is_pressed():
                        animations.boxMove("selset")
                        selset=self.selsetbox("文本阅读器;复制;删除;粘贴")
                        if selset=="文本阅读器":
                            with open("{}/{}".format(path,Dir[num]),"r") as f:
                                readFile=Textreader(f.read())
                                animations.clearFromLeftSide()
                                readFile.main()
                                readFile.test2()
                            del readFile;gc.collect()
                        elif selset=="复制":
                            self.copy=f"{path}/{Dir[num]}"
                        elif selset=="删除":
                            fileORdir=f"{path}/{Dir[num]}"
                            if self.fileattribute(fileORdir)=="目录":
                                os.rmdir(fileORdir)
                            else:
                                os.remove(fileORdir)
                        elif selset=="粘贴":
                            if self.fileattribute(self.copy)=="目录":
                                print("[FileViewer/ERROR]目录暂时不支持粘贴")
                            else:
                                with open(self.copy,"r") as f:
                                    with open("{}/{}".format(path,self.copy),"w") as f2:
                                        f2.write(f.read())
                        break
                    elif button_b.is_pressed():
                        if t=="目录":
                            animations.boxMove(Dir[num])
                            path="{}/{}".format(path,Dir[num])
                            Dir=os.listdir(path);num=0;DIRlen=len(Dir)
                            break
                        elif t=="文件":
                            with open("{}/{}".format(path,Dir[num]),"r") as f:
                                readFile=Textreader(f.read())
                                animations.clearFromLeftSide()
                                readFile.main()
                                readFile.test2()
                        elif t=="可执行文件":
                            libname=("{}/{}".format(path,Dir[num]))[:-3].replace("/",".")
                            while libname[0]==".":
                                libname=libname[1:]
                            try:
                                __import__(libname)
                                exec("del {}".format(libname));gc.collect()
                            except Exception as e:
                                print("导入失败，错误信息如下：\n",e.__class__.__name__,e)
                        elif t=="图片":
                            animations.boxMove("image")
                            oled.fill(0)
                            image_picture = Image()
                            oled.blit(image_picture.load('{}/{}'.format(path,Dir[num])), 0, 0)
                            oled.show()
                            while not (touchpad_t.is_pressed() or touchpad_h.is_pressed()):
                                pass
                            animations.lineMove()
                        break
                    if touchpad_n.is_pressed():
                        try:
                            animations.textMove(Dir[num+1])
                        except:
                            animations.textMove(Dir[0])
                        num+=1
                        if num>=DIRlen:num=0
                        break
                    elif touchpad_p.is_pressed():
                        try:
                            animations.textMove(Dir[num-1])
                        except:
                            animations.textMove(Dir[DIRlen-1])
                        num-=1
                        if num<0:num=DIRlen-1
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