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
        # print(Viper.tokens)
        # print(Viper.tokens[1], "\n", Viper.tokens[4], "\n", Viper.tokens[5] )
        Parser(Viper.tokens).parse() # type: ignore
        # for v in Viper.tokens:
        #     print(v)
        # print(Viper.dispatch["CONCAT"]("strings"," are fun"))

           



code = """return x+3

"""
Viper(code).interperter()

