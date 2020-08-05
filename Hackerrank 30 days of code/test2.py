import test1

print("top-level in two.py")
test1.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

#!As you will see, if you import test1.py, you run test1.py when you run test2.py
#!But since test1.py is imported the __name__ within test1.py would be "test1"
#!Then the rest of the code is run, with the name value of "__main__"