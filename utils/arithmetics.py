# Add (x+y)
def add(x, y):
    """
        Adds two numbers and returns the result.

        Parameters:
        x (int or float): The first number.
        y (int or float): The second number.

        Returns:
        int or float: The sum of x and y.

        Raises:
        TypeError: If the parameters are not numbers.
        """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x + y
    print("the parameters are not numbers")
    return


# Sub (x-y)
def sub(x, y):
    """
        Subtracts the second number from the first and returns the result.

        Parameters:
        x (int or float): The first number.
        y (int or float): The second number.

        Returns:
        int or float: The difference between x and y.

        Raises:
        TypeError: If the parameters are not numbers.
        """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x - y
    print("the parameters are not numbers")
    return

#
# Mul(x*y)
def mul(x, y):
    """
        Multiplies two numbers and returns the result.

        Parameters:
        x (int or float): The first number.
        y (int or float): The second number.

        Returns:
        int or float: The product of x and y.

        Raises:
        TypeError: If the parameters are not numbers.
        """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x * y
    print("the parameters are not numbers")
    return


# div(x/y) - throw an error if y=0
def div(x, y):
    """
        Divides the first number by the second and returns the result. Raises an error if the divisor is zero.

        Parameters:
        x (int or float): The dividend.
        y (int or float): The divisor.

        Returns:
        float: The quotient of x and y.

        Raises:
        ArithmeticError: If y is zero.
        TypeError: If the parameters are not numbers.
        """

    if y == 0:
        raise ArithmeticError("ZeroDivisionError - cannot divide by zero")
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x / y
    raise TypeError("the parameters are not numbers")


# Assign(x=y) variables are in dictionary
def assign(varsDict: dict, x: str, y):
    """
        Assigns the value of y to the variable x in the provided dictionary.

        Parameters:
        varsDict (dict): The dictionary storing variables.
        x (str): The variable name.
        y (any): The value to assign to the variable.
        """

    varsDict[x] = y

# Equal (x==y)
def equal(x, y):
    """
        Checks if two values are equal.

        Parameters:
        x: The first value.
        y: The second value.

        Returns:
        bool: True if x equals y, otherwise False.
        """

    return x == y


# Not Equal (x!=y)
def not_equal(x, y):
    """
        Checks if two values are not equal.

        Parameters:
        x: The first value.
        y: The second value.

        Returns:
        bool: True if x does not equal y, otherwise False.
        """

    return x != y


# not
def negate(expression):
    """
        Negates the boolean value of an expression.

        Parameters:
        expression (bool): The boolean expression to negate.

        Returns:
        bool: The negated boolean value.
        """

    return not expression


# Greater (x>y)
def greater(x, y):
    """
        Checks if the first number is greater than the second.

        Parameters:
        x (int or float): The first number.
        y (int or float): The second number.

        Returns:
        bool: True if x is greater than y, otherwise False.

        Raises:
        TypeError: If the parameters are not numbers.
        """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x > y
    raise TypeError("the parameters are not numbers")


# >=
def greaterEquals(x, y):
    """
       Checks if the first number is greater than or equal to the second.

       Parameters:
       x (int or float): The first number.
       y (int or float): The second number.

       Returns:
       bool: True if x is greater than or equal to y, otherwise False.

       Raises:
       TypeError: If the parameters are not numbers.
       """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x >= y
    raise TypeError("the parameters are not numbers")


# Smaller (x<y)
def less(x, y):
    """
       Checks if the first number is smaller than the second.

       Parameters:
       x (int or float): The first number.
       y (int or float): The second number.

       Returns:
       bool: True if x is smaller than y, otherwise False.

       Raises:
       TypeError: If the parameters are not numbers.
       """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x < y
    raise TypeError("the parameters are not numbers")


# <=
def lessEquals(x, y):
    """
        Checks if the first number is smaller than or equal to the second.

        Parameters:
        x (int or float): The first number.
        y (int or float): The second number.

        Returns:
        bool: True if x is smaller than or equal to y, otherwise False.

        Raises:
        TypeError: If the parameters are not numbers.
        """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x <= y
    raise TypeError("the parameters are not numbers")


# Or (x || y)
def Or(x, y):
    """
        Performs a logical OR operation between two expressions.

        Parameters:
        x (bool): The first expression.
        y (bool): The second expression.

        Returns:
        bool: True if either x or y is True, otherwise False.
        """

    if x or y:
        return True
    return False


# And (x&y)
def And(x, y):
    """
        Performs a logical AND operation between two expressions.

        Parameters:
        x (bool): The first expression.
        y (bool): The second expression.

        Returns:
        bool: True if both x and y are True, otherwise False.
        """

    if x and y == 1:
        return True
    return False


# Power (x^y)
def pow(x, y):
    """
        Raises the first number to the power of the second number.

        Parameters:
        x (int or float): The base number.
        y (int or float): The exponent.

        Returns:
        int or float: The result of x raised to the power of y.

        Raises:
        TypeError: If the parameters are not numbers.
        """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        return x ** y
    raise TypeError("the parameters are not numbers")


# Square (x^0.5) - add to rules
def sqrt(x):
    """
        Returns the square root of a number.

        Parameters:
        x (int or float): The number to find the square root of.

        Returns:
        float: The square root of x.

        Raises:
        TypeError: If the parameter is not a number.
        """

    if isinstance(x, int) or isinstance(x, float):
        return x ** 0.5
    raise TypeError("the parameters are not numbers")


# Min (x,y)
def min(x, y):
    """
        Returns the smaller of two numbers.

        Parameters:
        x (int or float): The first number.
        y (int or float): The second number.

        Returns:
        int or float: The smaller of x and y.

        Raises:
        TypeError: If the parameters are not numbers.
        """

    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        if x <= y:
            return x
        return y
    raise TypeError("the parameters are not numbers")


# Max (x,y)
def max(x, y):
    """
        Returns the larger of two numbers.

        Parameters:
        x (int or float): The first number.
        y (int or float): The second number.

        Returns:
        int or float: The larger of x and y.

        Raises:
        TypeError: If the parameters are not numbers.
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
    print(Or(5 % 2, 2 % 2))
    print(pow(5, 2))
    print(sqrt(4))
    print(min(5, 2))
    print(max(5, 2))
    print(And(5 % 2, 2 % 2))
