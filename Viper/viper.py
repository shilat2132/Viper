import sys
import os
from dispatch import dispatchInit

original_sys_path = sys.path.copy()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lexer')))
from lexer import *

sys.path = original_sys_path


class Viper:
    variables = {} #dictionary key is var's name, value is a tuple(type, value) -> x: ("number", 3)
    tokens = []
    dispatch = {}
    dispatchInit(dispatch)
    

    def __init__(self, code):
        self.stringCode = code
    
    def interperter(self):
        Viper.tokens = lexer(self.stringCode) # type: ignore
        print(Viper.tokens[2], "\n", Viper.tokens[3])
        # for v in Viper.tokens:
        #     print(v)
        # print(Viper.dispatch["CONCAT"]("strings"," are fun"))

           



code = """x   =    5
x = x+3
y = x
y = y^2
isTrue = true
if x<=5 && isTrue
"""
Viper(code).interperter()

# x = 5
# if x<=5 or x!=4:
#     print(2)

# y = x
# for i in range(4):
#     y = y+2

# print(y)