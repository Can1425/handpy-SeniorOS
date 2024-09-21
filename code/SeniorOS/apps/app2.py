import gc

def Main():
    import SeniorOS.system.ftreader as FTReader
    FTReader.Main()
    del FTReader;gc.collect()