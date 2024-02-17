# 介绍

是Gxxk设计的一种代码机制 用于为各类系统内置组件/第三方app 提供一个 **标准**/**统一**/**简单** 的 **易接入** 的运行环境

# 原理

利用FOS在 运行下一阶段代码/调用组件 时所使用的`__import__`函数 通过控制`globals`参数（后称注入参数） 注入一定的对象 让被运行的代码可以直接使用Flag OS内置的功能

其中 现阶段系统分为两部分的注入参数

作用域分别为 **系统组件** 与 **第三方App**

系统组件的注入参数主要存放于`boot.py`内

第三方App的注入参数主要存放于`/Flag_OS/system/pages.py内`

# 看到一些「似乎是无意义代码」并含有SURT标记？

为了兼容各大开发工具的代码高亮/自动分析功能 ，我们增添类似如下样式的代码
```python
# --SystemUniRuntime--
eval('[/hashtag/]');wifi=wifi
eval('[/hashtag/]');oled=oled
# --SystemUniRuntime--
```

这种样式的代码 是为了尽量大批量的消除代码中的 **reportNameUndefindError** 错误 而只保留此处的代码 便于辨认

而 `eval('[/hashtag/]')` 是为了在EXPR阶段 将这段代码注释 而不消耗性能
