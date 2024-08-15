class Tuple:
    def __init__(self, *args):
        """
        defines a tuple
        :param args: values of tuples
        """
        self._values = args

    def getitem(self, index):
        """
        gets the value at certain index
        :param index: which index to get
        :return: the item at certain index
        """
        return self._values[index]

    def __iter__(self):
        """
        creates iterator for tuples
        :return: iterator for tuples
        """
        return iter(self._values)

    def eq(self, other):
        """
        checks if two tuples are equal
        :param other: other tuple
        :return: True if all values equal, False otherwise
        """
        if not isinstance(other, Tuple):
            return False
        return self._values == other._values

    def __repr__(self):
        """
        converts tuples to string
        :return: representation of tuple as string
        """
        return f"CustomTuple{self._values}"

    def setattr(self, name, value):
        """
        sets attribute
        :param name: name of attribute
        :param value: new value of attribute
        :return:
        """
        if name == '_values':
            super().__setattr__(name, value)
        else:
            raise AttributeError("Cannot modify CustomTuple")

    def add(self, other):
        """
        adds two tuples
        :param other: other tuple
        :return: new tuple
        """
        if isinstance(other, Tuple):
            return Tuple(*(self._values + other._values))
        raise TypeError("Can only concatenate CustomTuple with another CustomTuple")

    def index(self, value):
        """
        returns the index of element in tuple
        :param value: value to find
        :return: index of value
        """
        return self._values.index(value)

    def sorted(self):
        """
        sorts tuple
        :return: new tuple
        """
        return Tuple(*sorted(self._values))
    
    def length(self):
        """
        returns the length of tuple
        :return:  length of tuple
        """
        count = 0
        for _ in self._values:
            count += 1
        return count

    # static function
    def rangeTuple(self, end, start=0):
        """
        finds range of tuple
        :param end: end of tuple
        :param start: start of tuple
        :return: range of tuple
        """
        return range(start, end)


