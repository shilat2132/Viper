class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
        # x = 5 -> {"identifier", x}, {operator, =}

    def __repr__(self):
        return "Token(type= %s, value= %s)" % (self.type, self.value)

token_patterns = {
    's'
}
