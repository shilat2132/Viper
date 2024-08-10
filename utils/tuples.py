class Tuple:
    """
        A custom immutable tuple-like class.

        Attributes:
        _values (tuple): The values stored in the CustomTuple.
        """

    def __init__(self, *args):
        """
                Initializes the CustomTuple with given values.

                Parameters:
                *args: The values to be stored in the tuple.
                """

        self._values = args

    def __getitem__(self, index):
        """
                Retrieves the value at the specified index.

                Parameters:
                index (int): The index of the value to retrieve.

                Returns:
                The value at the specified index.
                """

        return self._values[index]

    def __iter__(self):
        """
                Returns an iterator for the CustomTuple.

                Returns:
                An iterator object.
                """

        return iter(self._values)

    def __eq__(self, other):
        """
                Compares this CustomTuple to another for equality.

                Parameters:
                other (Tuple): The other CustomTuple to compare against.

                Returns:
                bool: True if the tuples are equal, False otherwise.
                """

        if not isinstance(other, Tuple):
            return False
        return self._values == other._values

    def __repr__(self):
        """
                Returns a string representation of the CustomTuple.

                Returns:
                str: The string representation of the tuple.
                """
        return f"CustomTuple{self._values}"

    def __setattr__(self, name, value):
        """
               Prevents modification of CustomTuple after initialization.

               Parameters:
               name (str): The attribute name.
               value: The value to set.

               Raises:
               AttributeError: If trying to modify attributes other than '_values'.
               """

        if name == '_values':
            super().__setattr__(name, value)
        else:
            raise AttributeError("Cannot modify CustomTuple")

    def __add__(self, other):
        """
                Concatenates this CustomTuple with another.

                Parameters:
                other (Tuple): The other CustomTuple to concatenate with.

                Returns:
                Tuple: A new CustomTuple containing elements from both tuples.

                Raises:
                TypeError: If the other object is not a CustomTuple.
                """

        if isinstance(other, Tuple):
            return Tuple(*(self._values + other._values))
        raise TypeError("Can only concatenate CustomTuple with another CustomTuple")

    def index(self, value):
        """
                Finds the index of the first occurrence of a value in the CustomTuple.

                Parameters:
                value: The value to find in the tuple.

                Returns:
                int: The index of the first occurrence of the value.

                Raises:
                ValueError: If the value is not found.
                """

        return self._values.index(value)

    def sorted(self):
        """
                Returns a new CustomTuple with the values sorted.

                Returns:
                Tuple: A new sorted CustomTuple.
                """

        return Tuple(*sorted(self._values))
    
    def length(self):
        """
                Returns the number of elements in the CustomTuple.

                Returns:
                int: The length of the CustomTuple.
                """

        count = 0
        for _ in self._values:
            count += 1
        return count
    # static function
    def rangeTuple(end, start=0):
        """
                Generates a range tuple from start to end.

                Parameters:
                end (int): The end of the range (exclusive).
                start (int, optional): The start of the range (inclusive). Defaults to 0.

                Returns:
                range: A range object.
                """

        return range(start, end)


