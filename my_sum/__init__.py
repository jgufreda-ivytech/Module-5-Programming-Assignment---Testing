# Joseph Gufreda
# Module 5 Programming Assignment - Testing
# From https://realpython.com/python-testing/#testing-your-code
# Defines sum function that iterates over arg, adding to itelf over each loop, then returning total

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total