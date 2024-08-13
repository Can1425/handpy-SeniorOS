# log_manager.py

## `LogManager` 类

### 方法

#### `__init__(self, log_level: str = 'INFO', log_prefix: str = '#', log_format: str = '[#level#] #format_time#: #message#') -> None`
- **参数:**
  - `log_level` (str): 最低日志级别，默认为 `'INFO'`。
  - `log_prefix` (str): 日志格式的前缀，默认为 `'#'`。
  - `log_format` (str): 日志格式，默认为 `'[#level#] #format_time#: #message#'`。
- **功能:**
  - 初始化 `LogManager` 实例，设置日志格式和级别。

#### `log(self, text: str, level: str = 'INFO')`
- **参数:**
  - `text` (str): 要记录的日志消息。
  - `level` (str): 日志级别，默认为 `'INFO'`。
- **功能:**
  - 根据指定的日志级别输出日志消息。

#### `Info(self, text: str)`
- **参数:**
  - `text` (str): 要记录的信息。
- **功能:**
  - 记录 `'INFO'` 级别的日志消息。

#### `Debug(self, text: str)`
- **参数:**
  - `text` (str): 要记录的信息。
- **功能:**
  - 记录 `'DEBUG'` 级别的日志消息。

#### `Message(self, text: str)`
- **参数:**
  - `text` (str): 要记录的信息。
- **功能:**
  - 记录 `'MSG'` 级别的日志消息。

#### `Warn(self, text: str)`
- **参数:**
  - `text` (str): 要记录的信息。
- **功能:**
  - 记录 `'WARN'` 级别的日志消息。

#### `Error(self, text: str)`
- **参数:**
  - `text` (str): 要记录的信息。
- **功能:**
  - 记录 `'ERROR'` 级别的日志消息。

#### `Fatal(self, text: str)`
- **参数:**
  - `text` (str): 要记录的信息。
- **功能:**
  - 记录 `'FATAL'` 级别的日志消息。

## 函数

### `format_timestamp()`
- **返回值:**
  - 返回格式化的当前时间字符串，格式为 `YYYY-MM-DD HH:MM:SS`。

### `getTime(format: bool = False)`
- **参数:**
  - `format` (bool): 是否返回格式化的时间字符串，默认为 `False`。
- **返回值:**
  - 如果 `format` 为 `False`，返回当前时间的时间戳。
  - 如果 `format` 为 `True`，返回格式化的当前时间字符串。

### `logFormatReplace(formatText: str, message: str, prefix: str = '#', level: str = 'INFO') -> str`
- **参数:**
  - `formatText` (str): 日志格式文本。
  - `message` (str): 日志消息。
  - `prefix` (str): 格式文本的前缀，默认为 `'#'`。
  - `level` (str): 日志级别，默认为 `'INFO'`。
- **返回值:**
  - 返回格式化后的日志字符串。