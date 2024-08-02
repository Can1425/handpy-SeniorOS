# SeniorOS 规范

## 命名规则
- 文件名使用小写，多个单词使用下划线连接
- 变量名使用小驼峰命名法，尽量不使用下划线
- 函数名使用大驼峰命名法，尽量不使用下划线
- 常量名使用大写字母和下划线，多个单词使用下划线连接

## 代码风格

调用mpython.py下的API 禁止使用纯小写格式的api，例如：
```python
ACCEPT : touchPad_X
 DENY  : touchpad_x
```

## 文件目录结构
- 任何与系统本体无关的内容不应存放于`code`文件夹内

## 文件规范

- 使用**UTF-8**编码
- 换行符使用**LF**(即`\n`)

## Commit编写规范

本项目禁止网页单文件commit！

请使用**Gitee IDE**或Git手动Push！

违者将被强行回滚其commit.

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
- refactor: 重构（即不是新增功能，也不是修改bug的代码变动）
- chore: 构建过程或辅助工具的变动
- comfix: 对上一次commit的遗留下来的Bug作修复
- merge: [合并专用] 用于表示此次commit是为了合并两次commit
#### 关于merge
是专门标注其合并分支/commit的属性的type.

commit body可以为空 但如果同时作了其他修改 则需要将合并以外的修改描述出来

#### 关于comfix

是 在单次commit的一小段时间之内针对此commit发现/产生的Bug作修补的commit 的commit-type

> merge是在comfix之上又细分出来的一种commit-type 但merge===comfix comfix!==merge
>
> merge和comfix的性质一样 但此处为dever们便于区分 采用两种type作表示
### Title
用于简短描述本次commit所作内容
### Body
用于详细描述本次commit所作内容 以序号再次细分为多个小结 例：
```text
1. 简短描述某更改
  /修改文件名/具体对象名   对象类型(简短描述此修改)
```
注意 需要严格控制其中的空格

如果其修改过于广泛 那么可以直接写出此更改 例：
```text
1. xxxxx
  ...
  直接在此描述
```
或者：
```text
1. 直接在此描述
```


