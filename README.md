# SeniorOS | All-Inclusive

（原 Flag OS）

![新春特别涂装](gitee_logo.jpg)

## 关于 mPython/掌控板

mPython掌控是一块MicroPython微控制器板。掌控板是创客教育专家委员会、猫友汇、广大一线老师共同提出需求并与创客教育行业优秀企业代表共同参与研发的教具、学具，是一块为教育而生的开源硬件，也是一个公益项目。

## 关于 SeniorOS

SeniorOS 是运行在 mPython （掌控版）平台上的轻量级多文件操作系统，旨在致力于构建完整的 mPython 生态体验。SeniorOS 也是一个为 mPython 开发者们准备好的全新平台，这里优化了大量官方固件中缺失的体验与功能，向 mPython 硬件的极限靠近。SeniorOS 不是 mPython 中的 MIUI ，也不会成为 mPython 中的 MIUI ，为了保证各位开发者能将程序毫发无损的迁移至 SeniorOS ，我们并未对固件做破坏性改动或删除重要功能，这将是日后， SeniorOS 生态强健有力的基础。

## Flag OS 现有版本文件目录

```
待重写
```

# 开发注意事项

请注意，您的开发应当基于 Alpha 分支，您的提交也应在 Alpha 分支进行

目前该系统没有正式版本


## 如何构建？

本系统使用了专用的特殊工具以提高代码精简度/可读性，如果您对系统在本地仓库做了一定更改，并不能直接刷入至掌控版中

我们编写了`./tools/Build.py`，您可以在本地仓库中**直接运行它**来构建**SeniorOS**

但在此之前，您需要进行一些简单的环境配置

### 创建并激活虚拟环境
```bash
python -m venv .venv
.venv/Scripts/Activate.ps1
# 如果您使用cmd.exe作为终端 请使用以下代码：
.venv/Scripts/activate.bat
# Linux用户根据以上代码以此类推 可以使用以下代码：
.venv/Scripts/activate
```

### 安装编译器

这是本作唯一的一个需要配置的外部编译器，接下来请在终端中输入以下代码 便会安装完成.
```python
pip install mpy-cross-v5
```

### 安装Build.py前置

Build.py需要使用Gitpython库来保证正常运行，请在终端中运行以下代码安装GitPython.
```python
pip install GitPython
```

### 构建

非常简单 一句话即可：
```bash
python ./tools/Build.py
```

将会在`./build`目录下生成真正可运行的文件 使用软件将其按目录结构全部刷入即可.