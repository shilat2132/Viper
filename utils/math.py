# Add (x+y)
def add(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x + y


# Sub (x-y)
def sub(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x - y


# Mul(x*y)
def mul(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x * y


# div(x/y) - throw an error if y=0
def div(x, y):
    if y == 0:
        raise "ZeroDivisionError- cannot divide by zero"
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x / y


# StringAssign(x=y)
def assign(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    x = y
    return x


# Equal (x==y)
def equal(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x == y


# Not Equal (x!=y)
def not_equal(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x != y


# Greater (x>y)
def greater(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x > y


# Smaller (x<y)
def less(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x < y


# Or (x || y)
def Or(x, y):
    return x or y


# And (x&y)
def And(x, y):
    return x and y


# Power (x^y)
def pow(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return x ** y


# Square (x^0.5)
def sqrt(x):
    if not isinstance(x, int) or not isinstance(x, float):
        print("the parameters are not numbers")
        return
    return x ** 0.5


# Min (x,y)
def min(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return min(x, y)


# Max (x,y)
def max(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(x, float) or not isinstance(y, float):
        print("the parameters are not numbers")
        return;
    return max(x, y)