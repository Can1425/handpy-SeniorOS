path='/'
while not eval("[/GetButtonExpr('a')/]")():
    fileviewer(path)

def IsFile(f):
    print(f)
    if os.stat(f)[0]<20000:return "目录"
    else:
        return fileattribute(f)
def fileattribute(f):
    last4=f[-4:]
    last3=f[-3:]
    if last3==".py":
        return "可执行文件"
    elif last4==".pbm" or last4==".bmp":
        return "图片"
    else:
        return "文件"
def waitkey(**kwargs):
    while True:
        for value,key in kwargs.items():
            if key.is_pressed():
                return value
pathpic=bytearray([0X00,0X00,0X3E,0X00,
                0X41,0X00,0X80,0X80,
                0X81,0XFC,0XFE,0X02,
                0X80,0X01,0X80,0X01,
                0XFF,0XFF,0X80,0X01,
                0X80,0X01,0X80,0X01,
                0X80,0X01,0X80,0X01,
                0X40,0X02,0X3F,0XFC,])
filepic=bytearray([0X00,0X00,0X3F,0XC0,
                0X20,0X60,0X2F,0X50,
                0X20,0X48,0X2F,0X7C,
                0X20,0X04,0X23,0XC4,
                0X22,0X04,0X23,0X84,
                0X22,0X04,0X22,0X04,
                0X22,0X04,0X20,0X04,
                0X3F,0XFC,0X00,0X00,])
runpic=bytearray([0X00,0X00,0X3F,0XC0,
                0X20,0X60,0X2F,0X50,
                0X20,0X48,0X2F,0X7C,
                0X20,0X04,0X23,0XC4,
                0X22,0X04,0X23,0X84,
                0X22,0X04,0X22,0X04,
                0X22,0X04,0X20,0X04,
                0X3F,0XFC,0X00,0X00,])
picpic=bytearray([0XFF,0XFF,0X80,0X01,
                0X8C,0X01,0X92,0X01,
                0X92,0X09,0X8C,0X15,
                0X80,0X23,0X84,0X41,
                0X8A,0X81,0X91,0X01,
                0XA0,0X01,0XC0,0X01,
                0X80,0X01,0X80,0X01,
                0X80,0X01,0XFF,0XFF,])

def fileviewer(initpath:str):
    path=initpath
    if path[:2]=="//":
        path=path[1:]
    Pathpic=pathpic
    Filepic=filepic
    Runpic=runpic
    Picpic=picpic
    def lastpath(path:str):
        return "/".join(path.split("/")[:-1])
    while True:
        Dir=os.listdir(path)
        DIRlen=len(Dir)
        num=0
        while True:
            t=IsFile("{}/{}".format(path,Dir[num]))
            oled.fill(0)
            oled.DispChar(Dir[num],16,0)
            oled.DispChar("属性:{}".format(t),0,16)
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
            key=waitkey(A=button_a,B=button_b,Y=touchpad_y,T=touchpad_t,H=touchpad_h,O=touchpad_o,N=touchpad_n,P=touchpad_p)
            if key=="T" or key=="H":
                if path=="/":
                    #print("已经是根目录")
                    continue
                path=lastpath(path)
                #print("返回上一级目录:{}".format(path))
                break
            elif key=="B":
                if t=="目录":
                    #print("进入目录:{}".format(Dir[num]))
                    #print("正在加载......可能需要几秒钟")
                    #print("Path: {}/{}".format(path,Dir[num]))
                    path="{}/{}".format(path,Dir[num])
                    break
                elif t=="文件":
                    oled.fill(0)
                    oled.DispChar("暂时不支持文件预览",0,0)
                    oled.DispChar("1秒后返回",0,16)
                    oled.show()
                    time.sleep(1)
                    break
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
                    while not key=="T" or key=="H":
                        pass
            elif key=="N":
                num+=1
                if num>=DIRlen:num=0
            elif key=="P":
                num-=1
                if num<0:num=DIRlen-1
    #鸣谢名单
    #程序设计---LP_OVER/emofalling
    #界面设计---LP_OVER
    #bug修复/优化---emofalling
    #运行平台提供---W-Can1425
    #感谢各位的付出!
    #fileviewer  -by LP_OVER/emofalling