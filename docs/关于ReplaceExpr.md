# 关于ReplaceExpr

对应文件`./tools/ReplaceExpression.py`

是FOS下，Gxxk开发的一款代码替换工具。

# 如何使用

## 正常使用

在正常环境中 可以直接运行其代码 会主动询问输入文件路径与输出文件路径

输入文件路径属于必须参数 如输出参数未填写(`outputPath==""`)将会自动使用输入路径

您也可以将路径写在调用命令上，如：
```bash
python ./ReplaceExpression.py <inputPath> [outputPath]
```

## 代码集成

如您的项目需要调用其功能 可以**直接导入**其文件中的函数`ReplaceExpr`，并传入 **\<inputPath\>** 与 **[outputPath]**  例：

```python
from tools.ReplaceExpression import ReplaceExpr

filePath="/path/file"
outputPath="/path/file2"

ReplaceExpr(filePath,outputPath)

```

## 日志

代码附带了一些日志 便于查询其替换过程，如：
```text
将eval("[/hashtag/]")替换为#
将eval("[/GetButtonExpr('a')/]")替换为button_a.value==0
```

# 内置对象

此脚本内置了一些便于用户操作的函数，您可以在调用时使用这些函数，如：
| 函数名 | 类型 | 功能 | 参数 | 返回值 | 备注 |
|-|-|-|-|-|-|
|GetButtonExpr|func|生成按钮表达式|目标按钮|表达式|详见下方|
|Const|func|获取一个用于构建的设置值|值的索引|值|/|

## GetButtonExpr

获取按钮表达式 适用场景：

- `GetButtonExpr`一般需要和`ReplaceExpr`函数一起使用

> 等待用户同时按下AB键
```python
while not eval("[/GetButtonExpr('ab','and')/]"):pass
```

- 注：此等待用户操作的这一核心思想来自于GxxkSystem
- 此处不得使用转移符号与大写字母

> 等待用户任意操作
```python
while not eval("[/GetButtonExpr('pythonab')/]"):pass
```

- 此处第二个参数名为`connector`，默认参数为`or`