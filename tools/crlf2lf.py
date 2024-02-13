# 将文件采用的CRLF（\r\n）换行符替换为LF（\n）换行符
def main():
    with open(filePath:=input("输入文件地址："),"r",encoding="utf-8")as f:
        code=[i.strip("\r") for i in f.read().split("\n")]
    with open(filePath,"w",encoding="utf-8")as f:
        f.write("\n".join(code))

if __name__ == '__main__':
    main()