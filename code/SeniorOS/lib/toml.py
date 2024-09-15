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
                if string.startswith("[") and string.endswith("]"):
                    string = string[1:-1]
                    spst=string.split(",")
                    n=0
                    for n in range(len(spst)):
                        spst[n]=spst[n].strip().strip("\"").strip("\'")
                    js[i.split('=')[0].strip()] = spst
                else:js[i.split('=')[0].strip()] = string
        return js