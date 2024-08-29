# 开发者模式将会启用绝大部分日志输出和禁用异常捕获（除了内存错误）
# 此处通过类似于回调函数的一个用法，在不修改原来代码的情况下（正经人谁愿意维护这屎山代码啊），控制绝大部分日志输出
# 如果需要绕过这一监测逻辑，使用print_(内容)即可
print_=print
print_("[GxxkSystem]系统本体被加载")
# 常用代码/API/导入模块
import ubinascii
import uhashlib as hashlib
import machine
import os
import urequests as requests
import parrot
import ntptime
import network
from mpython import *
import gc
#读取配置
with open("/SeniorOS/others_build/GxxkSystemData/config")as f:config_ = [i.strip("\r") for i in f.read().split("\n")]
print("[GxxkSystem]加载系统配置"+str(config_))
if int(config_[7]):
    print("[GxxkSystem]开启内存回收")
    gc.enable()
else:
    print("[GxxkSystem]关闭内存回收")
if int(config_[8]):
    print("[GxxkSystem]开启灵犀动画 By:POLA")
    gc.enable()
else:
    print("[GxxkSystem]关闭灵犀动画 By:POLA")
res = [["abcd", "efgh", "ijkl", "mnop"], ["qrst", "uvwx", "yz"], ["0123", "4567","89"], ["_+{}", '|:"=', "<>?-", ["[]\;", "',./", " !@#", ["[$%^", "&*()"]]]]
upper = True
temp = None 
def print(text):
    global config_,print_
    if config_[9]:
        print_(text)
 
def wait(mode="0"):
    modes = ("touchPad_P.read()<100 or touchPad_Y.read()<100 or touchPad_T.read()<100 or touchPad_H.read()<100 or touchPad_O.read()<100 or touchPad_N.read()<100",
             "button_a.value()==0 or button_b.value()==0")
    print("[GxxkSystem]等待用户操作...")
    print("[GxxkSystem]Mode："+ str(mode))
    while not eval(modes[0]+' or '+modes[1] if mode == "0" else modes[mode-1]):
        pass
    print("[GxxkSystem]用户做出决定")

# GxxkSystem/gxxkTyper.py
# 功能：可将某个嵌套列表中指定的一个大项（里面嵌套着很多列表的列表）中的每一个小列表合并为字符串
# 用法：list2str(index='[对应列表索引]')
# 这部分仅用于gxxkTyper部分


def list2str(list__='', index=''):
    exec("global "+list__)
    list_ = []
    for i in eval(list__+index):
        # 如果列表是字符串，那么直接将i添加到列表结尾
        # str用于指定列表内的嵌套的列表信息组合
        str_ = ''
        if type(i) == str:
            list_.append(i)
        else:
            # 将列表内的列表进行遍历，每一项的字符串拼接到str_内，最终再进行append
            str_+=[x if type(x)==str else [j if type(j)==str else [k for k in j] for j in x] for x in i]
            for x in i:
                if type(x) == str:
                    str_ += x
                else:
                    for j in x:
                        if type(j) == str:
                            str_ += j
                        else:
                            for k in j:
                                str_ += k
                            # res列表最多嵌套4层，所以这里可以直接加到临时变量
            # 结束当前层级循环后添加至列表
            list_.append(str_)
    return list_


class gxxkTyper():
    # 组内选择
    def group_main(group):
        global temp, upper
        print("[GxxkSystem]进入输入组的选择界面")
        print("[GxxkSystem]选择输入组")
        temp = group
        group_showtext = [i for i in temp]
        # 绘制UI
        oled.fill(0)
        # 不直接写4个DispChar是因为有的时候列表只有2个选项
        for i in range(len(group_showtext)):
            oled.DispChar(group_showtext[i].upper() if upper else group_showtext[i], 0, i*16)
        oled.show()
        # 等待
        wait()
        # 对决策作出判断
        if touchPad_P.read() < 100:
            # 组1
            print("[GxxkSystem]选择组1")
            return 0
        elif touchPad_Y.read() < 100 and len(group_showtext) >= 2:
            # 组2
            print("[GxxkSystem]选择组2 ")
            return 1
        elif touchPad_T.read() < 100 and len(group_showtext) >= 3:
            # 组3，多加一个条件是因为部分列表只有3或2个选项，下面也是
            print("[GxxkSystem]选择组3")
            return 2
        elif touchPad_H.read() < 100 and len(group_showtext) >= 4:
            # 组4
            print("[GxxkSystem]选择组4")
            return 3
        else:
            print("[GxxkSystem]未作出有效决策，自动返回上一级")
    # 主程序
    # 每个字母组、数字组使用group_main输入，设定好对应的组（group参数来源于str）即可

    def main(text=""):
        global res, temp, upper
        list_ = res
        while not button_a.value()==0:  # 如果a按下就跳出循环
            print("[GxxkSystem]文本  "+text)
            print("[GxxkSystem]大写状态为"+str(upper))
            print("[GxxkSystem]当前组："+str(list_))
            if touchPad_O.read() < 100:  # 显示文本
                print("[GxxkSystem]选择显示已输入内容，按任意键返回")
                oled.fill(0)
                oled.DispChar(text, 0, 0, auto_return=True)
                oled.show()
                wait()
            elif touchPad_N.read() < 100:  # 切换大小写
                print("[GxxkSystem]切换大小写")
                upper = bool(upper-1)
                sleep(0.3)
            elif button_b.value()==0:
                print("[GxxkSystem]退格")
                text = text[:len(text)-1]  # 退格
                sleep(0.3)
            try:
                userInput = gxxkTyper.group_main(
                    list_)  # 先把默认的列表传进去选择，返回值是用户选择的内容的索引
            except KeyboardInterrupt:
                userInput = None
                text = input("[GxxkSystem]请输入要修改的字段：")
            if userInput == None:  # 如果未作出有效决策，就先跳过当前循环，循环开始有 判断语句
                continue
            elif type(list_) == str:
                print("[GxxkSystem] "+list_[userInput]+" 为str，添加至text变量中")
                if upper:
                    text += list_[userInput].upper()
                else:
                    text += list_[userInput]
                list_ = res
            elif type(list_) == list:
                print('[GxxkSystem] '+str(list_[userInput])+" 为list，继续进行选择")
                list_ = list_[userInput]
        print("[GxxkSystem]按下A键 返回")
        gc.collect()
        return text

def consani(start_x=0,start_y=0,start_wide=129,start_height=65,start_fillet=0,done_x=0,done_y=0,done_wide=0,done_height=0,done_fillet=0,done_wait=5):
    global config_
    if not int(config_[8]):return None
    for count in range(7):
        oled.fill_rect(done_x, done_y, done_wide, done_height, 0)
        done_x = (done_x - start_x) // 2
        done_y = (done_y - start_y) // 2
        done_wide = (start_wide + done_wide) // 2
        done_height = (start_height + done_height) // 2
        done_fillet = (done_fillet - start_fillet) // 2
        done_wait = done_wait + 3
        oled.RoundRect(done_x, done_y, done_wide, done_height, done_fillet, 1)
        oled.show()
        if touchPad_P.read()<100 or touchPad_Y.read()<100:
            break
        sleep_ms(done_wait)

# GxxkSystem/main.py —— 选择器
# 就只有这个被我分离出来了，剩下的还是在别的里面 
def select(options, title):
    print("[GxxkSystem]进入选择器界面")
    target = 0
    # 主循环
    while True:
        print("[GxxkSystem]Target"+str(target))
        # 绘制UI
        oled.fill(0)
        oled.hline(0, 15, 128, 1)
        oled.DispChar(title, 0, -1)
        oled.DispChar(options[target], 0, 16, 2) # 反色模式绘制选中内容
        try:
            oled.DispChar(options[target+1], 0, 32)
            oled.DispChar(options[target+2], 0, 48) 
        except:pass
                
        oled.show()
        # 等待操作
        wait()
        # 做出决策
        if button_a.value()==0:
            return target, "A"
        elif button_b.value()==0:
            return target, "B"
        elif touchPad_P.read() < 100:
            target -= 1  # 向上（左）
        elif touchPad_N.read() < 100:
            target += 1  # 向下（右）
        if target == -1:
            target = len(options)-1
        elif target==len(options):
            target=0

# GxxkSystem/pluginApi.py
# 插件配置格式
# {id:[信息（列表）],id2:[信息2]}

# 不是 你这段就没多大意义了吧 会的人可以自己写配置文件 不会的图形化开发者又用不了
#                                               ——LP
# az 总之留着吧 屎山代码懒得改了
class pluginApi():
    def getPluginConfig(id):  # 指定行号
        with open("/SeniorOS/others_build/GxxkSystemData/pluginConfig", mode="r", encoding="utf-8")as f:
            try:
                return eval(f.read())[id]
            except IndexError:
                return None

    def writePluginConfig(id, data):
        config = pluginApi.getPluginConfig()
        config[id] = data
        with open("/SeniorOS/others_build/GxxkSystemData/pluginConfig", mode="w", encoding="utf-8")as f:
            f.write(str(config))

# GxxkSystem/config.py
# 这里负责获取/修改配置

# 格式：
# 系统版本
# 插件源
# 更新源
# WiFiSSID
# WiFiPWD
# 网络插件索引位置，将被拼接到插件源的后面
# 本体MD5
# 是否开启自动内存回收，0关1开
# 是否启用动画，0关1开
# 是否启用开发者模式，0关1开

class config():
    def writeConfig(index, text):
        global config_
        cfg = config_
        with open("/SeniorOS/others_build/GxxkSystemData/config", mode="w", encoding="utf-8")as f:
            for i in range(len(cfg)):
                if i == index:
                    f.write(str(text)+"\n")
                else:
                    f.write(str(cfg[i])+"\n")

# GxxkSystem/ui.py
# 这里用于存放静态\半静态页面


class ui():

    # 旧版本函数，drawLine，用于绘制分割线
    # def drawLine():
    #     oled.hline(0, 15, 128, 1)

    def noConnect():
        oled.fill(0)
        oled.DispChar("GxxkSystem-没有网络", 0, 0)
        oled.hline(0, 15, 128, 1)
        oled.DispChar("未连接WiFi 无法使用此功能", 0, 16, auto_return=True)
        oled.show()

    def showText(text):
        oled.fill(0)
        oled.DispChar("GxxkSystem-信息提示", 0, 0)
        oled.hline(0, 15, 128, 1)
        oled.DispChar(text, 0, 16, auto_return=True)
        oled.show()

    def noPlugin():
        oled.fill(0)
        oled.DispChar("GxxkSystem-没有插件", 0, -1)
        oled.hline(0, 15, 128, 1)
        oled.DispChar("目前没有存储任何本地插件，请先在插件商店下载插件", 0, 16, auto_return=True)
        oled.show()

    def about():
        oled.fill(0)
        global config_
        oled.DispChar("GxxkSystem-关于", 0, -1)
        oled.hline(0, 15, 128, 1)
        oled.DispChar("作者：0f永蓝", 0, 16)
        oled.DispChar("版本"+config_[0], 0, 32)
        oled.DispChar("动画：POLA",0,48)
        oled.show()

    def pluginInfo(pluginName, pluginAuthor):
        oled.fill(0)
        oled.hline(0, 15, 128, 1)
        oled.DispChar("GxxkSystem-插件信息", 0, -1)
        oled.DispChar("名："+pluginName, 0, 16)
        oled.DispChar("作者："+pluginAuthor, 0, 32)
        oled.show()


# GxxkSystem/main.py
# 主函数
class main():
    def main():
        consani()
        print("[GxxkSystem]进入主界面")
        userInput = select(
            options=["插件商店", "本地插件", "设置界面"],
            title="GxxkSystem-主界面")
        if userInput[1] == "B":
            main.lockScreen()
        wait()
        if userInput[0] == 0:
            main.pluginStore()  # 插件商店
        elif userInput[0] == 1:
            main.localPlugin()  # 本地插件
        elif userInput[0] == 2:
            main.setting()  # 设置
        else:
            print("[GxxkSystem]未作出有效决策，等待")

    # 插件商店
    # 插件列表格式： [["插件名称","插件作者","插件文件名"],["插件名称2","插件作者2","插件文件名2"]...]
    def pluginStore():
        global config_
        print("[GxxkSystem]进入在线插件商店")
        print("[GxxkSystem]目录"+os.getcwd())
        # 判断有没有网络
        if not wifi().sta.isconnected():
            ui.noConnect()
            sleep(1.5)
            main.main()
        # 获取插件列表
        r = requests.get(config_[1]+config_[5])
        if r.status_code != 200:
            ui.showText("获取插件列表失败，1s后退出")
            sleep(1)
            r.close()
            main.main()
        else:
            localPluginList = eval(r.text)
            r.close()
        print("[GxxkSystem]进入插件商店，软件源 "+str(config_[1]) +
              "   软件源信息 "+str(localPluginList))
        # 选择
        userInput = select(
            options=[i[0] for i in localPluginList],
            title="GxxkSystem-插件商店")

        # 判断决策  
        if userInput[1] == "B":
            main.main()  # 此处B为退出
        print("[GxxkSystem]"+str(userInput)+"被选中")
        ui.pluginInfo(localPluginList[userInput][0], localPluginList[userInput][1])
        # 等待做出决策
        wait()
        # 按任意键返回菜单
        if button_a.value()==0:  # 获取插件并运行
            print("[GxxkSystem]获取插件 URL："+config_[1] +
                  localPluginList[userInput][2])
            print("[GxxkSystem]插件文件 "+localPluginList[userInput][2])
            ui.showText("获取并写入插件中...")
            r = requests.get(config_[1]+localPluginList[userInput][2])
            if r.status_code != 200:  # 获取插件失败
                ui.showText("获取插件失败（1s后返回）")
                r.close()
                sleep(1)
                main.main()
            else:
                with open("/SeniorOS/others_build/GxxkSystemData/GxxkPlugin/"+localPluginList[userInput][2], mode="wb")as f:
                    f.write(r.content)
                r.close()
            ui.showText("加载中...")
            oled.fill(0)
            # 说实话这个字符串切片好像颜文字啊哈哈哈
            exec("import GxxkSystemData.GxxkPlugin." +
                 localPluginList[userInput][2][:-4]+" as startTarget;startTarget.start()")
        main.main()

    # 本地插件
    # 格式：[[名称,作者,导入的模块名]]
    def localPlugin():
        print("[GxxkSystem]进入本地插件")
        consani()
        ui.showText("请稍等...加载插件中")
        # 切换目录
        os.chdir("/SeniorOS/others_build/GxxkSystemData/GxxkPlugin/")
        # 获取插件信息
        localPluginList = [i[:-4] for i in os.listdir()]
        if len(localPluginList) == 0:
            print("[GxxkSystem]本地没有插件，回到主界面")
            ui.noPlugin()
            sleep(0.5)
            main.main()
        print("[GxxkSystem]开始遍历本地文件下的所有内容")
        # 处理插件列表信息
        for i in range(len(localPluginList)):
            print("[GxxkSystem]第"+str(i)+"个模块，导入名"+str(localPluginList[i]))
            exec("import {}".format(localPluginList[i]))
            info = eval(localPluginList[i]+".info")
            localPluginList[i] = [info[0], info[1],
                                  localPluginList[i]]  # 这里相当于是二维列表
            print("[GxxkSystem]文件名 "+localPluginList[i]
                  [2]+" 名称 "+localPluginList[i][0])
        print("[GxxkSystem]插件列表 "+str(localPluginList))
        # 选择
        userInput = select([i[0] for i in localPluginList], "GxxkSystem-本地插件")
        if userInput[1] == "B":
            main.main()  # 此处B为退出
        ui.pluginInfo(localPluginList[userInput[0]]
                      [0], localPluginList[userInput[0]][1])
        wait()
        if button_a.value()==0:
            print("[GxxkSystem]运行")
            exec(localPluginList[userInput[0]][2]+".start()")  # 运行插件
            print("[GxxkSystem]插件运行结束，正常返回")
            sleep(0.5)
            wait()
        elif button_b.value()==0:
            os.remove("/SeniorOS/others_build/GxxkSystemData/GxxkPlugin/" +
                      localPluginList[userInput[0]][2]+".mpy")  # 删除插件
        main.main()

    # 设置
    # 使用 PY TH ON 操作
    def setting():
        consani()
        global config_
        print("[GxxkSystem]进入设置页面")
        userInput = select(
            ["WiFi设置",
             "重启", "关于", "效验完整性",
             "关闭内存回收" if int(config_[7]) else "开启内存回收",
             "更新","关闭灵犀动画" if int(config_[8]) else "开启灵犀动画"]
            , "GxxkSystem-设置")
        if userInput[1] == "B":
            main.main()
        if userInput[0] == 0:
            consani()
            userInput = select(["设置WiFi信息", "断开WiFi" if wifi().sta.isconnected() else "连接WiFi"], "GxxkSystem-WiFi设置")
            if userInput[1] == "B":
                main.setting()
            if userInput[0] == 0:
                consani()
                ui.showText("扫描WiFi中...")
                network.WLAN().active(True)
                temp = [i[0].decode() for i in network.WLAN().scan()]
                network.WLAN().active(False)
                temp.append("手动输入WiFi")
                consani()
                ssid = temp[select(temp, "GxxkSystem-选择WiFi")]
                if ssid == "手动输入WiFi":
                    consani()
                    ssid = gxxkTyper.main()
                consani()
                ui.showText("输入WiFi密码")
                sleep(0.5)
                consani()
                pwd = gxxkTyper.main()
                print("[GxxkSystem]输入WiFi信息，ssid:"+ssid+"   pwd:"+pwd)
                config.writeConfig(str(ssid), 3)
                config.writeConfig(str(pwd), 4)
                print("[GxxkSystem]")
                try:
                    wifi().connectWiFi(ssid,pwd)
                except OSError:
                    ui.showText("WiFi信息错误！")
                ntptime.settime(8, "cn.ntp.org.cn")
                sleep(1)
            elif userInput[0] == 1:
                consani()
                if not wifi().sta.isconnected():
                    print("[GxxkSystem]连接WiFi")
                    ui.showText("正在连接中...如回到主界面就代表连接成功")
                    try:
                        wifi().connectWiFi(config_[3], config_[4])
                        ntptime.settime(8, "cn.ntp.org.cn")
                    except OSError:
                        ui.showText("WiFi信息错误！")
                    sleep(1)
                else:
                    print("[GxxkSystem]断开WiFi")
                    ui.showText("已断开WiFi")
                    wifi().disconnectWiFi()
                    sleep(0.5)
        elif userInput[0] == 1:
            ui.showText("即将在3s后重启")
            sleep(3)
            consani()
            machine.reset()
        elif userInput[0] == 2:
            consani()
            ui.about()
            wait()  # 关于 界面
        elif userInput[0] == 3:
            consani()
            print("[GxxkSystem]效验文件完整性")
            ui.showText("效验一次需要占用10-12kb的RAM，A继续")
            wait()
            if button_a.value()==0:
                consani()
                ui.showText("请稍等... 正在效验GxxkSystem主文件MD5值")
                # MD5部分存在于本地Config文件中
                with open(__file__, 'rb') as f:
                    fileMD5=str(ubinascii.hexlify(hashlib.md5(f.read()).digest()).upper())[2:-1]
                print("[GxxkSystem]配置文件内的hash："+config_[6])
                print("[GxxkSystem]本体hash："+fileMD5)
                consani()
                if config_[6] == fileMD5:
                    ui.showText("当前版本主文件未被修改，详细信息已输出到控制台")
                else:
                    ui.showText("文件hash与原版hash不匹配！详细信息已输出到控制台")
                sleep(1.5)
        elif userInput[0]==4: #是否启用内存回收
            consani()
            ui.showText("设置成功")
            config_[7]=str(int(config_[7])-1)
            config.writeConfig(7,str(int(config_[7])-1))
            sleep(1)
        elif userInput[0]==5: #更新
            consani()
            ui.showText("此功能在当前版本中被禁用！")
            wait()
            """
            if button_b.value()==0:main.setting()
            consani()
            oled.fill(0)
            oled.hline(0, 15, 128, 1)
            oled.DispChar("GxxkSystem-更新中...", 0, -1)
            oled.DispChar("将从云端下载安装包 完成后进入安装包界面", 0, 16, auto_return=True)
            oled.show()
            wifi.connect(config_[3], config_[4])
            with requests.get(config_[2]) as r:
                if r.status_code != 200:
                    oled.hline(0, 15, 128, 1)
                    oled.DispChar("GxxkSystem-更新错误", 0, 0)
                    oled.DispChar("获取安装包失败！2s后重启", 0, 16, auto_return=True)
                    oled.show()
                    time.sleep(2)
                    r.close()
                    machine.reset()
                with open("/GxxkSystem.mpy", mode="wb")as f:
                    f.write(r.content)
            machine.reset()
            """
        elif userInput[0]==6: #是否启用内存回收
            consani()
            ui.showText("设置成功")
            config_[8]=str(int(config_[8])-1)
            config.writeConfig(8,str(int(config_[8])-1))
            sleep(1)
        main.main()


    # 锁屏界面
    def lockScreen():
        consani()
        clock = Clock(oled, 15, 30, 15)
        rtc = machine.RTC()
        isConnect = wifi().sta.isconnected()
        if isConnect:
            w = requests.get(
                "https://api.seniverse.com/v3/weather/now.json?key=SHiilwSnAHS_tFuh6&location=ip&language=zh-Hans")
            if w.status_code != 200:
                isConnect = False
            else:
                w_ = w.json()
            w.close()                                      
            w = w_
            del w_ 
            text_day = w['results'][0]['now']['text']
            temperature = w['results'][0]['now']['temperature'] 
        while not button_b.value()==0:
            dt = rtc.datetime()
            oled.fill(0)
            clock.settime()
            clock.drawClock()
            oled.DispChar("GxxkSystem-锁屏界面", 0, -1)
            oled.hline(0, 15, 128, 1)
            oled.DispChar(str(dt[0]), 32, 16)
            oled.DispChar('{}.{}'.format(dt[1], dt[2]), 32, 32)
            oled.DispChar('{}:{}:{}'.format(dt[4], dt[5], dt[6]), 0, 48)
            try:
                oled.DispChar('电压'+str(parrot.get_battery_level()), 66, 16)
            except OSError:
                oled.DispChar("未开拓展板", 66, 16)
            oled.vline(64, 16, 48, 1)
            if isConnect:
                oled.DispChar("天气:"+text_day, 66, 32)
                oled.DispChar("温度:"+str(temperature), 66, 48)
            else:
                oled.DispChar("无网络", 66, 32)
            oled.show()
        consani()


def start():
    global config_,print_
    isREPL = button_b.value()==0
    # 其实单文件系统从第一行代码加载成功的时候，整个系统就已经完全加载好了，但是有一个图标和等待界面会让用户觉得流畅一点

    #启动主代码
    # exec(compile("try:\n\tif not isREPL:\n\t\t"+'_thread.start_new_thread(lambda ssid,pwd:wifi().connectWiFi(ssid,pwd),("ssid","pwd"))\n\t\t' if config_[9] else ""+"\n\t\tmain.main()\n"+"except MemoryError:\n\tui.showText(\"GxxkSystem发生内存错误\")" if config_[9] else "".format() +"\nexcept Exception as e:\n\tui.showText(\"系统发生未知错误，详细信息已输出到控制台\")\n\tprint_(\"[GxxkSystem]发生未知错误，具体报错为：\"+str(e))" if config_[9] else "","<startGxxkSystem>","exec"))
    try:
        if not isREPL:
            main.main()
    except MemoryError:
        ui.showText("GxxkSystem发生内存错误")
    if isREPL:
        ui.showText("已进入REPL！")
        oled.fill(0)

# 给个建议 wifi可以尝试多线程链接（指用_thread模块搞） 开机的时候开一个线程尝试根据配置自动链接 就是完全静默的
#  ——LP
# 这个想法好 可以实现 简单写一个匿名函数然后多线程即可
# _thread.start_new_thread(lambda ssid,pwd:wifi().connectWiFi(ssid,pwd),("ssid","pwd"))
# 尝试实现了一下 加在start函数 那个启动主代码exec里边字符串就完事
# 实装了 cfg第九行打开就能用 你编译拿去试试

start()