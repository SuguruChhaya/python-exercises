
# *kwargs is used keyword argument which works exactly like dictionaries.

def kwargsfunc1(**kwargs):
    #!The for loop works very much like dictionaries.
    '''
    for key, value in kwargs.items():
        #* "%" is an old-school method to format strings. It is like .format and f""
        print("%s == %s" % (key, value))
    '''
    for key in kwargs.keys():
        print(key)


def kwargsfunc2(kwargs):
    for key in kwargs.keys():
        print(key)


# *This is one way to pass a non-dictionary argument.
kwargsfunc1(Myname="Suguru", Myage="15")
# *A double asterisk can unpack dictionaries and the function repacks it into dictionaries
kwargsfunc1(**{"Myname": "Suguru", "Myage": "15"})
#!When the function doesn't pass the argument as a dictionary, this can be easier
kwargsfunc2({"Myname": "Suguru", "Myage": "15"})


def myFun(arg1, arg2, arg3):
    # *If the input is a **kwargs, arg1 will be assigned to the value.
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ["Geeks", "for", "Geeks"]
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
#!This one works as well, but it can be an extra step unpacking and packing again.
myFun('geeks', 'for', 'geeks', **
      {"first": "Geeks", "mid": "for", "last": "Geeks"})
      