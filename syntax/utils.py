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

# needs to add for lists and tuples - maybe
def tokenizeLiteralAndIdentifier(literal):
    """
    gets a string and returns its token, raise an error if it's not a literal or identifier
    """
    number_pattern = r'^\d+\.\d+|\d+$'  # Matches integers (positive only)
    string_pattern = r'^".*"$'  # Matches strings enclosed in double quotes
    boolean_pattern = r'^(true|false)$'  # Matches boolean values
    identifier_pattern = r'^[a-zA-Z]\w*$'  # Matches identifiers (letters, numbers, underscores)

    if re.match(number_pattern, literal):
        return Token("number", literal)
    
    if re.match(string_pattern, literal):
        return Token("string", literal)
    
    if re.match(boolean_pattern, literal):
        return Token("boolean", literal)
    
    if re.match(identifier_pattern, literal):
        return Token("identifier", literal)
    
    raise SyntaxError(f"Unexpected function argument {literal}")