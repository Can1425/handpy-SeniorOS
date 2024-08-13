# daylight.py

## 函数定义

### `UITime(pages=True)`
- **参数:**
  - `pages` (bool): 是否显示时间分隔符（默认为 `True`）。
- **返回值:**
  - 返回格式化的时间字符串，例如 `"HH:MM"`。

### `GetCharWidth(s)`
- **参数:**
  - `s` (str): 字符串。
- **返回值:**
  - 返回字符串的宽度。

### `AutoCenter`
- **功能:**
  - 计算字符串在屏幕中央的位置。

### `App.Style1(appTitle:str)`
- **参数:**
  - `appTitle` (str): 应用标题。
- **功能:**
  - 清空显示，设置样式1，并显示应用标题。

### `App.Style2(appTitle:str)`
- **参数:**
  - `appTitle` (str): 应用标题。
- **功能:**
  - 清空显示，设置样式2，并显示应用标题。

### `Select.Style1(dispContent:list, y:int, window:bool=False, appTitle=None)`
- **参数:**
  - `dispContent` (list): 显示内容。
  - `y` (int): Y 坐标。
  - `window` (bool): 是否显示窗口（默认为 `False`）。
  - `appTitle` (str): 应用标题（默认为 `None`）。
- **返回值:**
  - 返回选择的索引。

### `Select.Style2(dispContent:list, tip:list, y:int, window:bool=False, appTitle=None)`
- **参数:**
  - `dispContent` (list): 显示内容。
  - `tip` (list): 提示内容。
  - `y` (int): Y 坐标。
  - `window` (bool): 是否显示窗口（默认为 `False`）。
  - `appTitle` (str): 应用标题（默认为 `None`）。
- **返回值:**
  - 返回选择的索引。

### `Select.Style3()`
- **返回值:**
  - 返回选择的索引（0 或 1）。

### `ListOptions(dispContent:list, y:int, window:False, appTitle:str)`
- **参数:**
  - `dispContent` (list): 显示内容。
  - `y` (int): Y 坐标。
  - `window` (bool): 是否显示窗口（默认为 `False`）。
  - `appTitle` (str): 应用标题。
- **功能:**
  - 显示列表选项并处理用户输入。

### `VastSea.Switch()`
- **功能:**
  - 切换 VastSea 模式并更新设置。

### `VastSea.Off()`
- **功能:**
  - 关闭 VastSea 模式。

### `VastSea.Progressive(mode)`
- **参数:**
  - `mode` (bool): 进度模式（`True` 表示逐渐减少亮度，`False` 表示逐渐增加亮度）。
- **功能:**
  - 根据模式逐渐调整亮度。

### `VastSea.SeniorMove.Line(nowX1:int, nowY1:int, nowX2:int, nowY2:int, newX1:int, newY1:int, newX2:int, newY2:int)`
- **参数:**
  - `nowX1`, `nowY1`, `nowX2`, `nowY2` (int): 当前线段的坐标。
  - `newX1`, `newY1`, `newX2`, `newY2` (int): 目标线段的坐标。
- **功能:**
  - 在显示屏上绘制一条逐渐移动的线段。

### `VastSea.SeniorMove.Text(text, nowX:int, nowY:int, newX:int, newY:int)`
- **参数:**
  - `text` (str): 要显示的文本。
  - `nowX`, `nowY` (int): 当前文本的位置。
  - `newX`, `newY` (int): 目标位置。
- **功能:**
  - 在显示屏上逐渐移动文本。

### `UITools()`
- **功能:**
  - 设置显示屏的反转模式和对比度。

### `About()`
- **功能:**
  - 显示关于信息，并在按钮按下前保持显示。

### `LightModeSet()`
- **功能:**
  - 切换显示模式（开启或关闭光线模式）。

### `LuminanceSet()`
- **功能:**
  - 调整显示屏的亮度。

### `Text(text, x, y, outMode, space=1, maximum_x=122, returnX=5, returnAddy=16, showMode=1)`
- **参数:**
  - `text` (str): 要显示的文本。
  - `x`, `y` (int): 文本的位置。
  - `outMode` (int): 文本输出模式（1: 停止，2: 自动换行，3: 省略）。
  - `space` (int): 字符间距（默认为 `1`）。
  - `maximum_x` (int): 最大显示宽度（默认为 `122`）。
  - `returnX`, `returnAddy` (int): 返回位置（默认为 `5` 和 `16`）。
  - `showMode` (int): 显示模式（默认为 `1`）。
- **功能:**
  - 在显示屏上显示文本，根据 `outMode` 选择不同的输出方式。
