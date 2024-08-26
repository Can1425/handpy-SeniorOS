# 关于SmartWifi

## 何为SmartWifi?

SmartWifi是一个基于ESP32-Handpy的Wifi连接模块,通过网络HTML页面,可以轻松帮助handpy连接到wifi

smartwifi位于./code/SeniorOS/system/smart_wifi.py

## 如何使用?

### 1.打开handpy

### 2.用手机/电脑连接 SeniorOS-WIFI

**注意!!!** 此SeniorOS-WIFI仅提供连接网络的HTML页面服务,**不提供互联网服务!**

### 3.打开浏览器,输入192.168.4.1

**注意** 请在浏览器地址框输入,而不是在搜索框输入,如犯此错误,我们团队不会负责

### 4.输入wifi名称和密码

WiFi名称输入---- 在 "Type your wifiSSID" 内填写您的WiFi名称
点击旁边的upload按钮，您的WiFi名称将会存储到handpy
WiFi密码输入----在 "Type your wifiPassword" 内填写您的WiFi密码
点击旁边的upload按钮，您的WiFi密码将会存储到handpy

### 5.连接

请点击浏览器出现的"exit"按钮,这时您可以关闭浏览器,handpy将会自动连接到wifi.

**注意** 如果您直接关闭浏览器,handpy将不会会连接到wifi,并且会崩溃 我们 ***一律不负责***

### 6.连接成功

连接成功后,handpy将会在串口输出

如果报错，请重启handpy并从**步骤1**开始

## 类的调用

```python
import smart_wifi#导入smartwifi模块

smart_wifi.main()#main()函数是smartwifi模块的入口函数,调用该函数即可使用smartwifi模块,这时您可以从"如何使用"中的第一步开始
```
## 关于

想法/尝试:***CycleBai***

代码开发:***LP_OVER***

鸣谢:***CycleBai***/***Can1425***

邮箱:***d110101010101@outlook.com***