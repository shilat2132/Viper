class Tuple:

    def __init__(self, *args):
        """
        Initializes the CustomTuple with given values.

        Params:
            *args: The values to be stored in the tuple.
        """

        self.values = args

    def getItem(self, index):
        """
        Retrieves the value at the specified index.

        Parameters:
        index (int): The index of the value to retrieve.

        Returns:
        The value at the specified index.
        """
        
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        if index<0 or index>= self.length():
            raise IndexError("index out of bound")
        return self.values[index]

    def __iter__(self):
        """
        Returns an iterator for the CustomTuple.
        """
        return iter(self.values)



    def __repr__(self):
        """
        Returns a string representation of the CustomTuple.

        Returns:
        str: The string representation of the tuple.
        """
        return str(self.values)

    def combine(self, other):
        """
        combines two tuples
        
        Params:
          other: other tuple

            Returns: 
                new tuple with the 2 tuples combined
        """
        if isinstance(other, Tuple):
            return Tuple(*(self.values + other.values))
        raise TypeError("Can only concatenate CustomTuple with another Tuple")

    def index(self, value):
        """
        returns the index of element in tuple
        :param value: value to find
        :return: index of value or -1 if not found
        """
        try:
            return self.values.index(value)
        except:
            return -1

    def sorted(self):
        """
        Returns a new CustomTuple with the values sorted.

        Returns:
        Tuple: A new sorted CustomTuple.
        """

        return Tuple(*sorted(self.values))
    
    def length(self):
        """
        Returns the number of elements in the CustomTuple.

        Returns:
        int: The length of the CustomTuple.
        """

        count = 0
        for _ in self.values:
            count += 1
        return count




