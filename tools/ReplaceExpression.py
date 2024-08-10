import sys
import re
from BuildConfig import *  # 此处按照逻辑上讲 Build.py已经做过一次校验 因此可以直接import

class Tools:
    # 根据targetButton值生成一个纯or表达式
    # 例：输入：thab
    #
    def GetButtonExpr(targetButton, connector="or", touchPadValue=100):
        targetButtonList = []
        for i in targetButton:
            targetButtonList.append(eval(i,
                                       {'a': "button_a.value()==0",
                                        'b': "button_b.value()==0",
                                        'p': f"touchPad_P.read()<{touchPadValue}",
                                        'y': f"touchPad_Y.read()<{touchPadValue}",
                                        't': f"touchPad_T.read()<{touchPadValue}",
                                        'h': f"touchPad_H.read()<{touchPadValue}",
                                        'o': f"touchPad_O.read()<{touchPadValue}",
                                        'n': f"touchPad_N.read()<{touchPadValue}"
            }))
        return f"({f' {connector} '.join(targetButtonList)})"

    def Const(name):
        global constData
        return "'" + constData[name] + "'"

    def EnableDebugMsg(id):
        global debugMessage
        return "pass" if debugMessage[id] else "#"

    hashtag = "#"

    def Language(name):
        global Language, Chineses, English
        if Language == "Chinese":
            return "'" + Chineses[name] + "'"
        elif Language == "English":
            return "'" + English[name] + "'"


def ReplaceExpr(inputPath, outputPath=""):
    if outputPath == "":
        outputPath = inputPath

    # 读取文件
    with open(inputPath, "r", encoding="utf-8") as f:
        code = f.read()

    # 定义更高效的正则表达式模式
    pattern = re.compile(r'eval\(\[/(.*?)//\]\)', re.DOTALL)

    # 替换函数
    def replace_func(match):
        expr = match.group(1)
        expr_result = eval(f"Tools.{expr}")
        print(f"将 {match.group(0)} 替换为 {expr_result}")
        return expr_result

    # 执行替换
    new_code = pattern.sub(replace_func, code)

    # 写入
    with open(outputPath, "w", encoding="utf-8") as f:
        f.write(new_code)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        ReplaceExpr(input("请给定输入文件路径\n"), input("请给定输出文件路径(可不填)\n"))
    else:
        try:
            ReplaceExpr(sys.argv[1], sys.argv[2])
        except:
            ReplaceExpr(sys.argv[1])
