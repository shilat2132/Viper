import re

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
        # x = 5 -> {"identifier", x}, {"operator", =}, {"number", 5}

    def __repr__(self):
        return "Token(type: %s, value: %s)" % (self.type, self.value)



def tokenize(line)-> list[Token]:
    """
    tokenize the line

    Returns:
        tokens - a list of the tokens from that line, each token is instance of Token

    
    Example:
    line = "x=4" the function returns:
        [Token(type: identifier, value: x), Token(type: assign, value: =), Token(type: number, value: 4)]
    """
    pattern = r'''
    \s*                                # Optional leading whitespace
    (
        (?P<string>"(?:[^"\\]|\\.)*")  # Group 1: Quoted strings with escaped characters
    )
    |
    (
        (?P<keyword>\b(?:while|for|if|else|in)\b)  # Group 2: Control flow keywords
    )
    |
    (
        (?P<boolean>\b(?:true|false)\b)  # Group 3: Boolean literals
    )
    |
    (
        (?P<logical_operator>(?:<=|<|>=|>|==|!=|&&|\|\||!))  # Group 4: Logical operators
    )
    |
    (
        (?P<operator>[+*/%^-])  # Group 6: Arithmetic operators
    )
    |
    (
        (?P<number>[-]?\d+\.\d+|[-]?\d+)  # Group 5: Numeric literals (numbers, including floats)
    )
    |
    
    (
        (?P<builtinFunc>\b(?:range|print|max|min|sqrt)\b)  # Group 7: Built-in functions
    )
    |
    (
        (?P<tuple>\((?:\s*(?:[a-zA-Z_]\w*|[-]?\d+\.\d+|[-]?\d+|\'[^\']*\'|\"[^\"]*\")\s*(?:,\s*(?:[a-zA-Z_]\w*|[-]?\d+\.\d+|[-]?\d+|\'[^\']*\'|\"[^\"]*\"))*)?\))  # Group 8: Tuple
    )
    |
    (
        (?P<array>\[(?:\s*(?:[a-zA-Z_]\w*|[-]?\d+\.\d+|[-]?\d+|\'[^\']*\'|\"[^\"]*\")\s*(?:,\s*(?:[a-zA-Z_]\w*|[-]?\d+\.\d+|[-]?\d+|\'[^\']*\'|\"[^\"]*\"))*)?\])  # Group 9: Array
    )
    |
    (
        (?P<assign>[=])  # Group 10: Assignment operator
    )
    |
    (
        (?P<openParen>\()  # Group 11: Open parenthesis
    )
    |
    (
        (?P<closeParen>\))  # Group 12: Close parenthesis
    )
    |
    (
        (?P<scopeOpenParen>\{)  # Group 13: Open curly brace
    )
    |
    (
        (?P<scopeCloseParen>\})  # Group 14: Close curly brace
    )
     |
    (
        (?P<identifier>[a-zA-Z]\w*)  # Group 18: Identifiers
    )
    |
    
   # Group 15: String methods
    \b(?P<stringMethod>\.(REPLACE|isUpper|isLower|CONCAT|split))\b


    |
    # Group 16: Array methods
    \b(?P<arrayMethod>\.(length|index|get|addItem|append|remove|set))\b

    |
    # Group 17: Tuple methods
    \b(?P<tupleMethod>\.(getItem|combine|index|sorted|length))\b
    |
    (
        (?P<error>\S)  # Group 19: Any non-whitespace character (lexical error)
    )
    \s*                             
'''

    
    tokens = []
    for match in re.finditer(pattern, line, re.VERBOSE):
        if match.group('string'): 
            tokens.append(Token('string', match.group('string')[1:-1]))  # Remove quotes
        elif match.group('keyword'):  
            tokens.append(Token('keyword', match.group('keyword')))
        elif match.group('boolean'): 
            val = True if match.group('boolean') == "true" else False
            tokens.append(Token('boolean', val))
        elif match.group('logical_operator'):  
            tokens.append(Token('logical_operator', match.group('logical_operator')))
        elif match.group('number'): 
            val = float(match.group('number')) if "." in match.group('number') else int(match.group('number'))
            tokens.append(Token('number', val))
        elif match.group('operator'): 
            tokens.append(Token('operator', match.group('operator')))
        elif match.group('builtinFunc'):  
            tokens.append(Token('builtinFunc', match.group('builtinFunc')))
        elif match.group('tuple'): 
            tokens.append(Token('tuple', match.group('tuple')))
        elif match.group('array'): 
            tokens.append(Token('array', match.group('array')))
        elif match.group('assign'): 
            tokens.append(Token('assign', match.group('assign')))
        elif match.group('openParen'): 
            tokens.append(Token('openParen', match.group('openParen')))
        elif match.group('closeParen'): 
            tokens.append(Token('closeParen', match.group('closeParen')))
        elif match.group('scopeOpenParen'): 
            tokens.append(Token('scopeOpenParen', match.group('scopeOpenParen')))
        elif match.group('scopeCloseParen'): 
            tokens.append(Token('scopeCloseParen', match.group('scopeCloseParen')))
        elif match.group('identifier'):
            tokens.append(Token('identifier', match.group('identifier')))
        elif match.group('stringMethod'):
            tokens.append(Token('stringMethod', match.group('stringMethod')[1:]))
        elif match.group('arrayMethod'):
            tokens.append(Token('arrayMethod', match.group('arrayMethod')[1:]))
        elif match.group('tupleMethod'):
            tokens.append(Token('tupleMethod', match.group('tupleMethod')[1:]))
   
        elif match.group('error'):  # Unexpected symbols
            raise SyntaxError(f"Unexpected token: {match.group('error')}")
   
    return tokens



def lexer(code: str, tokens: list):
    """
    tokenize the code string and stores it in the tokens list

    in the end the tokens would be a list in which each element is a list of tokens of a line

    functions/method call would be tokenized as a tuple
    
    example: 
        for the following code:
            a = [3, 5]
            print(x)

        tokens list would be:
            [Token(type: identifier, value: a), Token(type: assign, value: =), Token(type: array, value: [3, 5])]
            [Token(type: builtinFunc, value: print), Token(type: tuple, value: (x))]
    """
    # split to lines
    lines = code.split("\n")
    # for each line classify to tokens with regex
    for line in lines:
        if len(line)>0:
            lineTokens = tokenize(line)
            tokens.append(lineTokens)
    
    
