import re

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
        # x = 5 -> {"identifier", x}, {operator, =}

    def __repr__(self):
        return "Token(type: %s, value: %s)" % (self.type, self.value)



def tokenize(line):
    pattern = r'''
     \s*                             # Optional leading whitespace
    (
        "(?:[^"\\]|\\.)*"           # Group 1: Quoted strings with escaped characters
    )
    |
    (
        \b(?:while|for|if|else|print|function)\b  # Group 2: Control flow keywords (whole words)
    )
    |
    (
        \b(?:true|false)\b          # Group 3: Boolean literals
    )
    |
    (
        (?:<=|<|>=|>|==|!=|&&|\|\||!)    # Group 4: Logical operators
    )
    |
    (
        \d+\.\d+|\d+                # Group 5: Numeric literals (numbers, including floats)
    )
    |
    (
        [=+*/%^-]                   # Group 6: Arithmetic operators
    )
    |
    (
        \w*[a-zA-Z]\w*                         # Group 7: Identifiers (including those with numbers)
    )
    |
    (
        \S                          # Group 8: Any non-whitespace character (lexical error)
    )
    \s*                             
'''
    
    tokens = []
    for match in re.finditer(pattern, line, re.VERBOSE):
        if match.group(1): 
            tokens.append(Token('string', match.group(1)[1:-1]))  # Remove quotes
        elif match.group(2):  
            tokens.append(Token('keyword', match.group(2)))
        elif match.group(3): 
            tokens.append(Token('boolean', match.group(3)))
        elif match.group(4):  
            tokens.append(Token('logical_operator', match.group(4)))
        elif match.group(5): 
            tokens.append(Token('number', match.group(5)))
        elif match.group(6): 
            tokens.append(Token('operator', match.group(6)))
        elif match.group(7):  
            tokens.append(Token('identifier', match.group(7)))
        elif match.group(8):  # Unexpected symbols
            raise SyntaxError(f"Unexpected token: {match.group(8)}")
    
    return tokens

def lexer(code: str):
    codeTokensList = []
    # split to lines
    lines = code.split("\n")
    # for each line classify to tokens with regex
    for line in lines:
        if len(line)>0:
            lineTokens = tokenize(line)
            codeTokensList.append(lineTokens)
    
    return codeTokensList
    
