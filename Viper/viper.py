import sys
import os
from dispatch import dispatchInit

original_sys_path = sys.path.copy()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lexer')))
from lexer import *

sys.path = original_sys_path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../syntax')))
from parser import *

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
        # print(Viper.tokens[4])
        # print(Viper.tokens[1], "\n", Viper.tokens[4], "\n", Viper.tokens[5] )
        # for v in Viper.tokens:
        #     print(v)
        Parser(Viper.tokens).parse() # type: ignore
       
        # print(Viper.dispatch["CONCAT"]("strings"," are fun"))

           


# chec; what's wrong
code = """
function f(a, v, l){
x=0
return v
}

"""
Viper(code).interperter()

# x = (x+3)^2
# y = sx
# isTrue = true
# if x<=5 && isTrue{
# print("some str")
# }
# x = 5
# if x<=5 or x!=4:
#     print(2)

# y = x
# for i in range(4):
#     y = y+2

# print(y)