#!/usr/bin/env python3
def multiply_and_square(a, b):
    """
    Multiplies two positive integers and raises the result to the power of 2.

    Args:
        a (int): The first positive integer.
        b (int): The second positive integer.

    Returns:
        int: The squared result of the multiplication.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive integers")
    result = a * b
    squared_result = result ** 2
    print(squared_result)

multiply_and_square(2,3)
