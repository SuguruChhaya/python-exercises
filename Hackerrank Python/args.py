# *arg receives numbers as a tuple.
#!I should study more about *arg and kwarg

# **args stands for arguements. The function can take in as many arguments as I want.

# *According to https://stackoverflow.com/questions/46794115/passing-a-tuple-in-args, I can also uppack tuples
# *using *
def function(*args):
    # *args is always a tuple (because the function argument is covered with a "()". * unpacks the brakcets.)
    print(args)
    print(*args)
    print(type(args))
    #*args arguments are tuples meaning they are ITERABLE
    for i in args:
        print(i)


a = (2, 2)
b = [2, 2]
#!In the first case, there is one argument, (2,2)
function(a)
#!In the second case, there are two arguments, 2 and 2, since the tuple is unpacked.
function(*a)
# *Just to show that the unpacking process works for lists too.
function(b)


def func2(arg1, *args):
    print(f"First argument: {arg1}")
    # *Even after one or more arguments are extracted from the tuple, args remains as a tuple
    print(f"Other arguments: {args}")
    for i in args:
        print(f"Other argements: {i}")


func2("Hi", "my", "name", "is", "suguru")
