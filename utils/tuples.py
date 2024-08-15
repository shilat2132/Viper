class Tuple:
    """
    A custom immutable tuple-like class.

    Attributes:
    values (tuple): The values stored in the CustomTuple.
    """

    def __init__(self, *args):
        """
        Initializes the CustomTuple with given values.

        Parameters:
        *args: The values to be stored in the tuple.
        """

        self.values = args

    def __getitem__(self, index):
        """
        Retrieves the value at the specified index.

        Parameters:
        index (int): The index of the value to retrieve.

        Returns:
        The value at the specified index.
        """
        
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        return self.values[index]

    def __iter__(self):
        """
        Returns an iterator for the CustomTuple.

        Returns:
        An iterator object.
        """

        return iter(self.values)

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
        return self.values == other.values

    def __repr__(self):
        """
        Returns a string representation of the CustomTuple.

        Returns:
        str: The string representation of the tuple.
        """
        return f"CustomTuple{self.values}"

    def add(self, other):
        """
        Concatenates this CustomTuple with another.

        Parameters:
        other (Tuple): The other CustomTuple to concatenate with.

        Returns:
        Tuple: A new CustomTuple containing elements from both tuples.

        Raises:
        TypeError: If the other object is not a CustomTuple.
        """

        if not isinstance(other, Tuple):
            raise TypeError("Can only concatenate CustomTuple with another CustomTuple")
        return Tuple(*(self.values + other.values))

    def index(self, value):
        """
        Finds the index of the first occurrence of a value in the CustomTuple.

        Parameters:
        value: The value to find in the tuple.

        Returns:
        int: The index of the first occurrence of the value.

        Raises:
        ValueError: If the value is not found.
        TypeError: If the value is not an int, float, or str.
        """

        if not isinstance(value, (int, float, str)):
            raise TypeError("value must be an int, float, or str")
        return self.values.index(value)

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
