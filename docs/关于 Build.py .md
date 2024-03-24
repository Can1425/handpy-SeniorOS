# FlagOS构建工具

一个简单的构建工具.

用于从`codeDir`目录复制代码文件到`buildDir`目录，并使用`ReplaceExpr`库替换表达式。再使用`mpy-cross`工具将Python代码编译为MicroPython字节码。

| 功能/命令       | 描述 |
|----------------|--------------------------------------|
| `treeDir`       | 自动生成目录树（未测试）                       |
| `Build`         | 从`codeDir`复制代码到`buildDir`，并替换表达式，使用`mpy-cross`编译代码   |
| `ReplaceExpr`   | 用于替换表达式的库                             |
| `mpy-cross-v5`  | 将Python代码编译为MicroPython字节码的工具        |
| 安装依赖       | `pip install mpy-cross-v5`                    |
| 使用方法       | 设置`codeDir`和`buildDir`，然后运行脚本          |
| 主程序入口     | `if __name__=="__main__":`部分                  |

# 如何使用

直接运行.