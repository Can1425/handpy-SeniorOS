# 替换代码中被特殊标记了的表达式 ByGxxk
# 格式：eval("[/表达式/]")

class Tools:
    # 根据targetButton值生成一个纯or表达式
    # 例：输入：thab
    # 
    def GetButtonExpr(targetButton,touchPadValue=100):
        targetButtonList=[]
        for i in targetButton:
            targetButton.append(eval(i,{'a':"button_a.value()==0",
                                        'b':"button_b.value()==0",
                                        'touchPad_P':f"touchPad_P.read()<{touchPadValue}",
                                        'touchPad_Y':f"touchPad_Y.read()<{touchPadValue}",
                                        'touchPad_T':f"touchPad_T.read()<{touchPadValue}",
                                        'touchPad_H':f"touchPad_H.read()<{touchPadValue}",
                                        'touchPad_O':f"touchPad_O.read()<{touchPadValue}",
                                        'touchPad_N':f"touchPad_N.read()<{touchPadValue}"
            }))
        return f"{' or '.join(targetButtonList)}"

def main():
    path=input("请给定文件路径\n")
    # 读取文件
    with open(path, "r", encoding="utf-8") as f:
        code = [i.strip("\r") for i in f.read().split("\n")] # strip属于对crlf作兼容
    # 遍历并查找标识符
    print("-----开始进行处理-----")
    for line in range(len(code)):
        if ("eval(\"[/" in code[line]) and ("/]\")" in code[line]):
            exprStart=code[line].index("[/")+2  # +2是因为 string.index 返回的是起始位置 需要+ len("[/") 才行
            exprEnd=code[line].index("/]")      # 防止各位看着有点晕 拆分来写 顺手加个日志 反正电脑端性能无所谓
            exprResult=eval(f"Tools.{code[line][exprStart:exprEnd]}")
            print(f"将{code[line][exprStart-8:exprEnd+4]}替换为{exprResult}")

            tmpVar=list(code[line])  # 用于兼容神比Python的不可变类型
            tmpVar[exprStart-8:exprEnd+4]=exprResult # 等号左侧是从eval函数开始到结束的需要替换的部分 
            code[line]="".join(tmpVar)
    print("----- 处理结束 -----")
    # 写入
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(code))
    

if __name__ == "__main__":
    main()