# Array
# Length
# Index
# Array(i)
# Add(i)
# Remove(i)
# Append

class Array:
    def __init__(self, initialVal=None):
        if initialVal == None:
            self.a = []
        else:
            self.a=initialVal
    
    def __repr__(self):
        return str(self.a)

    
    def length(self):
        count = 0
        for i in self.a:
            count+=1
        return count
    
    def index(self, element):
        i = 0
        while i<self.length():
               if self.a[i]==element:
                   return i
        return -1
    
    def get(self, i):
        l= self.length()
        if i>= l or i<0:
            raise ValueError(f"argument must be in range 0-{l}")
        return self.a[i]
    
    def addItem(self, i, element):
        a1 = self.a[:i]
        a2 = self.a[i:]
        print(a1, a2, [element])
        self.a = a1 + [element] + a2
    
    def append(self, element):
        self.a = self.a + [element]

    
    def remove(self, i):
        l= self.length()
        if i>= l or i<0:
            raise ValueError(f"argument must be in range 0-{l}")
        self.a = self.a[:i] + self.a[i+1:]
    
