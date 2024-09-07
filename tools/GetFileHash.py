import hashlib,os,json
#_dir = os.getcwd().replace('"\"',"") + "\\build\\"
_dir=""
print("将检查%s下所有文件hash"%_dir)
hash_dict={}
def check_hash(working_dir,file):
    for i in os.listdir(working_dir):
        if os.path.isfile(working_dir+i):
            print("正在检查%s"%i)
            with open(working_dir+i,"rb") as f:
                data = f.read()
                hash = hashlib.md5(data).digest()
                hash_dict[str(working_dir.replace(os.getcwd()+"\\build\\","")+i).replace("\\","/")] = hash.hex()
                #print(str("hash为%s")%(str(hash.decode())))
        else:
            check_hash(working_dir+i+"\\",file)

if __name__ == "__main__":
    with open("hash.json","w") as file:
        check_hash(_dir,file)
        _json=json.dumps(hash_dict)
        file.write(_json.replace(",",",\n").replace("{","{\n ").replace("}"," \n}"))
