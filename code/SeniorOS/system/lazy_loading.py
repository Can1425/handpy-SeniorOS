def lazy_import(module_name, func_name):
    '''
    调用方式：
    function = import_function('module', 'function')
    function()() # 注意，两个括号对！
    '''
    def wrapper():
        module = __import__(module_name, globals(), locals(), [func_name])
        return getattr(module, func_name)
    return wrapper