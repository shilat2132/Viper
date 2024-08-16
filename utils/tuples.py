class Tuple:
    def __init__(self, *args):
        """
        defines a tuple
        :param args: values of tuples
        """
        self._values = args

    def getItem(self, index):
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


    def __repr__(self):
        """
        converts tuples to string
        :return: representation of tuple as string
        """
        return str(self._values)


    def combine(self, other):
        """
        combines two tuples
        
        Params:
          other: other tuple

            Returns: 
                new tuple with the 2 tuples combined
        """
        if isinstance(other, Tuple):
            return Tuple(*(self._values + other._values))
        raise TypeError("Can only concatenate CustomTuple with another Tuple")

    def index(self, value):
        """
        returns the index of element in tuple
        :param value: value to find
        :return: index of value or -1 if not found
        """
        try:
            return self._values.index(value)
        except:
            return -1

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




