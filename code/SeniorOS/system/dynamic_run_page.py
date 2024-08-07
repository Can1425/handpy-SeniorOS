'''
简单说明：
此文件相当于一个 pages_manager 调用。
通过一些奇奇怪怪的技巧似乎能实现简化动态导入。

使用实例：

dyncmic_run_page.Main(AppManager 对象, 屏幕所在的模块, 屏幕名称, 屏幕的函数名称)
dyncmic_run_page.Main(Manager, 'SeniorOS.system.pages_manager', 'Screen', 'TheFunc')
'''

from SeniorOS.system.pages_manager import DynamicImport

def Main(app, moduleName, screenName, funcName):
    screenFunc = DynamicImport(moduleName, funcName)

    @app.regScreen(screenName)
    def MainScreen():
        screenFunc()

    @app.setPagesEntryPoint(override=True)
    def EntryPoint():
        app.changeScreen(screenName)

    app.Run()