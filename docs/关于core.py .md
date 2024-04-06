# DataCtrl类
|名称|类型|作用|传参|返回值|备注|
|-|-|-|-|-|-|
|\_\_init\_\_|func|初始化|.fos文件目录路径|已初始化的类|/|
|Get|func|获取数据|fos数据名|对应.fos文件内容|/|
|data|dict|数据存储实际对象|fos数据名,fos数据内容|获取全部.fos文件数据|/|
|dataFolderPath|str|.fos文件目录路径|/|/|/|
|Write|func|写入数据|_见下_|全部.fos文件数据|/|

## DataCtrl.Write

传参: 数据名,数据内容,一次性设置(singleUseSet)=False,需要重启生效(needReboot)=False

singleUseSet参数:一次性设置 不会实际写入文件 此选参为True时 needReboot不生效

needReboot参数:当该值为True时 不修改实际运行值 

# File_Path_Factory

|名称|类型|作用|传参|返回值|备注|
|-|-|-|-|-|-|
|Replace2Backslash|func|替换斜杠为反斜杠|字符串|替换后的字符串|/|
|FileIsExist|func|判断文件是否存在|文件路径|True/False|/|
|IsDir|func|判断是否为文件夹|文件路径|True/False|/|

# GetTime
|名称|类型|作用|传参|返回值|备注|
|-|-|-|-|-|-|
|Year|func|获取当前年份|/|当前年份|/|
|Month|func|获取当前月份|/|当前月份|/|
|Week|func|获取当前星期|/|当前星期|/|
|Day|func|获取当前日期|/|当前日期|/|
|Hour|func|获取当前小时|/|当前小时|/|
|Min|func|获取当前分钟|/|当前分钟|/|
|Sec|func|获取当前秒数|/|当前秒数|/|

# FullCollect

类型：函数

对RAM进行彻底清理 直至下次清理为清理出任何内容

无传参 返回值为目前可用RAM

# GetDeviceID

类型：函数

获取具有唯一性的设备ID

传参：mode:0/1
对应不同的ID生成方式
返回值为设备ID

> 注： 此func仍使用了回调函数便于dever们自定义 各位可以自行开发用法...
# Screenshot

|名称|类型|作用|传参|返回值|备注|
|-|-|-|-|-|-|
|CopyFrameBuf|func|通过复制缓冲区的方式截屏|截屏保存位置,oled对象|/|/|
|Enumerate|func|通过枚举缓冲区的方式截屏|截屏保存位置,oled对象|/|/|

## 关于OLED对象
>这是一个可选值 一般情况下会自动指定为`mpython.oled`

为了 节省RAM/使FOS.Core具有普适性 我们选择将使用到的oled操作对象以 **「回调函数」** 的形式作为参数传入函数体

> 关于回调函数一词解释：<https://blog.csdn.net/yushuaigee/article/details/86313697>

此值需要满足以下3个条件：
1. 是类 （必须满足此项）
2. 含有类变量：buffer   且可以被函数正确识别操作（使用 func`CopyFrameBuf` 时 必须满足此项）
3. 含有类函数：pixel    且可以被函数正确识别操作（使用 func`Enumerate` 时 必须满足此项）


## Enumerate

包含两种截屏算法（速度最快：`fast`,RAM占用最小：`ram`） 但算法思想一样 仅修改了缓冲区的操作

可以通过控制`./tools/ReplaceExpression.py`下的`constData["screenshodMethod"]`决定其使用算法