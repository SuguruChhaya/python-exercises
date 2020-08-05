
#!Run test2.py
def func():
    print("func() in one.py")


print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
    print("__name__ is " + str(__name__))
