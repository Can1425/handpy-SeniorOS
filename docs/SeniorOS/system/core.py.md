# core.py

## `DataCtrl` 类
用于管理和操作 `data/` 目录下的 `.sros` 扩展名文件。

### 方法

#### `__init__(self, dataFolderPath)`
- **参数:**
  - `dataFolderPath` (str): 文件夹路径（路径结尾必须有反斜杠）。
- **功能:**
  - 初始化 `DataCtrl` 实例，加载 `.sros` 文件内容到 `self.data` 字典中。

#### `GetOriginal(self, dataName)`
- **参数:**
  - `dataName` (str): 数据名称。
- **返回值:**
  - 返回 `self.data` 中指定名称的数据。

#### `WriteOriginal(self, dataName, dataValue, singleUseSet=False, needReboot=False)`
- **参数:**
  - `dataName` (str): 数据名称。
  - `dataValue` (str): 数据值。
  - `singleUseSet` (bool): 如果为 `True`，仅在内存中设置，不写入文件。
  - `needReboot` (bool): 如果为 `True`，不修改实际运行值。
- **功能:**
  - 写入数据到 `.sros` 文件中，更新 `self.data`。

#### `Get(self, controls, dataName)`
- **参数:**
  - `controls` (str): 配置文件名称。
  - `dataName` (str): 数据名称。
- **返回值:**
  - 返回指定名称的数据，可以是字符串或列表，取决于 `controls` 参数。

#### `Write(self, controls, dataName, dataValue)`
- **参数:**
  - `controls` (str): 配置文件名称。
  - `dataName` (str): 数据名称。
  - `dataValue` (str): 数据值。
- **功能:**
  - 写入数据到 `.sros` 文件中，并更新 `self.data`。

## `File_Path_Factory` 类
用于处理文件路径和文件存在性的检查。

### 方法

#### `Replace2Backslash(path)`
- **参数:**
  - `path` (str): 文件路径。
- **返回值:**
  - 将路径中的斜杠替换为反斜杠。

#### `FileIsExist(filePath: str) -> bool`
- **参数:**
  - `filePath` (str): 文件路径。
- **返回值:**
  - 返回文件是否存在的布尔值。

#### `IsDir(filePath: str) -> bool`
- **参数:**
  - `filePath` (str): 文件路径。
- **返回值:**
  - 返回路径是否指向目录的布尔值。

## `GetTime` 类
提供当前时间的各部分。

### 方法

#### `Year`
- **返回值:**
  - 当前年份。

#### `Month`
- **返回值:**
  - 当前月份。

#### `Week`
- **返回值:**
  - 当前周数（星期几）。

#### `Day`
- **返回值:**
  - 当前日期。

#### `Hour`
- **返回值:**
  - 当前小时。

#### `Min`
- **返回值:**
  - 当前分钟。

#### `Sec`
- **返回值:**
  - 当前秒钟。

## `FullCollect` 函数
执行垃圾回收，直到内存释放达到稳定状态。

### 函数定义

#### `FullCollect()`
- **返回值:**
  - 返回回收后的内存值。

## `GetDeviceID` 函数
获取设备唯一标识符。

### 函数定义

#### `GetDeviceID(wifiStaObj=network.WLAN(network.STA_IF), mode=1)`
- **参数:**
  - `wifiStaObj` (network.WLAN): WLAN 对象。
  - `mode` (int): 选择模式，0 为 MAC 地址，1 为唯一 ID。
- **返回值:**
  - 返回设备唯一标识符的字符串表示。

## `Screenshot` 类
提供屏幕截图的不同方法。

### 方法

#### `CopyFramebuf(path, oledObj=__import__("SeniorOS.system.devlib"))`
- **参数:**
  - `path` (str): 保存截图的文件路径。
  - `oledObj` (object): OLED 对象。
- **功能:**
  - 复制帧缓冲区数据并保存为 P4 格式文件。

#### `Enumerate(path, oledObj=__import__("SeniorOS.system.devlib"))`
- **参数:**
  - `path` (str): 保存截图的文件路径。
  - `oledObj` (object): OLED 对象。
- **功能:**
  - 根据 `screenshotMethod` 配置进行截图。支持 `fast`（速度优先）和 `ram`（内存优先）两种方法。

## `Tree` 函数
递归打印目录树结构。

### 函数定义

#### `Tree(path="/", prt=print, _tabs=0)`
- **参数:**
  - `path` (str): 目录路径。
  - `prt` (function): 打印函数，默认为 `print`。
  - ` _tabs` (int): 当前层级的缩进级别。
- **功能:**
  - 打印指定路径下的目录和文件结构。

## `ListState` 函数
生成显示列表状态的字符串。

### 函数定义

#### `ListState(dispContent, selectNum)`
- **参数:**
  - `dispContent` (list): 显示内容列表。
  - `selectNum` (int): 当前选择的项索引。
- **返回值:**
  - 返回格式化的列表状态字符串，例如 `"1/10"`。
