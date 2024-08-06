class Viper:
    variables = {} #dictionary key is var's name, value is a tuple(type, value) -> x: ("number", 3)

    def __init__(self, code):
        self.stringCode = code

    
    def interperter(strCode: str):
        # break into lines, each line trim and split with space
        lines = strCode.split("\n")