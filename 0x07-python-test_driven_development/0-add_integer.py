#!/usr/bin/python3
""" add_integer function
"""


def add_integer(a, b=98):
    """
    # Write a function that adds 2 integers.
    # a and b must be integers or floats, otherwise raise a...
    ....TypeError exception with the message a must be an integer...
    ....or b must be an integer.
    # VARIABLE(" "):
    # add_integer(int): Integers addition
    # Return: an integer.. the addition of a and b
    """
    """Adds two integers.

    Args:
        a (int or float): The first number
        b (int or float, optional): The second number. Defaults to 98.

    Return:
        int: The addition of a and b.

    Raises:
        TypeError: if a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)