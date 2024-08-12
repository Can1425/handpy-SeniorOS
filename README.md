# 苍旻操作系统｜SeniorOS

轻量级 handpy 用户界面框架

[官网/文档](https://senior.stfp.site/)

> Tips: 该文档暂未更新，请以当前版本代码以及以下简要介绍操作

![SeniorOS](https://senior.stfp.site/assets/senior.jpg)

## 关于 handpy(mpython)/掌控板

掌控板是一块 MicroPython 微控制器板。掌控板是创客教育专家委员会、猫友汇、广大一线老师共同提出需求并与创客教育行业优秀企业代表共同参与研发的教具、学具，是一块为教育而生的开源硬件，也是一个公益项目。

## 关于 SeniorOS

SeniorOS 是运行在 handpy （掌控版）平台上的轻量级用户界面框架，帮助各位开发者快速构建完整应用。你可以将程序毫发无损的迁移至 SeniorOS ，我们并未对固件做破坏性改动或删除重要功能。

## SeniorOS 现有版本文件目录

### 编译后

```
/build(刷入掌控版后在掌控版中为 /)
├SeniorOS
│├apps
││├logo.mpy
││├app1.mpy
││├app2.mpy
││├app3.mpy
││├app4.mpy
││├app5.mpy
││└port.mpy
│├data
││├list.sros
││└text.sros
│├fonts
││├HarmonyOS_sans_bold.mpy
││├misans.mpy
││└misans_16.mpy
│├style
││├bar.mpy
││├home.mpy
││└port.mpy
│├system
││├app_manager.mpy
││├core.mpy
││├daylight.mpy
││├devlib.mpy
││├main.mpy
││├typer.mpy
││├update.mpy
││├smart_wifi.mpy
││└pages.mpy
└boot.py
```

# 开发注意事项

请注意，您的开发应当基于 Alpha 分支，您的提交也应在 Alpha 分支进行

目前该系统没有正式版本

且现版本并不完善 并未发布官方编译版本 因此您需要自行编译

## 如何构建？

本系统使用了专用的特殊工具以提高代码精简度/可读性，如果您对系统在本地仓库做了一定更改，并不能直接刷入至掌控版中

我们编写了`./tools/Build.py`，您可以在本地仓库中**直接运行它**来构建**SeniorOS**

但在此之前，您需要进行一些简单的环境配置

### 基础环境

您需要具有以下工具 以便自行编译

- Python环境(不应低于3.8)
- Python-pip和本项目所要求的模块(模块配置请详见后文)

如您需要更进一步 编译历史版本/参与开发 您需要以下工具

- Git

> Tips: 推荐在 Ubuntu22.04(WSL) 下使用 VSCode 进行开发

### 创建并激活虚拟环境

```bash
# Windows 用户可以使用以下代码：
.\Python\python.exe -m venv .venv
# 请将 path 替换为 SeniorOS 在本地的仓库路径
path\.venv\Scripts\Activate.ps1
# 如果您使用cmd.exe作为终端 请使用以下代码：
path\.venv\Scripts\activate.bat

# Linux 用户根据以上代码以此类推 可以使用以下代码：
python -m venv .venv
source .venv/bin/activate
```
> Tips: 在Linux上 脚本对应路径通常位于`.venv/bin/activate`

### 安装所需模块

```bash
pip.exe install -r package.txt
pip install -r package.txt
# 两者任选其一，如有提示，请跟随提示运行另外的代码
```

### 设置编译相关选项

您需要根据您的需求修改`tools/BuildConfig.py`中的配置项

请**特别注意** `projectPath` ，此项用于识别编译时仓库的环境，应当指向该仓库的根目录

### 构建

瞬息可就

```bash
# Windows 用户可以使用以下代码：（两者任选其一）
python.exe ./tools/Win_Build.py
python ./tools/Win_Build.py

# Linux 用户可以使用以下代码：
python ./tools/Build.py
```

将会在`./build`目录下生成真正可运行的文件 使用软件将其按目录结构全部刷入即可