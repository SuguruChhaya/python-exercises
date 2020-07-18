
# *lambda has a couple of useful functions with it.

# *1. Reduce (have to import from functools)
# ?reduce iterates over a string
from fractions import Fraction
from functools import reduce
#print(reduce(lambda x, y: x - y, [1, 2, 3], 3))


def add(x, y):
    return x + y


# *The reduce function can also pass custom functions.
#print(reduce(add, [1, 2, 3]))
'''
def product(fracs):
    t = reduce(lambda x, y: x / y, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    #!fracs is already a list
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    # *Returns as a tuple
    print(type(result))
    print(*result)
    #! "*" somehow removes the brackets
    # * This works for lists and sets as well

# *The Fraction method from the fraction module converts a float to a reduced fraction
# * A comma separates the numerator and the denominator
a = {2, 3}
print(type(a))
print(a)
print(*a)
'''
# *arg receives numbers as a tuple.
#!I should study more about *arg and kwarg


def function(*argv):
    print(type(argv))
    for i in argv:
        print(i)


function(2, 2)
