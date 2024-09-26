# SeniorOS 代码书写规范

## 命名规则

- 文件名使用小写，多个单词使用下划线连接
- 变量名使用小驼峰命名法，尽量不使用下划线
- 函数名使用大驼峰命名法，尽量不使用下划线
- 常量名使用大写字母和下划线，多个单词使用下划线连接

## 调用库规范

本项目禁止使用 'mpython.py' ，请使用大量优化后的 'system/devlib.py'

```python
# from mpython import *
from SeniorOS.lib.devlib import *
```

## 代码风格

调用 'system/devlib.py' 下的 API 禁止使用纯小写格式的写法，例如：
```python
ACCEPT : touchPad_X
 DENY  : touchpad_x
```

合并字符串请用 "%" 或 .format() , 禁止使用 str(+) 或 f""(f-string) 的写法
examples:
```python
str1 = "Hello"
str2 = "World"
# 正确
str3 = "%s %s" % (str1, str2)
str4 = "{} {}".format(str1, str2)

# 错误
str3 = str1 + " " + str2
str4 = f"{str1} {str2}"
```

## 文件目录结构

- 任何与系统本体无关的内容不应存放于 `code` 文件夹内

## 文件规范

- 使用 **UTF-8** 编码
- 换行符使用 **LF** (即 `\n` )

## Commit 编写规范

本项目禁止网页单文件 Commit！

请使用 **Gitlab IDE** 或 Git 手动 Push

违者将被强行回滚其 Commit

### 模板
```text
<type>:<title>

<body>
```
### Type
- feat: 新功能（feature）
- fix: 修补bug
- docs: 文档（documentation）
- style: 格式（不影响代码运行的变动，修改命名也算在其中）
- refactor: 重构（即不是新增功能，也不是修改 Bug 的代码变动）
- chore: 构建过程或辅助工具的变动
- comfix: 对上一次 Commit 的遗留下来的 Bug 作修复
- merge: [合并专用] 用于表示此次 Commit 是为了合并两次 Commit

#### 关于 merge

是专门标注其合并 分支/Commit 的属性的 Type

Commit Body 可以为空 但如果同时作了其他修改 则需要将合并以外的修改描述出来

#### 关于comfix

是在单次commit的一小段时间之内针对此commit发现/产生的Bug作修补的commit 的commit-type

> 说明: merge 是在 comfix 之上又细分出来的一种 commit-type 但 merge===comfix 且 comfix!==merge

> 说明: merge 和 comfix 的性质一样，但此处为开发者便于区分 采用两种 Type 作表示

### Title

用于简短描述本次 Commit 所作内容

### Body

用于详细描述本次 Commit 所作内容，以序号再次细分为多个小结，例如：

```text
1. 简短描述某更改
  /修改文件名/具体对象名   对象类型(简短描述此修改)
```

> 重要: 需要严格控制其中的空格

如果其修改过于广泛，那么可以直接写出此更改，例如：
```text
1. xxxxx
  ...
  直接在此描述
```
或者：
```text
1. 直接在此描述
```