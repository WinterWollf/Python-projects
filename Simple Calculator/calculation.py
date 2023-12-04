import math


def calculation(type, n1=2, n2=1):
    if type == '+':
        return addition(n1, n2)
    elif type == '-':
        return subtraction(n1, n2)
    elif type == '*':
        return multiplication(n1, n2)
    elif type == '/':
        return division(n1, n2)
    elif type == '^':
        return to_power(n1, n2)
    elif type == "Square root":
        if n1 >= 0:
            return square_root(n1)
        else:
            return "Nan"
    else:
        return False


def addition(n1, n2):
    """Funtion takes two numbers and returns their addition result"""
    return n1 + n2


def subtraction(n1, n2):
    """Function takes two numbers and returns their subtraction result"""
    return n1 - n2


def multiplication(n1, n2):
    """Function takes two numbers and returns their multiplication result"""
    return n1 * n2


def division(n1, n2):
    """Function takes two numbers and returns their division result. Function provides exceptions checking"""
    if n2 == 0:
        return "nan"
    else:
        return n1 / n2


def square_root(n1):
    """Function takes a number and returns its square root"""
    return math.sqrt(n1)


def to_power(n1, power=1):
    """Function takes a number, a power and returns result of the number raised to the power"""
    return n1 ** power