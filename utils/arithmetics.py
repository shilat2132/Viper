# Add (x+y)
def add(x: int or float, y: int or float):
    """
    Adds two numbers together.
    :param x: first number
    :param y: second number
    :return: x+y
    """""
    return x + y


# Sub (x-y)
def sub(x: int or float, y: int or float):
    """
    Subtracts two numbers together.
    :param x: first number
    :param y: second number
    :return: x-y
    """
    return x - y


# Mul(x*y)
def mul(x: int or float, y: int or float):
    """
    Multiplies two numbers together.
    :param x: first number
    :param y: second number
    :return: x*y
    """
    return x * y


# div(x/y) - throw an error if y=0
def div(x: int or float, y: int or float):
    """
    Divides two numbers together.
    :param x: first number
    :param y: second number
    :return: x/y
    """
    if y == 0:
        raise ArithmeticError("ZeroDivisionError - cannot divide by zero")
    return x / y


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
    return x > y


# >=
def greaterEquals(x, y):
    """
    Checks if x is greater than or equal to y
    :param x:
    :param y:
    :return: True if greater or equal, false otherwise
    """
    return x >= y


# Smaller (x<y)
def less(x, y):
    """
    Checks if x is less than y
    :param x:
    :param y:
    :return: True if less, false otherwise
    """
    return x < y


# <=
def lessEquals(x, y):
    """
    Checks if x is less than or equal to y
    :param x:
    :param y:
    :return: True if less or equal, false otherwise
    """
    return x <= y


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
    return x**y


# Square (x^0.5)
def sqrt(x):
    """
    calculates the square root of x
    :param x:
    :return: square root of x
    """
    return x ** 0.5


# Min (x,y)
def Min(x, y):
    """
    picks the smallest value between x and y
    :param x:
    :param y:
    :return: x if x is smaller than y, y otherwise
    """
    if x <= y:
        return x
    return y


# Max (x,y)
def Max(x, y):
    """
    picks the largest value between x and y
    :param x:
    :param y:
    :return: x if x is larger than y, y otherwise
    """
    if x <= y:
        return y
    return x


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
