from mpython import*
import os
import gc
class Textreader:
    def __init__(self, text, splitCfg="\n"):
        self.text = text.split(splitCfg)
    def showText(self,lines=0):
        for i in [0,1,2]:
            try:
                oled.DispChar(self.text[i+lines],0,i*16)
            except:
                oled.DispChar(" ",0,i*16)
    def text_info(self,info):
        if info == "len":
            return int(len(self.text)/3)
        elif info == "len3":
            return len(self.text)%3
    def main(self):
        page_num=self.text_info("len")+self.text_info("len3")
        n=0
        while not button_a.is_pressed():
            gc.collect()
            oled.fill(0)
            self.showText(n)
            oled.DispChar("<PY",0,48);oled.DispChar("ON>",104,48)
            oled.DispChar("{}/{}".format(int(n/3),int(page_num/3)),52,48)
            oled.hline(0,48,128,1)
            oled.show()
            if touchpad_p.is_pressed() or touchpad_y.is_pressed():
                if n-3<0:
                    n=0
                else:
                    n-=3
            elif touchpad_n.is_pressed() or touchpad_o.is_pressed():
                if n+3>page_num:
                    n=page_num#-self.text_info("len3")
                else:
                    n+=3
class FileViewer:
    def __init__(self):
        self.pathpic=bytearray([0X00,0X00,0X3E,0X00,
                            0X41,0X00,0X80,0X80,
                            0X81,0XFC,0XFE,0X02,
                            0X80,0X01,0X80,0X01,
                            0XFF,0XFF,0X80,0X01,
                            0X80,0X01,0X80,0X01,
                            0X80,0X01,0X80,0X01,
                            0X40,0X02,0X3F,0XFC,])
        self.filepic=bytearray([0X00,0X00,0X3F,0XC0,
                0X20,0X60,0X2F,0X50,
                0X20,0X48,0X2F,0X7C,
                0X20,0X04,0X23,0XC4,
                0X22,0X04,0X23,0X84,
                0X22,0X04,0X22,0X04,
                0X22,0X04,0X20,0X04,
                0X3F,0XFC,0X00,0X00,])
        self.runpic=bytearray([0X00,0X00,0X3F,0XC0,
                0X20,0X60,0X2F,0X50,
                0X20,0X48,0X2F,0X7C,
                0X20,0X04,0X23,0XC4,
                0X22,0X04,0X23,0X84,
                0X22,0X04,0X22,0X04,
                0X22,0X04,0X20,0X04,
                0X3F,0XFC,0X00,0X00,])
        self.picpic=bytearray([0XFF,0XFF,0X80,0X01,
                0X8C,0X01,0X92,0X01,
                0X92,0X09,0X8C,0X15,
                0X80,0X23,0X84,0X41,
                0X8A,0X81,0X91,0X01,
                0XA0,0X01,0XC0,0X01,
                0X80,0X01,0X80,0X01,
                0X80,0X01,0XFF,0XFF,])
    def IsFile(self,f):
        print(f)
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

    def fileviewer(self,initpath:str):
        path=initpath
        if path[:2]=="//":
            path=path[1:]
        Pathpic=self.pathpic
        Filepic=self.filepic
        Runpic=self.runpic
        Picpic=self.picpic
        def lastpath(path:str):
            return "/".join(path.split("/")[:-1])
        while True:
            gc.collect()
            Dir=os.listdir(path)
            DIRlen=len(Dir)
            num=0
            while not button_a.is_pressed():
                t=self.IsFile("{}/{}".format(path,Dir[num]))
                oled.fill(0)
                oled.DispChar(Dir[num],16,0)
                oled.DispChar("属性:{}".format(t),0,16)
                oled.DispChar("B)默认打开 O)文本打开",0,32)
                oled.DispChar("<P           {}/{}           N>".format(num+1,DIRlen),1,48)
                if t=="目录":
                    oled.Bitmap(0, 0,Pathpic, 16, 16, 1)
                elif t=="文件":
                    oled.Bitmap(0,0,Filepic,16,16,1)
                elif t=="可执行文件":
                    oled.Bitmap(0,0,Runpic,16,16,1)
                elif t=="图片":
                    oled.Bitmap(0,0,Picpic,16,16,1)
                oled.hline(0,16,130,1)
                oled.show()
                if touchpad_t.is_pressed() or touchpad_h.is_pressed():
                    if path=="/":
                        #print("已经是根目录")
                        continue
                    path=lastpath(path)
                    #print("返回上一级目录:{}".format(path))
                    break
                if touchpad_o.is_pressed():
                        with open("{}/{}".format(path,Dir[num]),"r") as f:
                            readFile=Textreader(f.read())
                            readFile.main()
                elif button_b.is_pressed():
                    if t=="目录":
                        #print("进入目录:{}".format(Dir[num]))
                        #print("正在加载......可能需要几秒钟")
                        #print("Path: {}/{}".format(path,Dir[num]))
                        path="{}/{}".format(path,Dir[num])
                        break
                    elif t=="文件":
                        with open("{}/{}".format(path,Dir[num]),"r") as f:
                            readFile=Textreader(f.read())
                            readFile.main()
                    elif t=="可执行文件":
                        libname=("{}/{}".format(path,Dir[num]))[:-3].replace("/",".")
                        while libname[0]==".":
                            libname=libname[1:]
                        try:
                            __import__(libname)
                        except Exception as e:
                            print("导入失败，错误信息如下：\n",e.__class__.__name__,e)
                        else:
                            #print("导入成功")
                            pass
                    elif t=="图片":
                        oled.fill(0)
                        image_picture = Image()
                        oled.blit(image_picture.load('{}/{}'.format(path,Dir[num])), 0, 0)
                        oled.show()
                        while not (touchpad_t.is_pressed() or touchpad_h.is_pressed()):
                            pass
                if touchpad_n.is_pressed():
                    num+=1
                    if num>=DIRlen:num=0
                elif touchpad_p.is_pressed():
                    num-=1
                    if num<0:num=DIRlen-1
    #鸣谢名单
    #程序设计---LP_OVER/emofalling
    #界面设计---LP_OVER
    #bug修复/优化---emofalling
    #运行平台提供---W-Can1425

path='/'
while not button_a.is_pressed():
    fileview=FileViewer()
    fileview.fileviewer(path)