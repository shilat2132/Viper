import sys
import os
import inspect
from dispatch import dispatchInit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lexer')))
from lexer import *


class Viper:
    variables = {} #dictionary key is var's name, value is a tuple(type, value) -> x: ("number", 3)
    tokens = []
    dispatch = {}
    dispatchInit(dispatch)
    

    def __init__(self, code):
        self.stringCode = code
    
    def interperter(self):
        # break into lines, each line trim and split with space
        lines = self.stringCode.split("\n")
        lineTokensArray = []
        i =0
        for l in lines:
            lineArray = l.split()
            print(lineArray)
            for t in lineArray:
                lineTokensArray.append(Token("identifier", t))
            Viper.tokens.append(lineTokensArray)
        print(Viper.dispatch["CONCAT"]("strings"," are fun"))

           



code = """x   =    5
x = x + 3"""
Viper(code).interperter()

# x = 5
# if x<=5 or x!=4:
#     print(2)

# y = x
# for i in range(4):
#     y = y+2

# print(y)