class GetLogo:
    def __init__(self,LogoLoc):
        self.LogoLoc = LogoLoc
    def Logo(self,LogoNum):
        LogoData = ""
        with open(self.LogoLoc) as f:
            f.seek(0)
            for i in range(LogoNum+1):
                LogoData = f.readline()
        LogoData = eval("[{}]".format(LogoData))
        #gc.collect()
        return bytearray(LogoData)
    def LogoLength(self):
        LogoLen = 0
        with open(self.LogoLoc) as f:
            f.seek(0)
            while f.readline() != "":
                LogoLen += 1
        return LogoLen