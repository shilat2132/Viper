class Token(object):
    def __init__(self, types, value, position):
        if not isinstance(type, str):
            raise "TypeError- Token type must be a string"
        if not isinstance(position, tuple) or not all(isinstance(i, int) for i in position):
            raise "TypeError- Position must be a tuple of integers"
        self.type = type
        self.value = value
        self.position = position

    def __repr__(self):
        return "Token(type= %s, value= %s, position= %s)" % (self.type, self.value, self.position)

token_patterns = {
    's'
}
