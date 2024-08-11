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

    def __init__(self, initialVal=None):
<<<<<<< HEAD
        """
                Initializes the Array with an optional initial list of values.

                Parameters:
                initialVal (list, optional): The initial list of elements. Defaults to an empty list.
                """

        if initialVal == None:
=======
        if initialVal is None:
>>>>>>> ef81074ef3e2781a81d048ed14a268024f4cf937
            self.a = []
        else:
            self.a = initialVal

    def __repr__(self):
        """
                Returns a string representation of the Array.

                Returns:
                str: The string representation of the array.
                """

        return str(self.a)

    def length(self):
        """
<<<<<<< HEAD
               Returns the number of elements in the Array.

               Returns:
               int: The length of the array.
               """

=======
        calculates the length of the array
        :return: length of the array
        """
>>>>>>> ef81074ef3e2781a81d048ed14a268024f4cf937
        count = 0
        for i in self.a:
            count += 1
        return count

    def index(self, element):
        """
<<<<<<< HEAD
                Finds the index of the first occurrence of an element in the Array.

                Parameters:
                element: The element to search for.

                Returns:
                int: The index of the element, or -1 if not found.
                """

=======
        returns the index of the element in the array
        :param element: element to be searched
        :return: index of the element in the array, -1 if element is not found
        """
>>>>>>> ef81074ef3e2781a81d048ed14a268024f4cf937
        i = 0
        while i < self.length():
            if self.a[i] == element:
                return i
        return -1

    def get(self, i):
        """
<<<<<<< HEAD
                Retrieves the element at the specified index.

                Parameters:
                i (int): The index of the element to retrieve.

                Returns:
                The element at the specified index.

                Raises:
                ValueError: If the index is out of range.
                """

        l = self.length()
        if i >= l or i < 0:
=======
        returns the element at the given index
        :param i: given index
        :return: element at the given index
        """
        le = self.length()
        if i >= le or i < 0:
>>>>>>> ef81074ef3e2781a81d048ed14a268024f4cf937
            raise ValueError(f"argument must be in range 0-{l}")
        return self.a[i]

    def addItem(self, i, element):
        """
<<<<<<< HEAD
                Inserts an element at the specified index.

                Parameters:
                i (int): The index where the element should be inserted.
                element: The element to insert.
                """

=======
        adds an element to the array
        :param i: index of the element to be added
        :param element: element to be added
        :return:
        """
>>>>>>> ef81074ef3e2781a81d048ed14a268024f4cf937
        a1 = self.a[:i]
        a2 = self.a[i:]
        print(a1, a2, [element])
        self.a = a1 + [element] + a2

    def append(self, element):
        """
<<<<<<< HEAD
                Appends an element to the end of the Array.

                Parameters:
                element: The element to append.
                """

=======
        appends an element to the array
        :param element: element to be appended
        :return:
        """
>>>>>>> ef81074ef3e2781a81d048ed14a268024f4cf937
        self.a = self.a + [element]

    def remove(self, i):
        """
<<<<<<< HEAD
                Removes the element at the specified index.

                Parameters:
                i (int): The index of the element to remove.

                Raises:
                ValueError: If the index is out of range.
                """

=======
        removes an element from the array
        :param i: index of the element to be removed
        :return: 
        """
>>>>>>> ef81074ef3e2781a81d048ed14a268024f4cf937
        l = self.length()
        if i >= l or i < 0:
            raise ValueError(f"argument must be in range 0-{l}")
        self.a = self.a[:i] + self.a[i + 1:]
