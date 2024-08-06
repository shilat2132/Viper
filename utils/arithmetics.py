# Add (x+y)
def add(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x + y
    print("the parameters are not numbers")
    return

# Sub (x-y)
def sub(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x - y
    print("the parameters are not numbers")
    return


# Mul(x*y)
def mul(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x * y
    print("the parameters are not numbers")
    return

# div(x/y) - throw an error if y=0
def div(x, y):
    if y == 0:
        raise ArithmeticError("ZeroDivisionError - cannot divide by zero")
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x / y
    raise TypeError("the parameters are not numbers")
    
# Assign(x=y) variables are in dictionary
def assign(varsDict: dict, x, y):
    varsDict[x] = y



# Equal (x==y)
def equal(x, y):
    return x == y

# Not Equal (x!=y)
def not_equal(x, y):
    return x != y

# not
def negate(expression):
    return not expression

# Greater (x>y)
def greater(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x > y
    raise TypeError("the parameters are not numbers")

# >=
def greaterEquals(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x >= y
    raise TypeError("the parameters are not numbers")

# Smaller (x<y)
def less(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x < y
    raise TypeError("the parameters are not numbers")

# <=
def lessEquals(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x <= y
    raise TypeError("the parameters are not numbers")

# Or (x || y)
def Or(x, y):
    if x or y == 1:
        return True
    return False


# And (x&y)
def And(x, y):
    if x and y ==1:
        return True
    return False


# Power (x^y)
def pow(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x**y
    raise TypeError("the parameters are not numbers")

# Square (x^0.5)
def sqrt(x):
    if isinstance(x, int) or isinstance(x, float):
        return x ** 0.5
    raise TypeError("the parameters are not numbers")


# Min (x,y)
def min(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        if x <= y:
            return x
        return y
    raise TypeError("the parameters are not numbers")

# Max (x,y)
def max(x, y):
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        if x <= y:
            return y
        return x
    raise TypeError("the parameters are not numbers")

if __name__ == "__main__":
    print(add(1, 2))
    print(sub(1, 2))
    print(mul(5, 2))
    print(div(5, 2))
    x = 5
    y=2
    assign(x, y)
    print(x, y)
    print(equal(5, 2))
    print(not_equal(5, 2))
    print(greater(5, 2))
    print(less(5, 2))
    print(Or(5%2, 2%2))
    print(pow(5, 2))
    print(sqrt(4))
    print(min(5, 2))
    print(max(5, 2))
    print(And(5%2, 2%2))
