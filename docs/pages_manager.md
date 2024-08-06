# Pages Manager for SeniorOS

 基于 App Manager for HandPy 开发

## 作者

- **CycleBai**
- **W-Can1425**

## 由以下组件支持

- `devlib`
- `SeniorOS`

## 类定义

### `ScreenError`

自定义异常类，用于表示屏幕相关的错误。

### `PagesError`

自定义异常类，用于表示应用程序相关的错误。

### `main`

管理器类，用于管理 Pages 的屏幕和数据。

#### 方法

- **`__init__(self, app_name: str) -> None`**

  初始化 `main` 实例。

  - `app_name`: 应用名称（字符串）。

- **`genAppDataDump(self) -> dict`**

  生成应用数据的转储，包括屏幕数据、应用数据和应用名称。

  - 返回: 包含 `ScreenData`、`AppData` 和 `AppName` 的字典。

- **`RestoringAppDataDump(self, dump: dict) -> None`**

  恢复应用数据转储。

  - `dump`: 包含 `ScreenData`、`AppData` 和 `AppName` 的字典。
  - 抛出: `RuntimeError` 如果转储文件不完整。

- **`regScreen(self, screenName: str, override: bool = False, extra: dict = {}) -> None`**

  注册一个屏幕。

  - `screenName`: 屏幕名称（字符串）。
  - `override`: 是否覆盖已存在的屏幕（布尔值）。
  - `extra`: 附加数据（字典）。
  - 返回: 装饰器函数。

- **`readScreenExtraData(self, screenName: str, fullDict: bool = False, dataName: str = '') -> object`**

  读取屏幕的附加数据。

  - `screenName`: 屏幕名称（字符串）。
  - `fullDict`: 是否返回完整的数据字典（布尔值）。
  - `dataName`: 需要读取的具体数据名称（字符串）。
  - 返回: 请求的数据或数据字典。
  - 抛出: `ScreenError` 如果屏幕名称未定义或参数不符合要求。

- **`setScreenExtraData(self, screenName: str, dataName: str, data: object) -> bool`**

  设置屏幕的附加数据。

  - `screenName`: 屏幕名称（字符串）。
  - `dataName`: 数据名称（字符串）。
  - `data`: 数据内容（任意对象）。
  - 返回: 成功时返回 `True`。
  - 抛出: `ScreenError` 如果设置数据时发生错误。

- **`setAppExtraData(self, dataName: str, data: object) -> bool`**

  设置应用的附加数据。

  - `dataName`: 数据名称（字符串）。
  - `data`: 数据内容（任意对象）。
  - 返回: 成功时返回 `True`。
  - 抛出: `ScreenError` 如果设置数据时发生错误。

- **`readAppExtraData(self, fullDict: bool = False, dataName: str = '') -> object`**

  读取应用的附加数据。

  - `fullDict`: 是否返回完整的数据字典（布尔值）。
  - `dataName`: 需要读取的具体数据名称（字符串）。
  - 返回: 请求的数据或数据字典。
  - 抛出: `ScreenError` 如果参数不符合要求。

- **`setAppEntryPoint(self, override: bool = False) -> function`**

  设置应用的入口点。

  - `override`: 是否覆盖已存在的入口点（布尔值）。
  - 返回: 装饰器函数。
  - 抛出: `AppError` 如果入口点已定义且不允许覆盖。

- **`Run(self) -> None`**

  运行应用程序。

  - 抛出: `Error` 如果 Pages 入口点未设置或在执行过程中发生错误。
