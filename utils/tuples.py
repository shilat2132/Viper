class Tuple:
    def __init__(self, *args):
        self._values = args

    def __getitem__(self, index):
        return self._values[index]

    def __iter__(self):
        return iter(self._values)

    def __eq__(self, other):
        if not isinstance(other, Tuple):
            return False
        return self._values == other._values

    def __repr__(self):
        return f"CustomTuple{self._values}"

    def __setattr__(self, name, value):
        if name == '_values':
            super().__setattr__(name, value)
        else:
            raise AttributeError("Cannot modify CustomTuple")

    def __add__(self, other):
        if isinstance(other, Tuple):
            return Tuple(*(self._values + other._values))
        raise TypeError("Can only concatenate CustomTuple with another CustomTuple")

    def index(self, value):
        return self._values.index(value)

    def sorted(self):
        return Tuple(*sorted(self._values))
    
    def length(self):
        count = 0
        for _ in self._values:
            count += 1
        return count

# דוגמה לשימוש
t = Tuple(1, 2, 3, 4, 5)
print(t.length())  # הדפס 5
