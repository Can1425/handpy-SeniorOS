# 注意：在导入devlib后请不要导入mpython，否则会报错，反过来也是，在导入mpython后请不要导入devlib，否则会报错
from machine import Pin,I2C,TouchPad,ADC
from esp import flash_read
from neopixel import NeoPixel
from ssd1106_dpr import SSD1106_I2C
from micropython import schedule,const
from gui import *
import micropython
from framebuf import FrameBuffer
import ustruct,math,time
import calibrate_img
import NVS
import network
import SeniorOS.system.log_manager as LogManager
LogManager.Output("system/devlib.mpy", "INFO")

overclock=True
if overclock:
    i2cclock=1250000
else:
    i2cclock= 400000
i2c = I2C(0, scl=Pin(Pin.P19), sda=Pin(Pin.P20), freq=i2cclock)

class wifi:
    def __init__(self):
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)

    def connectWiFi(self, ssid, passwd, timeout=10):
        if self.sta.isconnected():
            self.sta.disconnect()
        self.sta.active(True)
        list = self.sta.scan()
        for i, wifi_info in enumerate(list):
            try:
                if wifi_info[0].decode() == ssid:
                    self.sta.connect(ssid, passwd)
                    wifi_dbm = wifi_info[3]
                    break
            except UnicodeError:
                self.sta.connect(ssid, passwd)
                wifi_dbm = '?'
                break
            if i == len(list) - 1:
                LogManager.Output("SSID invalid / failed to scan this wifi", "ERROR")
        start = time.time()
        LogManager.Output("Connection WiFi", "INFO")
        while (self.sta.ifconfig()[0] == '0.0.0.0'):
            if time.ticks_diff(time.time(), start) > timeout:
                print("")
                LogManager.Output("Timeout!,check your wifi password and keep your network unblocked", "Error")
            print("_ ", end="")
            time.sleep_ms(500)
        print("")
        LogManager.Output('WiFi(%s,%sdBm) Connection Successful, Config:%s' % (ssid, str(wifi_dbm), str(self.sta.ifconfig())), "INFO")


class Colormode:
    noshow=0
    normal=1
    reverse=2
    nobg=3
    reverse_nobg=4
    black=5
    white=6
    xor=7
    xor_nobg=8
    xor_fill=9
    xor_fill_reverse=10
class Outmode:
    keepon=0
    stop=1
    stop2=2
    autoreturn=3
    autoreturn2=4
    ellipsis=5

font_address=0x400000
maximum_fontbitmaplen=64
class OLED(SSD1106_I2C):
    def __init__(self,addr):
        super().__init__(128,64,i2c,addr,external_vcc=True) #VDD=3.3v,且掌控板自带的稳压器带载能力通常比OLED内置的稳压器更好,所以使用external_vcc=True
        #将Font对象集成在OLED内，提高速度
        self.font_addr=font_address
        buffer = bytearray(18)
        flash_read(self.font_addr, buffer)
        self.font_header,\
        self.font_height,\
        self.font_width,\
        self.font_baseline,\
        self.font_x_height,\
        self.font_y_height,\
        self.font_first_char,\
        self.font_last_char = ustruct.unpack('4sHHHHHHH', buffer)
        del buffer
        self.font_lenbuffer=bytearray(6)
        self.font_infobuffer=bytearray(4)
        self.font_bitmapbuffer=bytearray(maximum_fontbitmaplen)
        if self.font_header != b"GUIX":
            print("Font Error: Invalid font header: {}".format(self.font_header))
    @micropython.native
    def _reverse(self,bytearr:bytearray):
        for i in range(len(bytearr)):
            bytearr[i]=~bytearr[i]
    def DispChar(self, s, x, y, mode=Colormode.normal, out=Outmode.stop,maximum_x=128,space=1,newlinecode=True,return_x=0,return_addy=16,ellipsis="...",end="",buffer=None):
        stat_w=0
        stat_h=0
        stat_chars=0
        stat_returns=0
        char_x=x
        char_y=y
        char_w=0
        char_h=self.font_height
        lenbuffer=self.font_lenbuffer
        infobuffer=self.font_infobuffer
        bitmapbuffer=self.font_bitmapbuffer

        framebuffer=FrameBuffer
        flashread=flash_read
        unpack=ustruct.unpack

        firstchar=self.font_first_char
        lastchar=self.font_last_char
        charaddr=self.font_addr
        first_char_info_address = charaddr + 18
        reverse=self._reverse

        if buffer:
            screen=buffer
        else:
            screen=self
        blit=screen.blit
        fill_rect=screen.fill_rect
         
        if out==5:
            ellip_w=0
            end_w=0
            cchar_w=0
            for char in ellipsis:
                uni=ord(char)
                if firstchar>uni or lastchar<uni:
                    continue
                flashread(first_char_info_address + (uni - firstchar) * 6, lenbuffer)
                ptr_char_data, len = unpack('IH', lenbuffer)
                if not (ptr_char_data and len):
                    continue
                flashread(ptr_char_data + charaddr, infobuffer)
                char_w,_ = unpack('HH', infobuffer)
                ellip_w+=char_w+space
            for char in end:
                uni=ord(char)
                if firstchar>uni or lastchar<uni:
                    continue
                flashread(first_char_info_address + (uni - firstchar) * 6, lenbuffer)
                ptr_char_data, len = unpack('IH', lenbuffer)
                if not (ptr_char_data and len):
                    continue
                flashread(ptr_char_data + charaddr, infobuffer)
                char_w,_ = unpack('HH', infobuffer)
                end_w+=char_w+space
            ellip_x = maximum_x-ellip_w-end_w
            maximum_x -= end_w
            eidx=None
            for index,char in enumerate(s):
                uni=ord(char)
                if uni==10 and newlinecode: #ord("\n")
                    cchar_w=return_x
                    continue
                if firstchar>uni or lastchar<uni:
                    continue
                flashread(first_char_info_address + (uni - firstchar) * 6, lenbuffer)
                ptr_char_data, len = unpack('IH', lenbuffer)
                if not (ptr_char_data and len):
                    continue
                flashread(ptr_char_data + charaddr, infobuffer)
                char_w,_ = unpack('HH', infobuffer)
                cchar_w+=char_w+space
                if cchar_w>ellip_x and eidx is None:
                    eidx=index
                if cchar_w>maximum_x:
                    s=s[:eidx]+ellipsis
                    break
        s+=end
        for char in s:
            uni=ord(char)
            if uni==10 and newlinecode: #ord("\n")
                char_x=return_x
                char_y+=return_addy
                stat_returns+=1
                continue
            if firstchar>uni or lastchar<uni:
                continue
            flashread(first_char_info_address + (uni - firstchar) *6, lenbuffer)
            ptr_char_data, len = unpack('IH', lenbuffer)
            if not (ptr_char_data and len):
                continue
            addr_len = ptr_char_data + charaddr
            flashread(addr_len, infobuffer)
            char_w,_ = unpack('HH', infobuffer)
            if char_x+char_w>maximum_x:
                if out==2:
                    break
                elif out==3:
                    char_x=return_x
                    char_y+=return_addy
                    stat_returns+=1
            bgcol=self.pixel(char_x,char_y)
            if mode==0:
                pass
            elif mode==5:
                fill_rect(char_x,char_y,char_w,char_h,0)
            elif mode==6:
                fill_rect(char_x,char_y,char_w,char_h,1)
            elif mode==9:
                fill_rect(char_x,char_y,char_w,char_h,bgcol)
            elif mode==10:
                fill_rect(char_x,char_y,char_w,char_h,0 if bgcol else 1)
            else:
                flashread(addr_len+4,bitmapbuffer)
                if mode in (2,4):
                    reverse(bitmapbuffer)
                elif mode in (7,8) and bgcol==1:
                    reverse(bitmapbuffer)
                fbuf=framebuffer(bitmapbuffer,char_w,char_h,3)#framebuf.MONO_HLSB = 3   framebuf.MONO_HMSB = 4
                if mode==3 or (mode==8 and bgcol==0):
                    blit(fbuf,char_x,char_y,0)
                elif mode==4 or (mode==8 and bgcol==1):
                    blit(fbuf,char_x,char_y,1)
                else:
                    blit(fbuf,char_x,char_y)
            char_x+=char_w+space
            if char_x>maximum_x:
                if out==1:
                    break
                elif out==4:
                    char_x=return_x
                    char_y+=return_addy
                    stat_returns+=1
            stat_chars+=1
            stat_w=max(stat_w,char_x-x)
        stat_h=stat_returns*return_addy+char_h
        return (stat_w,stat_h),(stat_chars,stat_returns)
    def DispChar_font(self,font,s,x,y,mode=Colormode.normal,out=Outmode.stop,*,maximum_x=128,space=1,newlinecode=True,return_x=0,return_addy=16,ellipsis="...",end="",buffer=None):
        stat_w=0
        stat_h=0
        stat_chars=0
        stat_returns=0
        char_x=x
        char_y=y
        char_w=0
        char_h=font.height()

        firstchar=font.min_ch()
        lastchar=font.max_ch()

        framebuffer=FrameBuffer
        reverse=self._reverse

        if buffer:
            screen=buffer
        else:
            screen=self
        blit=screen.blit
        fill_rect=screen.fill_rect
        if font.hmap():
            font_map = 4 if font.reverse() else 3 #framebuf.MONO_HLSB = 3   framebuf.MONO_HMSB = 4
        else:
            if font.reverse():
                font_map = 0 #framebuf.MONO_VLSB = 0
            else:
                raise TypeError("No support vmap and no reverse font")
        
        if out==5:
            ellip_w=0
            end_w=0
            cchar_w=0
            for char in ellipsis:
                uni=ord(char)
                if firstchar>uni or lastchar<uni:
                    continue
                _,_,char_w = font.get_ch(char)
                ellip_w+=char_w+space
            for char in end:
                uni=ord(char)
                if firstchar>uni or lastchar<uni:
                    continue
                _,_,char_w = font.get_ch(char)
                end_w+=char_w+space
            ellip_x = maximum_x-ellip_w-end_w
            maximum_x -= end_w
            eidx=None
            for index,char in enumerate(s):
                uni=ord(char)
                if firstchar>uni or lastchar<uni:
                    continue
                if uni==10 and newlinecode: #ord("\n")
                    cchar_w=return_x
                    continue
                _,_,char_w = font.get_ch(char)
                cchar_w+=char_w+space
                if cchar_w>ellip_x and eidx is None:
                    eidx=index
                if cchar_w>maximum_x:
                    s=s[:eidx]+ellipsis
                    break
        s+=end
        for char in s:
            uni=ord(char)
            if uni==10 and newlinecode: #ord("\n")
                char_x=return_x
                char_y+=return_addy
                stat_returns+=1
                continue
            if firstchar>uni or lastchar<uni:
                continue
            _,_,char_w = font.get_ch(char)
            if char_x+char_w>maximum_x:
                if out==2:
                    break
                elif out==3:
                    char_x=return_x
                    char_y+=return_addy
                    stat_returns+=1
            bgcol=self.pixel(char_x,char_y)
            if mode==0:
                pass
            elif mode==5:
                fill_rect(char_x,char_y,char_w,char_h,0)
            elif mode==6:
                fill_rect(char_x,char_y,char_w,char_h,1)
            elif mode==9:
                fill_rect(char_x,char_y,char_w,char_h,bgcol)
            elif mode==10:
                fill_rect(char_x,char_y,char_w,char_h,0 if bgcol else 1)
            else:
                mview,_,_ = font.get_ch(char)
                bitmapbuffer=bytearray(mview)
                if mode in (2,4):
                    reverse(bitmapbuffer)
                elif mode in (7,8) and bgcol==1:
                    reverse(bitmapbuffer)
                fbuf=framebuffer(bitmapbuffer,char_w,char_h,font_map)#framebuf.MONO_HLSB = 3   framebuf.MONO_HMSB = 4
                if mode==3 or (mode==8 and bgcol==0):
                    blit(fbuf,char_x,char_y,0)
                elif mode==4 or (mode==8 and bgcol==1):
                    blit(fbuf,char_x,char_y,1)
                else:
                    blit(fbuf,char_x,char_y)
            char_x+=char_w+space
            if char_x>maximum_x:
                if out==1:
                    break
                elif out==4:
                    char_x=return_x
                    char_y+=return_addy
                    stat_returns+=1
            stat_chars+=1
            stat_w=max(stat_w,char_x-x)
        stat_h=stat_returns*return_addy+char_h
        return (stat_w,stat_h),(stat_chars,stat_returns)


if 60 in i2c.scan():
    oled = OLED(60)
    display = oled
else:
    pass

# 3 rgb leds
rgb = NeoPixel(Pin(17, Pin.OUT), 3, 3, 1, brightness=1)
rgb.write()

# light sensor
light = ADC(Pin(39))
light.atten(light.ATTN_11DB)

# sound sensor
sound = ADC(Pin(36))
sound.atten(sound.ATTN_11DB)

# Button<-machine.Pin
#   ├-event_pressed:Callable(Pin)
#   ├-event_released:Callable(Pin)
#   ├-schedule_event:bool #是否在micropython.schedule内运行事件函数
#   ├-is_pressed()->bool
#   ├-__irq_handler(Pin) #内部中断处理函数
#   └-*machine.Pin #此类集成machine.Pin类
class Button(Pin):
    def __init__(self,pin):
        super().__init__(pin,Pin.IN,Pin.PULL_UP)
        self.event_pressed=lambda pin:None
        self.event_released=lambda pin:None
        self.schedule_event=False
        self.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.__irq_handler)
    def is_pressed(self):
        return not self.value()
    def __irq_handler(self,pin):
        if self.value():
            event=self.event_released
        else:
            event=self.event_pressed
        if self.schedule_event:
            schedule(event,pin)
        else:
            event(pin)

#buttons
button_a = button_A = Button(0)#Pin.P5
button_b = button_B = Button(2)#Pin.P11

# Touch<-machine.TouchPad
#   ├-event_pressed:Callable(Pin)
#   ├-event_released:Callable(Pin)
#   ├-schedule_event:bool #是否在micropython.schedule内运行事件函数
#   ├-value:Literal[0，1] #当前值
#   ├-is_pressed()->bool #若触摸键按下则返回1，否则返回0
#   ├-__irq_handler(Pin) #内部中断处理函数
#   └-*machine.TouchPad #此类集成machine.TouchPad类
class Touch(TouchPad):
    def __init__(self,pin):
        super().__init__(pin)
        self.value=0
        self.event_pressed=lambda pin:None
        self.event_released=lambda pin:None
        self.schedule_event=False
        self.irq(self.__irq_handler)
    def __irq_handler(self,value):
        self.value=value
        if value:
            event=self.event_pressed
        else:
            event=self.event_released
        if self.schedule_event:
            schedule(event,value)
        else:
            event(value)
    def is_pressed(self):
        return bool(self.value)
    

#touchpads
touchpad_p = touchPad_P = Touch(Pin(27))#Pin.P23
touchpad_y = touchPad_Y = Touch(Pin(14))#Pin.P24
touchpad_t = touchPad_T = Touch(Pin(12))#Pin.P25
touchpad_h = touchPad_H = Touch(Pin(13))#Pin.P26
touchpad_o = touchPad_O = Touch(Pin(15))#Pin.P27
touchpad_n = touchPad_N = Touch(Pin(4)) #Pin.P28
#from mpython.py，有改动，新增可返回弧度制的
class MOTION(object):
    def __init__(self):
        self.i2c = i2c
        addr = self.i2c.scan()
        if 38 in addr:
            MOTION.chip = 1  # MSA300
            MOTION.IIC_ADDR = 38
        elif 107 in addr:
            MOTION.chip = 2  # QMI8658
            MOTION.IIC_ADDR = 107
        else:
            raise OSError("MOTION init error")
        if(MOTION.chip == 1):
            pass
        elif(MOTION.chip == 2):
            MOTION._writeReg(0x60, 0x01) # soft reset regist value.
            time.sleep_ms(20)
            MOTION._writeReg(0x02, 0x60) # Enabe reg address auto increment auto
            MOTION._writeReg(0x08, 0x03) # Enable accel and gyro
            MOTION._writeReg(0x03, 0x1c) # accel range:4g ODR 128HZ
            MOTION._writeReg(0x04, 0x40) # gyro ODR 8000HZ, FS 256dps
            MOTION._writeReg(0x06, 0x55) # Enable accel and gyro Low-Pass Filter
        # print('Motion init finished!')

    # @staticmethod
    def _readReg(reg, nbytes=1):
        return i2c.readfrom_mem(MOTION.IIC_ADDR, reg, nbytes)

    # @staticmethod
    def _writeReg(reg, value):
        i2c.writeto_mem(MOTION.IIC_ADDR, reg, value.to_bytes(1, 'little'))

    def get_fw_version(self):
        if(self.chip==1):
            pass
        elif(self.chip==2):
            MOTION._writeReg(0x0a, 0x10) # send ctrl9R read FW cmd
            while True:
                if (MOTION._readReg(0x2F, 1)[0] & 0X01) == 0X01:
                    break
            buf = MOTION._readReg(0X49, 3)
            # print(buf[0])
            # print(buf[1])
            # print(buf[2])
        
    class Accelerometer():
        """MSA300"""
        # Range and resolustion
        RANGE_2G = const(0)
        RANGE_4G = const(1)
        RANGE_8G = const(2)
        RANGE_16G = const(3)
        RES_14_BIT = const(0) 
        RES_12_BIT = const(1)
        RES_10_BIT = const(2)
        # Event
        TILT_LEFT = const(0)
        TILT_RIGHT = const(1)
        TILT_UP = const(2)
        TILT_DOWN = const(3)
        FACE_UP = const(4)
        FACE_DOWN = const(5)
        SINGLE_CLICK = const(6)
        DOUBLE_CLICK = const(7)
        FREEFALL = const(8)

        """QMI8658C"""
        # Range and resolustion
        # QMI8658C_RANGE_2G = const(0x00)
        # QMI8658C_RANGE_4G = const(0x10)
        # QMI8658C_RANGE_8G = const(0x20)
        # QMI8658C_RANGE_16G = const(0x40)

        def __init__(self):
            if(MOTION.chip==1):
                self.set_resolution(MOTION.Accelerometer.RES_10_BIT)
                self.set_range(MOTION.Accelerometer.RANGE_2G)
                MOTION._writeReg(0x12, 0x03)               # polarity of y,z axis,
                MOTION._writeReg(0x11, 0)                  # set power mode = normal
                # interrupt
                MOTION._writeReg(0x16, 0x70)      # int enabled: Orient | S_TAP | D_TAP 
                MOTION._writeReg(0x17, 0x08)      # int enabled: Freefall
                MOTION._writeReg(0x19, 0x71)      # int1 map to: Orient, S_TAP, D_TAP, Freefall
                MOTION._writeReg(0x20, 0x02)      # int1 active level = 0, output = OD
                MOTION._writeReg(0x21, 0x0C)      # int tempoary latched 25ms
                # freefall:
                #   single mode: |acc_x| < Threshold && |acc_y| < Threshold && |acc_z| < Threshold, at least time > Duration
                #   sum mode: |acc_x| + |acc_y| + |acc_z| < Threshold, at least time > Duration
                MOTION._writeReg(0x22, 20)    # Freefall Duration:(n+1)*2ms, range from 2ms to 512ms
                MOTION._writeReg(0x23, 48)    # Freefall Threshold: n*7.81mg
                MOTION._writeReg(0x24, 0x01)  # Freefall mode = 0-singlemode;hysteresis = n*125mg
                # tap:
                MOTION._writeReg(0x2A, 0x06)  # Tap duration:quit = 30ms, shock=50ms, time window for secent shock=500ms
                MOTION._writeReg(0x2B, 0x0A)  # Tap threshold = 10*[62.5mg@2G | 125mg@4G | 250mg@8G | 500mg@16g]
                # Orient
                MOTION._writeReg(0x2C, 0x18)  # Orient hysteresis= 1*62.5mg; 
                                            #        block mode = 10 z_axis blocking or slope in any axis > 0.2g;
                                            #        orient mode = 00-symetrical
                MOTION._writeReg(0x2D, 8)     # Z-axis block
                # int pin irq register
                self.int = Pin(37, Pin.IN)
                self.int.irq(trigger=Pin.IRQ_FALLING, handler=self.irq)
                # event handler 
                self.event_tilt_up = None
                self.event_tilt_down = None
                self.event_tilt_left = None
                self.event_tilt_right = None
                self.event_face_up = None
                self.event_face_down = None
                self.event_single_click = None
                self.event_double_click = None
                self.event_freefall = None
            elif(MOTION.chip==2):
                # 设置偏移值
                self.x_offset = 0
                self.y_offset = 0
                self.z_offset = 0
                self.get_nvs_offset()
                try:
                    id =  MOTION._readReg(0x0, 2)
                except:
                    pass
                self.set_range(MOTION.Accelerometer.RANGE_2G) #设置默认分辨率+-2g
                self.int = Pin(37, Pin.IN)
                self.int.irq(trigger=Pin.IRQ_FALLING, handler=self.irq)
                # event handler 
                self.wom = None
            

        def irq(self, arg):
            if(MOTION.chip==1):
                reg_int = MOTION._readReg(0x09)[0]
                reg_orent = MOTION._readReg(0x0C)[0]
                # orient_int
                if (reg_int & 0x40):
                    if ((reg_orent & 0x30) == 0x00 and self.event_tilt_left is not None):
                        schedule(self.event_tilt_left, self.TILT_LEFT)
                    if ((reg_orent & 0x30) == 0x10 and self.event_tilt_right is not None):
                        schedule(self.event_tilt_right, self.TILT_RIGHT)
                    if ((reg_orent & 0x30) == 0x20 and self.event_tilt_up is not None):
                        schedule(self.event_tilt_up, self.TILT_UP)
                    if ((reg_orent & 0x30) == 0x30 and self.event_tilt_down is not None):
                        schedule(self.event_tilt_down, self.TILT_DOWN)
                    if ((reg_orent & 0x40) == 0x00 and self.event_face_up):
                        schedule(self.event_face_up, self.FACE_UP)
                    if ((reg_orent & 0x40) == 0x40 and self.event_face_down):
                        schedule(self.event_face_down, self.FACE_DOWN)
                # single tap
                if (reg_int & 0x20):
                    if (self.event_single_click is not None):
                        schedule(self.event_single_click, self.SINGLE_CLICK)
                # double tap
                if (reg_int & 0x10):
                    if (self.event_double_click is not None):
                        schedule(self.event_double_click, self.DOUBLE_CLICK)
                # freefall
                if (reg_int & 0x01):
                    if (self.event_freefall is not None):
                        schedule(self.event_freefall, self.FREEFALL)
                # print("acc sensor interrupt, because 0x%2x, orient = 0x%2x" % (reg_int, reg_orent))
            elif(MOTION.chip==2):  
                flag = MOTION._readReg(0x2F, 1)[0]
                if (flag & 0x04) == 0x04:
                    print('wom int trigged.')

        def wom_config(self):
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                MOTION._writeReg(0x60, 0x01) # soft reset regist value.
                time.sleep_ms(20)
                MOTION._writeReg(0x08, 0x0) # disable all sensor
                MOTION._writeReg(0x03, 0x1c) # accel range:4g ODR 128HZ
                MOTION._writeReg(0x0B, 0xfF) # CAL_L WoM Threshold(1mg/LSB resolution)
                MOTION._writeReg(0x0C, 0x8F) # CAL_H WoM (INT1 blank time 0x1f)
                MOTION._writeReg(0x0A, 0x08)
                while True:
                    if (MOTION._readReg(0x2F, 1)[0] & 0X01) == 0X01:
                        break
                MOTION._writeReg(0x08, 0x01) # enable accel

        def set_resolution(self, resolution):# set data output rate
            if(MOTION.chip==1):
                format = MOTION._readReg(0x0f, 1)
                format = format[0] & ~0xC
                format |= (resolution << 2)
                MOTION._writeReg(0x0f, format)
            elif(MOTION.chip==2):
                self.odr = resolution
                format = MOTION._readReg(0x03, 1)
                format = format[0] & 0xf0
                format |= (resolution & 0x0f)
                MOTION._writeReg(0x03, format)
                
        def set_range(self, range):
            if(MOTION.chip==1):
                self.range = range
                format = MOTION._readReg(0x0f, 1)
                format = format[0] & ~0x3
                format |= range
                MOTION._writeReg(0x0f, format)
            elif(MOTION.chip==2):
                if(range==3):
                    range = 64 #0x40
                else:
                    range = range << 4
                self.FS = 2*(2**(range >> 4))
                format = MOTION._readReg(0x03, 1)
                format = format[0] & 0x8F
                format |= range
                MOTION._writeReg(0x03, format)

        def set_offset(self, x=None, y=None, z=None):
            if(MOTION.chip==1):
                for i in (x, y, z):
                    if i is not None:
                        if i < -1 or i > 1:
                            raise ValueError("out of range,only offset 1 gravity")
                if x is not None:
                    MOTION._writeReg(0x39, int(round(x/0.0039)))
                elif y is not None:
                    MOTION._writeReg(0x38, int(round(y/0.0039)))
                elif z is not None:
                    MOTION._writeReg(0x3A, int(round(z/0.0039)))
            elif(MOTION.chip==2):
                for i in (x, y, z):
                    if i is not None:
                        if i < -16 or i > 16:
                            raise ValueError("超出调整范围!!!")
                if x is not None:
                    self.x_offset = x
                    self.set_nvs_offset("x", x)
                if y is not None:
                    self.y_offset = y
                    self.set_nvs_offset("y", y)
                if z is not None:
                    self.z_offset = z
                    self.set_nvs_offset("z", z)
                
        def get_x(self):
            if(MOTION.chip==1):
                retry = 0
                if (retry < 5):
                    try:
                        buf = MOTION._readReg(0x02, 2)
                        x = ustruct.unpack('h', buf)[0]
                        return x / 4 / 4096 * 2**self.range
                    except:
                        retry = retry + 1
                else:
                    raise Exception("i2c read/write error!")
            elif(MOTION.chip==2):
                buf = MOTION._readReg(0x35, 2)
                x = ustruct.unpack('<h', buf)[0]
                return (x * self.FS) / 32768 + self.x_offset

        def get_y(self):
            if(MOTION.chip==1):
                retry = 0
                if (retry < 5):
                    try:
                        buf = MOTION._readReg(0x04, 2)
                        y = ustruct.unpack('h', buf)[0]
                        return y / 4 / 4096 * 2**self.range
                    except:
                        retry = retry + 1
                else:
                    raise Exception("i2c read/write error!")
            elif(MOTION.chip==2):
                buf = MOTION._readReg(0x37, 2)
                y = ustruct.unpack('<h', buf)[0]
                return (y * self.FS) / 32768  + self.y_offset

        def get_z(self):
            if(MOTION.chip==1):
                retry = 0
                if (retry < 5):
                    try:
                        buf = MOTION._readReg(0x06, 2)
                        z = ustruct.unpack('h', buf)[0]
                        return z / 4 / 4096 * 2**self.range
                    except:
                        retry = retry + 1
                else:
                    raise Exception("i2c read/write error!")
            elif(MOTION.chip==2):
                buf = MOTION._readReg(0x39, 2)
                z = ustruct.unpack('<h', buf)[0]
                return (z * self.FS) / 32768 + self.z_offset
                # return -(z * self.FS) / 32768
     
        def roll_pitch_angle(self,degress=True):
            x, y, z = self.get_x(), self.get_y(), -self.get_z()
            # vector normalize
            mag = math.sqrt(x ** 2 + y ** 2+z ** 2)
            x /= mag
            y /= mag
            z /= mag
            
            if degress:
                roll = math.degrees(-math.asin(y))
                pitch = math.degrees(math.atan2(x, z))
            else:
                roll = -math.asin(y)
                pitch = math.atan2(x, z)

            return roll, pitch
        
        def get_nvs_offset(self):
            try:
                tmp = NVS("offset_a")
                self.x_offset = round(tmp.get_i32("x")/1e5, 5)
                self.y_offset = round(tmp.get_i32("y")/1e5, 5)
                self.z_offset = round(tmp.get_i32("z")/1e5, 5)
            except OSError as e:
                # print('Accelerometer get_nvs_offset:',e)
                # self.x_offset = 0
                # self.y_offset = 0
                # self.z_offset = 0
                self.set_offset(0,0,0)
        
        def set_nvs_offset(self, key, value):
            try:
                nvs = NVS("offset_a")
                nvs.set_i32(key, int(value*1e5))
                nvs.commit()
            except OSError as e:
                print('Gyroscope set_nvs_offset error:',e)

    class Gyroscope():
        # gyro full scale
        RANGE_16_DPS =  const(0x00)
        RANGE_32_DPS =  const(0x10)
        RANGE_64_DPS =  const(0x20)
        RANGE_128_DPS =  const(0x30)
        RANGE_256_DPS =  const(0x40)
        RANGE_512_DPS =  const(0x50)
        RANGE_1024_DPS = const(0x60)
        RANGE_2048_DPS = const(0x70)

        def __init__(self):
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                # 设置偏移值
                self.x_offset = 0
                self.y_offset = 0
                self.z_offset = 0
                self.get_nvs_offset()
                self.set_range(MOTION.Gyroscope.RANGE_256_DPS)

        def set_range(self, range):
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                self.FS = 16*(2**(range >> 4))        
                format = MOTION._readReg(0x04, 1)
                format = format[0] & 0x8F
                format |= range
                MOTION._writeReg(0x04, format)

        def set_ODR(self, odr):  # set data output rate
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                self.odr = odr
                format = MOTION._readReg(0x04, 1)
                format = format[0] & 0xF0
                format |= odr
                MOTION._writeReg(0x04, format)

        def get_x(self):
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                buf = MOTION._readReg(0x3b, 2)
                x = ustruct.unpack('<h', buf)[0]
                return (x * self.FS) / 32768 + self.x_offset

        def get_y(self):
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                buf = MOTION._readReg(0x3d, 2)
                y = ustruct.unpack('<h', buf)[0]
                return (y * self.FS) / 32768 + self.y_offset

        def get_z(self):
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                buf = MOTION._readReg(0x3f, 2)
                z = ustruct.unpack('<h', buf)[0]
                return (z * self.FS) / 32768 + self.z_offset
        
        def set_offset(self, x=None, y=None, z=None):
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                for i in (x, y, z):
                    if i is not None:
                        if i < -4096 or i > 4096:
                            raise ValueError("超出调整范围!!!")
                if x is not None:
                    self.x_offset = x
                    self.set_nvs_offset("x", x)
                if y is not None:
                    self.y_offset = y
                    self.set_nvs_offset("y", y)
                if z is not None:
                    self.z_offset = z
                    self.set_nvs_offset("z", z)

        def get_nvs_offset(self):
            if(MOTION.chip==1):
                pass
            elif(MOTION.chip==2):
                try:
                    tmp = NVS("offset_g")
                    self.x_offset = round(tmp.get_i32("x")/1e5, 5)
                    self.y_offset = round(tmp.get_i32("y")/1e5, 5)
                    self.z_offset = round(tmp.get_i32("z")/1e5, 5)
                except OSError as e:
                    # print('Gyroscope get_nvs_offset:',e)
                    self.set_offset(0,0,0)
                    # self.x_offset = 0
                    # self.y_offset = 0
                    # self.z_offset = 0

        def set_nvs_offset(self, key, value):
            try:
                nvs = NVS("offset_g")
                nvs.set_i32(key, int(value*1e5))
                nvs.commit()
            except OSError as e:
                print('Gyroscope set_nvs_offset error:',e)

    
motion = MOTION()
accelerometer = motion.Accelerometer()
gyroscope = motion.Gyroscope()
#from mpython.py，有改动，新增自动存储校准值
class Magnetic(object):
    """ MMC5983MA driver """
    """ MMC5603NJ driver 20211028替换"""
    def __init__(self,addr):
        self.addr = addr
        self.i2c = i2c
        self._judge_id()
        time.sleep_ms(5)
        if (self.product_ID==48):
            pass  # MMC5983MA
        elif (self.product_ID==16):
            pass  # MMC5603NJ
        else:
            raise OSError("Magnetic init error")
        """ MMC5983MA driver """
        # 传量器裸数据，乘0.25后转化为mGS
        self.raw_x = 0.0
        self.raw_y = 0.0
        self.raw_z = 0.0
        self.offset_tmp=NVS("mag_offset")
        try:
            self.offset_x = self.__getint(self.offset_tmp.get_i32("x"))
            self.offset_y = self.__getint(self.offset_tmp.get_i32("y"))
            self.offset_z = self.__getint(self.offset_tmp.get_i32("z"))
        except OSError:
            # 校准后的偏移量, 基于裸数据
            self.offset_x = 0.0 
            self.offset_y = 0.0
            self.offset_z = 0.0
            self.offset_tmp.set_i32("x", self.__packint(0.0))
            self.offset_tmp.set_i32("y", self.__packint(0.0))
            self.offset_tmp.set_i32("z", self.__packint(0.0))
            self.offset_tmp.commit()
        self.peeling_tmp=NVS("mag_peeling")
        try:
            self.peeling_x = self.__getint(self.peeling_tmp.get_i32("x"))
            self.peeling_y = self.__getint(self.peeling_tmp.get_i32("y"))
            self.peeling_z = self.__getint(self.peeling_tmp.get_i32("z"))
            self.is_peeling = 1
        except OSError:
            # 去皮偏移量，类似电子秤去皮功能，基于裸数据。
            self.peeling_x = 0.0
            self.peeling_y = 0.0
            self.peeling_z = 0.0
            self.peeling_tmp.set_i32("x", self.__packint(0.0))
            self.peeling_tmp.set_i32("y", self.__packint(0.0))
            self.peeling_tmp.set_i32("z", self.__packint(0.0))
            self.peeling_tmp.commit()
            self.is_peeling = 0
        if (self.chip==1):
            self.i2c.writeto(self.addr, b'\x09\x20\xbd\x00', True)
        """ MMC5603NJ driver """
        if (self.chip==2):
            self._writeReg(0x1C, 0x80)#软件复位
            time.sleep_ms(100)
            self._writeReg(0x1A, 255)
            self._writeReg(0x1B, 0b10100001)
            self._writeReg(0x1C, 0b00000011)
            self._writeReg(0x1D, 0b10010000)
            time.sleep_ms(100)
    def __packint(self,float):
        #用一种不按套路出牌的方式强制将浮点数转换为整数，用于NVS存储值
        return ustruct.unpack("i",ustruct.pack("f",float))[0]
    def __getint(self,int):
        #用一种不按套路出牌的方式强制将__packint用于转换的浮点数转换后的整数转换为浮点数，用于NVS存储值
        ustruct.unpack("f",ustruct.pack("i",int))[0]
    def _readReg(self, reg, nbytes=1):
        return i2c.readfrom_mem(self.addr, reg, nbytes)

    def _writeReg(self, reg, value):
        i2c.writeto_mem(self.addr, reg, value.to_bytes(1, 'little')) 

    def _set_offset(self):
        if(self.chip == 1):
            self.i2c.writeto(self.addr, b'\x09\x08', True)  #set
            self.i2c.writeto(self.addr, b'\x09\x01', True)
            while True:
                self.i2c.writeto(self.addr, b'\x08', False)
                buf = self.i2c.readfrom(self.addr, 1)
                status = ustruct.unpack('B', buf)[0]
                if(status & 0x01):
                    break
            self.i2c.writeto(self.addr, b'\x00', False)
            buf = self.i2c.readfrom(self.addr, 6)
            data = ustruct.unpack('>3H', buf)

            self.i2c.writeto(self.addr, b'\x09\x10', True)  #reset

            self.i2c.writeto(self.addr, b'\x09\x01', True)
            while True:
                self.i2c.writeto(self.addr, b'\x08', False)
                buf = self.i2c.readfrom(self.addr, 1)
                status = ustruct.unpack('B', buf)[0]
                if(status & 0x01):
                    break
            self.i2c.writeto(self.addr, b'\x00', False)
            buf = self.i2c.readfrom(self.addr, 6)
            data1 = ustruct.unpack('>3H', buf)

            self.x_offset = (data[0] + data1[0])/2
            self.y_offset = (data[1] + data1[1])/2
            self.z_offset = (data[2] + data1[2])/2
        elif(self.chip == 2):
            pass
    
    def _get_raw(self):
        if (self.chip == 1):
            retry = 0
            if (retry < 5):
                try:
                    self.i2c.writeto(self.addr, b'\x09\x08', True)  #set

                    self.i2c.writeto(self.addr, b'\x09\x01', True)
                    while True:
                        self.i2c.writeto(self.addr, b'\x08', False)
                        buf = self.i2c.readfrom(self.addr, 1)
                        status = ustruct.unpack('B', buf)[0]
                        if(status & 0x01):
                            break
                    self.i2c.writeto(self.addr, b'\x00', False)
                    buf = self.i2c.readfrom(self.addr, 6)
                    data = ustruct.unpack('>3H', buf)

                    self.i2c.writeto(self.addr, b'\x09\x10', True)  #reset

                    self.i2c.writeto(self.addr, b'\x09\x01', True)
                    while True:
                        self.i2c.writeto(self.addr, b'\x08', False)
                        buf = self.i2c.readfrom(self.addr, 1)
                        status = ustruct.unpack('B', buf)[0]
                        if(status & 0x01):
                            break
                    self.i2c.writeto(self.addr, b'\x00', False)
                    buf = self.i2c.readfrom(self.addr, 6)
                    data1 = ustruct.unpack('>3H', buf)

                    self.raw_x = -((data[0] - data1[0])/2)
                    self.raw_y = -((data[1] - data1[1])/2)
                    self.raw_z = -((data[2] - data1[2])/2)
                    # print(str(self.raw_x) + "   " + str(self.raw_y) + "  " + str(self.raw_z))
                except:
                    retry = retry + 1
            else:
                raise Exception("i2c read/write error!")     
        elif(self.chip == 2):
            retry = 0
            if (retry < 5):
                try:
                    _raw_x = 0
                    _raw_y = 0
                    _raw_z = 0
                    while True:
                        self._writeReg(0x1B,0b10100001)
                        time.sleep_ms(10)
                        buf = self._readReg(0x18, 1)
                        status = buf[0]
                        # print('status:',status)
                        if(status & 0x40):
                            break
                    # self.i2c.writeto(self.addr, b'\x00', False)
                    # buf = self.i2c.readfrom(self.addr, 9)
                    buf = self._readReg(0x00, 9)

                    _raw_x |= buf[0] << 12
                    _raw_x |= buf[1] << 4
                    # _raw_x |= buf[6] << 0
                    _raw_x |= buf[6] >> 4
                    self.raw_x = _raw_x

                    _raw_y |= buf[2] << 12
                    _raw_y |= buf[3] << 4
                    # _raw_y |= buf[7] << 0
                    _raw_y |= buf[7] >> 4
                    self.raw_y = _raw_y

                    _raw_z |= buf[4] << 12
                    _raw_z |= buf[5] << 4
                    # _raw_z |= buf[8] << 0
                    _raw_z |= buf[8] >> 4
                    self.raw_z = _raw_z
                    

                except:
                    retry = retry + 1
            else:
                raise Exception("i2c read/write error!")

    def peeling(self,innvs=True):
        '''
        去除磁场环境
        '''
        self._get_raw()
        raw_x = self.raw_x
        raw_y = self.raw_y
        raw_z = self.raw_z
        self.peeling_x = raw_x
        self.peeling_y = raw_y
        self.peeling_z = raw_z
        self.peeling_tmp.set_i32("x",self.__packint(raw_x))
        self.peeling_tmp.set_i32("y",self.__packint(raw_y))
        self.peeling_tmp.set_i32("z",self.__packint(raw_z))
        self.peeling_tmp.commit()

        self.is_peeling = 1

    def clear_peeling(self):
        self.peeling_x = 0.0
        self.peeling_y = 0.0
        self.peeling_z = 0.0
        self.peeling_tmp.set_i32("x",self.__packint(0.0))
        self.peeling_tmp.set_i32("y",self.__packint(0.0))
        self.peeling_tmp.set_i32("z",self.__packint(0.0))
        self.peeling_tmp.commit()
        self.is_peeling = 0

    def get_x(self):
        if (self.chip == 1):
            self._get_raw()
            return self.raw_x * 0.25
        if (self.chip == 2):
            self._get_raw()
            return -0.0625 * (self.raw_x - self.cali_offset_x - 524288)
            # return (self.raw_x - 524288)/16384

    def get_y(self):
        if (self.chip == 1):
            self._get_raw()
            return self.raw_y * 0.25
        if (self.chip == 2):
            self._get_raw()
            return -0.0625 * (self.raw_y - self.cali_offset_y - 524288)
            # return (self.raw_y - 524288)/16384

    def get_z(self):
        if (self.chip == 1):
            self._get_raw()
            return self.raw_z * 0.25 
        if (self.chip == 2):
            self._get_raw()
            return 0.0625 * (self.raw_z - self.cali_offset_z - 524288)
            # return (self.raw_z - 524288)/16384

    def get_field_strength(self):
        if(self.chip==1):
            self._get_raw()
            if self.is_peeling == 1:
                return (math.sqrt((self.raw_x - self.peeling_x)*(self.raw_x - self.peeling_x) + (self.raw_y - self.peeling_y)*(self.raw_y - self.peeling_y) + (self.raw_z - self.peeling_z)*(self.raw_z - self.peeling_z)))*0.25
            return (math.sqrt(self.raw_x * self.raw_x + self.raw_y * self.raw_y + self.raw_z * self.raw_z))*0.25
        elif(self.chip==2):
            self._get_raw()
            if self.is_peeling == 1:
                return (math.sqrt(math.pow(self.raw_x - self.peeling_x -524288, 2) + pow(self.raw_y - self.peeling_y -524288, 2) + pow(self.raw_z - self.peeling_z -524288, 2)))*0.0625
            return (math.sqrt(math.pow(self.get_x(), 2) + pow(self.get_y(), 2) + pow(self.get_z(), 2)))

    def calibrate(self):
        oled.fill(0)
        oled.DispChar("步骤1:", 0,0,1)
        oled.DispChar("如图",0,26,1)
        oled.DispChar("转几周",0,43,1)
        oled.bitmap(64,0,calibrate_img.rotate,64,64,1)
        oled.show()
        self._get_raw()
        min_x = max_x = self.raw_x
        min_y = max_y = self.raw_y
        min_z = max_z = self.raw_z
        ticks_start = time.ticks_ms()
        while (time.ticks_diff(time.ticks_ms(), ticks_start) < 15000) :
            self._get_raw()
            min_x = min(self.raw_x, min_x)
            min_y = min(self.raw_y, min_y)
            max_x = max(self.raw_x, max_x)
            max_y = max(self.raw_y, max_y)
            time.sleep_ms(100)
        self.cali_offset_x = (max_x + min_x) / 2
        self.cali_offset_y = (max_y + min_y) / 2
        print('cali_offset_x: ' + str(self.cali_offset_x) + '  cali_offset_y: ' + str(self.cali_offset_y))
        oled.fill(0)
        oled.DispChar("步骤2:", 85,0,1)
        oled.DispChar("如图",85,26,1)
        oled.DispChar("转几周",85,43,1)
        oled.bitmap(0,0,calibrate_img.rotate1,64,64,1)
        oled.show()
        ticks_start = time.ticks_ms()
        while (time.ticks_diff(time.ticks_ms(), ticks_start) < 15000) :
            self._get_raw()
            min_z = min(self.raw_z, min_z)
            max_z = max(self.raw_z, max_z)
            time.sleep_ms(100)
        self.cali_offset_z = (max_z + min_z) / 2
  
        print('cali_offset_z: ' + str(self.cali_offset_z))

        oled.fill(0)
        oled.DispChar("校准完成", 40,24,1)
        oled.show()
        oled.fill(0)

    def get_heading(self):
        if(self.chip==1):
            self._get_raw()
            temp_x = self.raw_x - self.cali_offset_x
            temp_y = self.raw_y - self.cali_offset_y
            # temp_z = self.raw_z - self.cali_offset_z
            heading = math.atan2(temp_y, -temp_x) * (180 / 3.14159265) + 180
            return heading
        else:
            # self._get_raw()
            # heading = math.atan2(temp_y, -temp_x) * (180 / 3.14159265) + 180 + 3
            heading = math.atan2(self.get_y(), -self.get_x()) * (180 / 3.14159265) + 180 + 3
            return heading
        
    def _get_temperature(self):
        if(self.chip==1):
            retry = 0
            if (retry < 5):
                try:
                    self.i2c.writeto(self.addr, b'\x09\x02', True)
                    while True:
                        self.i2c.writeto(self.addr, b'\x08', False)
                        buf = self.i2c.readfrom(self.addr, 1)
                        status = ustruct.unpack('B', buf)[0]
                        if(status & 0x02):
                            break
                    self.i2c.writeto(self.addr, b'\x07', False)
                    buf = self.i2c.readfrom(self.addr, 1)
                    temp = (ustruct.unpack('B', buf)[0])*0.8 -75
                    # print(data)
                    return temp
                except:
                    retry = retry + 1
            else:
                raise Exception("i2c read/write error!")   
        elif(self.chip == 2):
            pass

    def _get_id(self):
        if (self.chip==1):
            retry = 0
            if (retry < 5):
                try:
                    self.i2c.writeto(self.addr, bytearray([0x2f]), False)
                    buf = self.i2c.readfrom(self.addr, 1, True)
                    print(buf)
                    id = ustruct.unpack('B', buf)[0]
                    return id
                except:
                    retry = retry + 1
            else:
                raise Exception("i2c read/write error!")
        elif (self.chip==2):
            retry = 0
            if (retry < 5):
                try:
                    self.i2c.writeto(self.addr, bytearray([0x39]), False)
                    buf = self.i2c.readfrom(self.addr, 1, True)
                    id = ustruct.unpack('B', buf)[0]
                    return id
                except:
                    retry = retry + 1
            else:
                raise Exception("i2c read/write error!")

    def _judge_id(self):
        """
        判断product_ID
        """
        retry = 0
        if (retry < 5):
            try:
                self.i2c.writeto(self.addr, bytearray([0x39]), False)
                buf = self.i2c.readfrom(self.addr, 1, True)
                id = ustruct.unpack('B', buf)[0]
                if(id == 16):
                    self.chip = 2
                    self.product_ID = 16
                else:
                    self.chip = 1
                    self.product_ID = 48
            except:
                retry = retry + 1
        else:
            raise Exception("i2c read/write error!") 

# Magnetic
if 48 in i2c.scan():
    magnetic = Magnetic(48)

def numberMap(inputNum, bMin, bMax, cMin, cMax):
    return ((cMax - cMin) / (bMax - bMin)) * (inputNum - bMin) + cMin