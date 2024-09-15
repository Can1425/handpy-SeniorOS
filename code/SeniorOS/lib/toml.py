class toml:
    def toml2dict(self, file):
        js = {}
        text = file.read()
        if '\r\n' in text:text=text.split('\r\n')
        else:text=text.split('\n')
        for i in text:
            if i.startswith('#') or "=" not in i:continue
            if i.startswith('['):
                js[i[1:-1]] = {}
            else:
                string=(i.split('=')[1]).split("#")[0].strip().strip("\"").strip("\'")
                try:js[i.split('=')[0].strip()] = eval(string,{})
                except:js[i.split('=')[0].strip()] = string
        return js
    def dict2toml(self, js):
        text = ""
        for i in js:
            if type(js[i]) == dict:
                text += f"[{i}]\n"
            if type(js[i]) == list:
                text += f"{i} = ["
                for j in range(len(js[i])):
                    if j != len(js[i])-1:text += f"{js[i][j]},"
                    else:text += f"{js[i][j]}"
                text += "]\n"
            else:
                if type(js[i]) == str:text += f"{i} = \"{js[i]}\"\n"
                else:text += f"{i} = {js[i]}\n"
        return text