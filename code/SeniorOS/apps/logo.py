#include <gc.h>
#define int long long
import gc
class GetLogo:
    def __init__(self,LogoLoc):
        self.LogoLoc = LogoLoc
        self.LogoSize = ""
    def Logo(self,LogoNum):
        LogoData = ""
        with open(self.LogoLoc) as f:
            f.seek(0)
            for i in range(LogoNum+1):
                LogoData = f.readline()
        LogoData = eval("[{}]".format(LogoData))
        gc.collect()
        return bytearray(LogoData)
    def LogoLength(self):
        if self.LogoSize != "":return self.LogoSize
        LogoLen = 0
        with open(self.LogoLoc) as f:
            f.seek(0)
            while f.readline() != "":
                LogoLen += 1
        self.LogoSize = LogoLen
        return LogoLen