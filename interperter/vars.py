class Variable:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Variable(name: {self.name}, type: {self.type}, value: {self.value})"

class Vars:
    def __init__(self):
        self.variables = {}

    def __getitem__(self, varName):
        if varName in self.variables:
            return self.variables[varName]
        else:
            raise KeyError(f"Variable '{varName}' doesn't exist")

    def __setitem__(self, varName, variable):
        self.variables[varName] = variable

    def __delitem__(self, varName):
        if varName in self.variables:
            del self.variables[varName]

    def __repr__(self):
        return f"{self.variables}"


