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
        [+*/%^-]                   # Group 6: Arithmetic operators
    )
    |
    (
        \w*[a-zA-Z]\w*                         # Group 7: Identifiers (including those with numbers)
    )
    |
    ([=]) #Group 8: assign
    |
    (\() #Group 9: openParen
    |
    (\)) #Group 10: closeParen
    |
    (\{) #Group 11: scopeOpenParen
    |
    (\}) #Group 12: scopeCloseParen
    |
    (
        \S  # Group 13: Any non-whitespace character (lexical error)
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
        elif match.group(8):  
            tokens.append(Token('assign', match.group(8)))
        elif match.group(9):  
            tokens.append(Token('openParen', match.group(9)))
        elif match.group(10):  
            tokens.append(Token('closeParen', match.group(10)))
        elif match.group(11):  
            tokens.append(Token('scopeOpenParen', match.group(11)))
        elif match.group(12):  
            tokens.append(Token('scopeCloseParen', match.group(12)))
        elif match.group(13):  # Unexpected symbols
            raise SyntaxError(f"Unexpected token: {match.group(13)}")
    
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
    
