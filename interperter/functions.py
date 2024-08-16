class FunctionManager:
    def __init__(self):
        self.functions = {}

    def __setitem__(self, funcName, func):
        self.functions[funcName] = func

    def __getitem__(self, funcName):
        if funcName in self.functions:
            return self.functions[funcName]
        else:
            raise KeyError(f"Function '{funcName}' not found")

    def __contains__(self, funcName):
        return funcName in self.functions

