def no_nums(string):
    check = 0
    current = ""
    if not string[check].isdigit:
        while not string[check].isdigit:
            current = current + string[check]
            check = check + 1
    if string[check].isdigit:
        while string[check].isdigit:
            check = check + 1
    return current
    
print(no_nums("yeet7"))