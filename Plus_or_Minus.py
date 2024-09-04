"""
In this task you are required to determine an expression consisting of variables and operators.

The variables are all single lower-case alphabetic characters
Each variable occurs only once in the expression
The operators are either + or -
There are no parentheses.
For example: "x-y+z" or "-d-b-c+w"

You must implement a function plus_or_minus which will be passed two parameters:

variables : a string consisting of just the variables in the order that they appear in the expression. For example: "xyz" or "dbcw" (The length of the input string will be between 1 and 26 inclusive.)
test : a test function which takes as its parameter a list of numeric values to be substituted for the variables in variables. The function will return the result of evaluation the expression.
You must return the expression with the variables in the same order as the input and with the correct operators inserted. Omit any leading + from the start of the expression.

Example 1:

expression = "x-y+z"
variables = "xyz"
test([1, 2, 3]) = 2
Example 2:

expression = "-d-b-c+w"
variables = "dbcw"
test([3, 0, -1, 0.5]) = -1.5
Here's the catch: In each test case you may only call test once. Subsequent calls will return None

"""


def plus_or_minus(variables):
    if len(variables) not in range(1,27):
        raise "Vrong lenght"
    return '+'.join(variables)
    # a = ''.join([i for i in variables if i.isalpha()])
    # b = [i for i in range(1, len(a) + 1)]

    def test(values):
        pass

print(plus_or_minus("x+y-z"))



print(plus_or_minus("x-s+z"))
