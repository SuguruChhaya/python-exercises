def swap_case(string):
    check = 0
    current = ""
    while string[check].isupper:
        check = check + 1
        
        return string[check].lower()
    while string[check].islower:
        check = check + 1
    return string[check].upper()

print(swap_case("Hello"))