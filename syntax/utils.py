import sys
import os
import re

original_sys_path = sys.path.copy()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lexer')))
from lexer import Token
sys.path = original_sys_path

def argsToList(args: str)->list:
    """
    converts string which represents function args to a list
    returns list of args
    """
    args = args[1:-1] #remove the parenthasis
    args = [k.strip() for k in args.split(",")]
    return args

def tokenizeLiteralAndIdentifier(literal:str, isDef = False):
    """
        gets a string and returns its token 
        
        for a function call:
        raise an error if it's not a literal or identifier
        
        for a function definition:
        raise an error if it's not an identifier
    """
    number_pattern = r'^\d+\.\d+|\d+$'  # Matches integers
    string_pattern = r'^".*"$'  # Matches strings enclosed in double quotes
    boolean_pattern = r'^(true|false)$'  # Matches boolean values
    identifier_pattern = r'^\w*[a-zA-Z]\w*$'  # Matches identifiers (letters, numbers, underscores)
    tuple_pattern = r'\((?:\s*(?:[a-zA-Z_]\w*|\d+|\d+\.\d+|\'[^\']*\'|\"[^\"]*\")\s*(?:,\s*(?:[a-zA-Z_]\w*|\d+|\d+\.\d+|\'[^\']*\'|\"[^\"]*\"))*)?\)'
    array_pattern = r'\[(?:\s*(?:[a-zA-Z_]\w*|\d+|\'[^\']*\'|\"[^\"]*\")\s*(?:,\s*(?:[a-zA-Z_]\w*|\d+|\'[^\']*\'|\"[^\"]*\"))*)?\]'

    if isDef:
        if re.match(identifier_pattern, literal):
            return Token("identifier", literal)
        raise SyntaxError("functions definitions can only have identifiers as arguments")
    
    if re.match(number_pattern, literal):
        if "." in literal: val = float(literal)
        else: val = int(literal)
        return Token("number", val)
    
    if re.match(string_pattern, literal):
        return Token("string", literal[1:-1])
    
    if re.match(boolean_pattern, literal):
        return Token("boolean", literal)
    
    if re.match(identifier_pattern, literal):
        return Token("identifier", literal)
    
    if re.match(tuple_pattern, literal):
        return Token("tuple", literal)
    
    if re.match(array_pattern, literal):
        return Token("array", literal)
    
    raise SyntaxError(f"Unexpected function argument {literal}")


def checkParenthasesValidation(parenthasesAmount: int, parenthasesType = "()" ):
      if parenthasesAmount <0:
                raise SyntaxError(f"extra {parenthasesType[1]}")
      elif parenthasesAmount>0:
           raise SyntaxError(f"extra {parenthasesType[0]}")