class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
        # x = 5 -> {"identifier", x}, {operator, =}

    def __repr__(self):
        return "Token(type= %s, value= %s)" % (self.type, self.value)

token_patterns = {
    'KEYWORD': r'\b(if|else|while|for|return)\b',
    'IDENTIFIER': r'[A-Za-z][A-Za-z0-9_]*',
    'LITERAL': r'\d+',
    'OPERATOR': r'[+\-*/=<>]+',
    'DELIMITER': r'[();]',
}


def tokenize(code):
    tokens = []
    pos = 0
    
