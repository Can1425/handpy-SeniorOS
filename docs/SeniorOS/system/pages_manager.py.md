# pages_manager.py

## 方法

### `__init__(self) -> None`
- **功能:**
  - 初始化 `Main` 类的实例。

### `Import(moduleLoc: str, funcName: str, log = True, *argument) -> bool`
- **参数:**
  - `moduleLoc` (str): 模块的路径（例如 `'module.submodule'`）。
  - `funcName` (str): 要调用的函数名。
  - `log` (bool): 是否记录日志，默认为 `True`。
  - `*argument`: 传递给函数的可变参数。
- **返回值:**
  - 成功时返回 `True`。
  - 出错时返回 `False`。
- **功能:**
  - 导入指定的模块，并调用指定的函数。
  - 记录函数调用的日志信息。
  - 捕获并记录函数执行中的异常。