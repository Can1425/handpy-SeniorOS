import sys
import re
from BuildConfig import *  # 此处按照逻辑上讲 Build.py已经做过一次校验 因此可以直接import

class Tools:
    # 根据targetButton值生成一个纯or表达式
    def GetButtonExpr(targetButton, connector="or"):
        targetButtonList = []
        for i in targetButton:
            targetButtonList.append(eval(i,
                                       {'a': "button_a.value()==0",
                                        'b': "button_b.value()==0",
                                        'p': "touchPad_P.read()<Core.VitalData(1)",
                                        'y': "touchPad_Y.read()<Core.VitalData(1)",
                                        't': "touchPad_T.read()<Core.VitalData(1)",
                                        'h': "touchPad_H.read()<Core.VitalData(1)",
                                        'o': "touchPad_O.read()<Core.VitalData(1)",
                                        'n': "touchPad_N.read()<Core.VitalData(1)"
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

    # 使用优化的正则表达式模式，匹配 "eval("[/表达式/]")" 的部分
    pattern = re.compile(r'eval\("\[\/(.*?)\/\]\"\)')

    # 缓存表达式结果
    expr_cache = {}

    def replace_function(match):
        expr = match.group(1)
        if expr not in expr_cache:
            try:
                expr_cache[expr] = eval(f"Tools.{expr}")
            except Exception as e:
                print(f"替换失败: {e}")
                expr_cache[expr] = match.group(0)  # 错误时保留原表达式
        return expr_cache[expr]

    # 执行替换
    updated_code = pattern.sub(replace_function, code)

    # 写入文件
    with open(outputPath, "w", encoding="utf-8") as f:
        f.write(updated_code)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        ReplaceExpr(input("请给定输入文件路径\n"), input("请给定输出文件路径(可不填)\n"))
    else:
        try:
            ReplaceExpr(sys.argv[1], sys.argv[2])
        except:
            ReplaceExpr(sys.argv[1])
