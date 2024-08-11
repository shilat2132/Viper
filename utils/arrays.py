# Array
# Length
# Index
# Array(i)
# Add(i)
# Remove(i)
# Append

class Array:
    def __init__(self, initialVal=None):
        if initialVal is None:
            self.a = []
        else:
            self.a = initialVal

    def __repr__(self):
        return str(self.a)

    def length(self):
        """
        calculates the length of the array
        :return: length of the array
        """
        count = 0
        for i in self.a:
            count += 1
        return count

    def index(self, element):
        """
        returns the index of the element in the array
        :param element: element to be searched
        :return: index of the element in the array, -1 if element is not found
        """
        i = 0
        while i < self.length():
            if self.a[i] == element:
                return i
        return -1

    def get(self, i):
        """
        returns the element at the given index
        :param i: given index
        :return: element at the given index
        """
        le = self.length()
        if i >= le or i < 0:
            raise ValueError(f"argument must be in range 0-{l}")
        return self.a[i]

    def addItem(self, i, element):
        """
        adds an element to the array
        :param i: index of the element to be added
        :param element: element to be added
        :return:
        """
        a1 = self.a[:i]
        a2 = self.a[i:]
        print(a1, a2, [element])
        self.a = a1 + [element] + a2

    def append(self, element):
        """
        appends an element to the array
        :param element: element to be appended
        :return:
        """
        self.a = self.a + [element]

    def remove(self, i):
        """
        removes an element from the array
        :param i: index of the element to be removed
        :return: 
        """
        l = self.length()
        if i >= l or i < 0:
            raise ValueError(f"argument must be in range 0-{l}")
        self.a = self.a[:i] + self.a[i + 1:]
