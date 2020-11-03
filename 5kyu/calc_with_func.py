# This time we want to write calculations using functions and get the results. 
# Let's have a look at some examples:
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
#    Requirements:
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))


def zero(func=0):
    if func:
        answ = func(0)
        return answ
    return 0               
def one(func=0):
    if func:
        answ = func(1)
        return answ
    return 1
def two(func=0):
    if func:
        answ = func(2)
        return answ
    return 2
def three(func=0):
    if func:
        answ = func(3)
        return answ
    return 3
def four(func=0):
    if func:
        answ = func(4)
        return answ
    return 4
def five(func=0):
    if func:
        answ = func(5)
        return answ
    return 5
def six(func=0):
    if func:
        answ = func(6)
        return answ
    return 6
def seven(func=0):
    if func:
        answ = func(7)
        return answ
    return 7
def eight(func=0):
    if func:
        answ = func(8)
        return answ
    return 8
def nine(func=0):
    if func:
        answ = func(9)
        return answ
    return 9


def plus(num1):
    return lambda x: x + num1
def minus(num1):
    return lambda x: x - num1
def times(num1):
    return lambda x: x * num1
def divided_by(num1):
    return lambda x: x / num1


print(seven(times(five())))