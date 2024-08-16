import sys
import os
original_sys_path = sys.path.copy()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lexer')))
from lexer import *

sys.path = original_sys_path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../syntax')))
from parser import *

sys.path = original_sys_path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../interperter')))
from executor import Executor

sys.path = original_sys_path


class Viper:
    def __init__(self, code):
        self.stringCode = code
    
    def interperter(self):
        tokens = []
        lexer(self.stringCode, tokens) # type: ignore
        # print(Viper.tokens[4])
        # print(Viper.tokens[1], "\n", Viper.tokens[4], "\n", Viper.tokens[5] )
        # for v in tokens:
        #     print(v)

        ast = Parser(tokens).parse()
        # vars = Executor().evaluate(ast.rootNode)
        # print(vars)


           


code = """
min(1, 7)

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