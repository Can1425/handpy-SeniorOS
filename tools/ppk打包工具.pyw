# by emofalling
import os
import _thread
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox

if not os.path.exists("packs"):
    os.mkdir("packs")

class gui:
    def __init__(self,root):
        self.root=root
        self.root.title("ppk打包工具")
        self.gui()
        self.root.mainloop()
    def gui(self):
        self.ispack=False
        
        self.log=Text(self.root,height=15)
        self.log.pack(side=BOTTOM,fill=BOTH)
        self.logt=Label(self.root,text="日志")
        self.logt.pack(side=BOTTOM)
        
        fse=Frame(self.root)
        fse.pack()
        f1=LabelFrame(fse,text="设置打包目录")
        f1.pack()
        f1i=Frame(f1)
        f1i.pack()
        f1t=Label(f1i,text="目录：")
        f1t.pack(side=LEFT)
        self.f1p=Entry(f1i,width=50)
        self.f1p.pack(side=LEFT)
        f1b=Button(f1i,text="浏览",width=5,command=self.exp)
        f1b.pack()
        self.sjv=IntVar(f1,1)
        sj=Checkbutton(f1,text="使用相对于选择的目录的相对目录（否则使用在该平台下的绝对目录）",variable=self.sjv,
                       onvalue=1,offvalue=0)
        sj.pack()
        
        f2=LabelFrame(fse,text="设置包信息")
        f2.pack()
        fn=Frame(f2)
        fn.pack()
        fnt=Label(fn,text="名称：")
        fnt.pack(side=LEFT)
        self.ni=Entry(fn,width=20)
        self.ni.pack()
        fv=Frame(f2)
        fv.pack()
        fvt=Label(fv,text="版本：")
        fvt.pack(side=LEFT)
        self.vi=Entry(fv,width=20)
        self.vi.pack()
        ft=Frame(f2)
        ft.pack()
        ftt=Label(ft,text="适用平台：")
        ftt.pack(side=LEFT)
        self.ti=Entry(ft,width=20)
        self.ti.pack()
        fa=Frame(f2)
        fa.pack()
        fat=Label(fa,text="作者：")
        fat.pack(side=LEFT)
        self.ai=Entry(fa,width=20)
        self.ai.pack()
        fg=Frame(f2)
        fg.pack()
        fgt=Label(fg,text="其他参数：")
        fgt.pack(side=LEFT)
        self.gi=Entry(fg,width=20)
        self.gi.pack()

        self.StartButton=Button(fse,text="开始打包",command=self.run)
        self.StartButton.pack()
        self.root.bind("<Return>",self.run)

    def exp(self):
        dire=filedialog.askdirectory(title="打包目录")
        if dire=="":
            return 0
        self.f1p.delete(0,END)
        self.f1p.insert(0,dire)
        self.ni.delete(0,END)
        self.ni.insert(0,os.path.basename(dire))
    def cll(self):
        self.log.delete(0.0,END)
    def l(self,s):
        self.log.insert(0.0,s+"\n")
    def run(self,event=None):
        if self.ispack:
            return 0
        path=self.f1p.get()
        if not os.path.exists(path):
            messagebox.showerror("错误","目录无效")
            return 0
        name=self.ni.get()
        version=self.vi.get()
        platform=self.ti.get()
        author=self.ai.get()
        arg=self.gi.get()
        rel=bool(self.sjv.get())
        _thread.start_new_thread(self.pack,(path,name,version,platform,author,arg,rel))
    def pack(self,path,name,version,platform,author,arg,rel):
        speed=1048576 #1MB
        self.ispack=True
        self.cll()
        filename=os.path.basename(path)
        pack=open("packs\\%s.ppk"%filename,"wb")
        self.l("创建：%s.ppk"%filename)
        def write(s):
            pack.write(s.encode())
        self.l("正在写入包信息")
        write(name + "\n")
        write(version + "\n")
        write(platform + "\n")
        write(author + "\n")
        write(arg + "\n")
        def add(a,b):
            return a.replace("\\","/")+"/"+b.replace("\\","/")
        self.l("正在写入目录信息")
        for p,o,f in os.walk(path):
            if rel:
                pt=os.path.relpath(p,path)
            else:
                pt=p
            for om in o:
                write('d"%s"\n'% add(pt,om))
                self.l("写入目录：%s"% add(pt,om))
            for fm in f:
                fmr=add(p,fm)
                try:
                    filesz=os.stat(fmr)[6]
                    file=open(fmr,"rb")
                    self.l("写入文件:%s"% add(pt,fm))
                    if filesz !=0 :
                        write('f"%s"%s\n'%(add(pt,fm),filesz))
                        while True:
                            nr=file.read(speed)
                            if len(nr)==0:
                                break
                            pack.write(nr)
                    else:
                        write('f"%s"\n'%add(pt,fm))
                except:
                    self.l("读取文件失败")
                """
                try:
                    file=open(fmr,"rb")
                    self.l("读取文件:%s"% fmr)
                except:
                    self.l("读取文件失败")
                    ff=b""
                else:
                    ff=file.read()
                    file.close()
                ff=ff.split(b"\n")
                fn=len(ff)
                if fn==1 and ff[0]==b"":
                    fn=""
                    ff=[]
                else:
                    fn=str(fn)
                self.l("写入文件：%s"% add(pt,fm))
                write('f"%s"%s\n'%(add(pt,fm),fn))
                for fk in ff:
                    pack.write(fk + b'\n')
                """
        self.ispack=False
        self.l("打包完成")
        messagebox.showinfo("提示","打包完成！")

gui(Tk())
