from collections import defaultdict
#*This will give me a key error
'''
a = {}
print(a[0])
'''
'''
#!The difference for default keys is that I can assign a function for when the key has not been assigned yet
def func():
    return "No key yet"

a = defaultdict(func)
print(a['a'])


#*For this case, everytime the key doesn't exist, a list is assigned for the key. Things can then be appended to it.
b = defaultdict(list)
print(b["a"])
b['a'].append("b")
b["a"].append("c")
print(b)
'''

d = defaultdict(list)
first, second = map(int, input().strip().split())

for i in range(first):
    d[input()].append(str(i + 1))


print(d)

final = ""
for h in range(second):
    b = input()
    if b in d.keys():
        #*I have to make sure items in the list are strings to join them
        #*cannot let it print while input is still running

        final += " ".join(d[b]) + "\n"
    else:
        #!Don't forget to indent!!
        final += "-1\n"

print(final)
