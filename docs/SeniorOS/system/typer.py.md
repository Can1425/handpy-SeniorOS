# typer.py

## 常量

### `NL`

表示可供选择的字母和数字的二维列表。

```python
NL=[
    ['a','b','c','d','e','f'],
    ['g','h','i','j','k','l'],
    ['m','n','o','p','q','r'],
    ['s','t','u','v','w','x'],
    ['y','z','1','2','3','4'],
    ['5','6','7','8','9','0'],
]
```

### `PM`

表示可供选择的标点符号的二维列表。

```python
PM=[
    ['.', ',', ';', ':', '!', '?'],
    ['"', "'", '-', '—', '(', ')'],
    ['[', ']', '{', '}', ' ', "_"],
]
```

## 函数

### `typeOfNL()`

处理从 `NL` 列表中选择字母和数字的功能。

1. 在 OLED 屏幕上显示用于选择字符行的选项（P, Y, T, H, O, N）。
2. 等待用户按下触摸板以选择行。
3. 在 OLED 屏幕上显示选择的行。
4. 等待用户按下触摸板以选择列。
5. 如果启用了 Shift（`button_b`），则返回大写字母，否则返回字符本身。

```python
def typeOfNL():
    # 选择NL<list> y轴
    x=0; y=0; up=False
    time.sleep(0.25)
    oled.fill(0)
    oled.text("P:a b c d e f",0,0)
    oled.text("Y:g h i j k l",0,8)
    oled.text("T:m n o p q r",0,16)
    oled.text("H:s t u v w x",0,24)
    oled.text("O:y z 1 2 3 4",0,32)
    oled.text("N:5 6 7 8 9 0",0,40)
    oled.DispChar("B:大写",0,48)
    oled.show()
    while True:
        if touchpad_p.is_pressed(): y=0; break
        elif touchpad_y.is_pressed(): y=1; break
        elif touchpad_t.is_pressed(): y=2; break
        elif touchpad_h.is_pressed(): y=3; break
        elif touchpad_o.is_pressed(): y=4; break
        elif touchpad_n.is_pressed(): y=5; break                                                   
        if button_b.is_pressed():
            if up == False: up = True
            else: up = False
        if up == True:
            oled.DispChar("大写:开",64,48)
            oled.show()
        else: pass
    time.sleep(0.25)
    oled.fill(0)
    oled.DispChar("P:{} Y:{} T:{}".format(NL[y][0], NL[y][1], NL[y][2]),0,16)
    oled.DispChar("H:{} O:{} N:{}".format(NL[y][3], NL[y][4], NL[y][5]),0,32)
    oled.DispChar("B:大写",0,0)
    oled.show()         
    while True:
        if touchpad_p.is_pressed(): x=0; break
        elif touchpad_y.is_pressed(): x=1; break
        elif touchpad_t.is_pressed(): x=2; break
        elif touchpad_h.is_pressed(): x=3; break
        elif touchpad_o.is_pressed(): x=4; break
        elif touchpad_n.is_pressed(): x=5; break
        if button_b.is_pressed():
            if up == False: up = True
            else: up = False
        if up == True:
            oled.DispChar("大写:开",0,48)
            oled.show()
        else: pass
    time.sleep(0.5)
    if up == True: return NL[y][x].upper()
    else: return NL[y][x]
```

### `typeOfPM()`

处理从 `PM` 列表中选择标点符号的功能。

1. 在 OLED 屏幕上显示用于选择标点符号的选项（P, Y, T）。
2. 等待用户按下触摸板以选择行。
3. 在 OLED 屏幕上显示选择的标点符号。
4. 等待用户按下触摸板以选择列。
5. 返回选择的标点符号。

```python
def typeOfPM():
    # 选择PM<list> y轴
    x=0; y=0
    time.sleep(0.25)
    oled.fill(0)
    oled.text("P:. , ; : ! ?",0,0)
    oled.text("Y:\" ' - — (  )",0,8)
    oled.text("T:[ ] { } SPE _",0,16)
    oled.show()
    while True:
        if touchpad_p.is_pressed(): y=0; break
        elif touchpad_y.is_pressed(): y=1; break
        elif touchpad_t.is_pressed(): y=2; break
    time.sleep(0.25)
    oled.fill(0)
    oled.DispChar("P:{} Y:{} T:{}".format(PM[y][0], PM[y][1], PM[y][2]),0,16)
    oled.DispChar("H:{} O:{} N:{}".format(PM[y][3], PM[y][4], PM[y][5]),0,32)
    oled.show()
    while True:
        if touchpad_p.is_pressed(): x=0; break
        elif touchpad_y.is_pressed(): x=1; break
        elif touchpad_t.is_pressed(): x=2; break
        elif touchpad_h.is_pressed(): x=3; break
        elif touchpad_o.is_pressed(): x=4; break
        elif touchpad_n.is_pressed(): x=5; break
    time.sleep(0.25)
    return PM[y][x]
```

### `main()`

处理主程序逻辑，用于显示文本输入界面和处理用户输入。

1. 显示输入界面和当前文本。
2. 等待用户按下触摸板或按钮以选择字符或标点符号。
3. 更新文本内容或删除最后一个字符，直到用户按下完成按钮（A）。

```python
def main():
    text = ''
    while not button_a.is_pressed():
        oled.fill(0)
        oled.DispChar(text, 0, 0)
        oled.DispChar("字母/数字(P)",0,16)
        oled.DispChar("符号(Y)",0,32)
        oled.DispChar("删除(N) 完成(A)",0,48)
        oled.hline(0,16,128,1)
        oled.show()
        if touchpad_p.is_pressed(): text+=typeOfNL()
        elif touchpad_y.is_pressed(): text+=typeOfPM()
        elif touchpad_n.is_pressed(): text=text[:-1]
    return text
```
