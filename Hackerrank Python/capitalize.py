

'''
def solve(s):
    s = s.strip()
    new_list = []
    start = 0
    for i in range(len(s)):
        if s[i] != " " and s[i-1] == " ":
            new_list += [s[start:i]]
            start = i
    new_list += [s[start:]]

    string = ""
    for item in new_list:
        string += item.capitalize()

    return string


a = input()
solve(a)
'''


# *easier way to do the same thing
# * The capitalize method capitalizes the first letter of a string
# * Clean and easy to understand.
#!.replace method is very useful.
def solve(s):
    for item in s.split():
        # *The replace method is useful for only converting a part of a string.
        s = s.replace(item, item.capitalize())
    return s


a = input()
print(solve(a))
