# Add (x+y)
def add(x, y):
    """
    Adds two numbers together.
    :param x: 
    :param y: 
    :return: x+y
    """""
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x + y
    print("the parameters are not numbers")
    return


# Sub (x-y)
def sub(x, y):
    """
    Subtracts two numbers together.
    :param x:
    :param y:
    :return: x-y
    """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x - y
    print("the parameters are not numbers")
    return


# Mul(x*y)
def mul(x, y):
    """
    Multiplies two numbers together.
    :param x:
    :param y:
    :return: x*y
    """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x * y
    print("the parameters are not numbers")
    return


# div(x/y) - throw an error if y=0
def div(x, y):
    """
    Divides two numbers together.
    :param x:
    :param y:
    :return: x/y
    """
    if y == 0:
        raise ArithmeticError("ZeroDivisionError - cannot divide by zero")
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x / y
    raise TypeError("the parameters are not numbers")


# Assign(x=y) variables are in dictionary
def assign(varsDict: dict, x, y):
    """
    Assigns value y to variable x.
    :param varsDict: dictionary where variables are held
    :param x: variable to assign
    :param y: value to assign
    :return: x=y
    """
    varsDict[x] = y


# Equal (x==y)
def equal(x, y):
    """
    Checks if two numbers are equal
    :param x:
    :param y:
    :return: True if equal, false otherwise
    """
    return x == y


# Not Equal (x!=y)
def not_equal(x, y):
    """
    Checks if two numbers are not equal
    :param x:
    :param y:
    :return: True if not equal, false otherwise
    """
    return x != y


# not
def negate(expression):
    """
    negates expression
    :param expression:
    :return: negated expression
    """
    return not expression


# Greater (x>y)
def greater(x, y):
    """
    Checks if x is greater than y
    :param x:
    :param y:
    :return: True if greater, false otherwise
    """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x > y
    raise TypeError("the parameters are not numbers")


# >=
def greaterEquals(x, y):
    """
    Checks if x is greater than or equal to y
    :param x:
    :param y:
    :return: True if greater or equal, false otherwise
    """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x >= y
    raise TypeError("the parameters are not numbers")


# Smaller (x<y)
def less(x, y):
    """
    Checks if x is less than y
    :param x:
    :param y:
    :return: True if less, false otherwise
    """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x < y
    raise TypeError("the parameters are not numbers")


# <=
def lessEquals(x, y):
    """
    Checks if x is less than or equal to y
    :param x:
    :param y:
    :return: True if less or equal, false otherwise
    """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x <= y
    raise TypeError("the parameters are not numbers")


# Or (x || y)
def Or(x, y):
    """
    Checks if x or y
    :param x:
    :param y:
    :return: True if x or y, false otherwise
    """
    return x | y


# And (x&y)
def And(x, y):
    """
    Checks if x and y
    :param x:
    :param y:
    :return: True if x and y, false otherwise
    """
    return x & y


# Power (x^y)
def power(x, y):
    """
    lifts x to the power of y
    :param x:
    :param y:
    :return: x to the power of y
    """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x**y
    raise TypeError("the parameters are not numbers")


# Square (x^0.5)
def sqrt(x):
    """
    calculates the square root of x
    :param x:
    :return: square root of x
    """
    if isinstance(x, int) or isinstance(x, float):
        return x ** 0.5
    raise TypeError("the parameters are not numbers")


# Min (x,y)
def Min(x, y):
    """
    picks the smallest value between x and y
    :param x:
    :param y:
    :return: x if x is smaller than y, y otherwise
    """
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        if x <= y:
            return x
        return y
    raise TypeError("the parameters are not numbers")


# Max (x,y)
def Max(x, y):
    """
    picks the largest value between x and y
    :param x:
    :param y:
    :return: x if x is larger than y, y otherwise
    """
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
    y = 2
    assign(x, y)
    print(x, y)
    print(equal(5, 2))
    print(not_equal(5, 2))
    print(greater(5, 2))
    print(less(5, 2))
    print(Or(5%2, 2%2))
    print(power(5, 2))
    print(sqrt(4))
    print(Min(5, 2))
    print(Max(5, 2))
    print(And(5%2, 2%2))
