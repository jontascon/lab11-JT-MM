# https://github.com/jontascon/lab11-JT-MM
# Partner 1: Jon Tascon
# Partner 2: Jon Tascon
# Partner two is the same as one due to lack of response from Matthew Merrell.

import math

def square_root(a):
    if a < 0:
        raise ValueError("square_root undefined for negative numbers")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b