# README PLZ!

此项是旧版FOS开发者因不熟悉Python内置对象使用方法而「虚构」出的一种架构方案/SDK

该功能在 [COMMIT `ad864a3e`](https://gitee.com/can1425/mPython-SeniorOS/commit/ad864a3ee7ebe11970747619f3a00acfec6af809) 后便已完全不可调用

在此COMMIT的临近几个COMMIT后将完全抹除其在代码中的存在痕迹

特将此文档保留 警示用.

> ~~技术力越强的破坏性越大啊 ccc~~


# 介绍

是Gxxk设计的一种代码机制 用于为各类系统内置组件/第三方app 提供一个 **标准**/**统一**/**简单** 的 **易接入** 的运行环境

# 原理

利用FOS在 运行下一阶段代码/调用组件 时所使用的`__import__`函数 通过控制`globals`参数（后称注入参数） 注入一定的对象 让被运行的代码可以直接使用Flag OS内置的功能

其中 现阶段系统分为两部分的注入参数

作用域分别为 **系统组件** 与 **第三方App**

系统组件的注入参数主要存放于`boot.py`内

第三方App的注入参数主要存放于`/SeniorOS/system/pages.py内`

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
