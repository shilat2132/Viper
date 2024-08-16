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
        ast = Parser(tokens).parse()
        vars = Executor().evaluate(ast.rootNode)
        print(vars)
