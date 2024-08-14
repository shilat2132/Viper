# Array
# Length
# Index
# Array(i)
# Add(i)
# Remove(i)
# Append

class Array:
    """
        A custom array-like class for managing a list of elements.

        Attributes:
        a (list): The internal list storing the elements of the array.
        """

    def __init__(self, *args):
        """
                Initializes the Array with an optional initial list of values.

                Parameters:
                args (list, optional): The initial list of elements. Defaults to an empty list.
                """

        self.a = []
        for a in args:
            self.a.append(a)

    def __repr__(self):
        """
                Returns a string representation of the Array.

                Returns:
                str: The string representation of the array.
                """

        return str(self.a)

    def length(self):
        """
               Returns the number of elements in the Array.

               Returns:
               int: The length of the array.
               """

        count = 0
        for i in self.a:
            count += 1
        return count

    def index(self, element):
        """
                Finds the index of the first occurrence of an element in the Array.

                Parameters:
                element: The element to search for.

                Returns:
                int: The index of the element, or -1 if not found.
                """

        i = 0
        while i < self.length():
            if self.a[i] == element:
                return i
        return -1

    def get(self, i):
        """
                Retrieves the element at the specified index.

                Parameters:
                i (int): The index of the element to retrieve.

                Returns:

                Raises:
                ValueError: If the index is out of range.
        """
        l= self.length()
        if i>= l or i<0:
            raise ValueError(f"argument must be in range 0-{l}")
        return self.a[i]
    

    def addItem(self, i, element):
        a1 = self.a[:i+1]
        a2 = self.a[i+1:]
        self.a = a1 + [element] + a2

    def append(self, element):
        """
                Appends an element to the end of the Array.

                Parameters:
                element: The element to append.
                """

        self.a = self.a + [element]

    def remove(self, i):
        """
                Removes the element at the specified index.

                Parameters:
                i (int): The index of the element to remove.

                Raises:
                ValueError: If the index is out of range.
                """

        l = self.length()
        if i >= l or i < 0:
            raise ValueError(f"argument must be in range 0-{l}")
        self.a = self.a[:i] + self.a[i + 1:]
