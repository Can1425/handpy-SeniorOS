class toml:
    def toml2dict(self,file):
        js = {};text=(file.read()).split('\r\n' if '\r\n' in file.read() else '\n')
        for i in text:
            if i.startswith('#') or "=" not in i:continue
            if i.startswith('['):js[i[1:-1]] = {}
            else:
                string=(i.split('=')[1]).split("#")[0].strip().strip("\"").strip("\'")
                js[i.split('=')[0].strip()] = eval("string")
        return js
    def dict2toml(self,js):
        text = ""
        for i in js:text += "{0} = {1}{2}{1}\n".format(i, "\"" if type(js[i]) == str else "",js[i])
        return text