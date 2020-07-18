from collections import OrderedDict

#*Ordered dict acts like a dictionary which stores order of keys inserted.
'''
my_dict = OrderedDict()
my_dict['c'] = 3
my_dict['a'] = 2
my_dict['b'] = 1
sorted(my_dict)
print(my_dict)

#8prints key
for i in my_dict:
    print(i)
'''
'''
num = int(input())
my_dict = OrderedDict()
final = ""

for i in range(1, num + 1):
    a = input()
    my_dict[a] = i
    if a not in final:
        final += a + "\n"

print(final)
'''
'''
my_tuple = ("Suguru", "Chhaya")
#*I can join items in a tuple too!!
print(" ".join(my_tuple))
'''
'''
my_tuple = {"Suguru": "Chhaya"}
#*I can join items in a tuple too!!
for key, item in my_tuple.items():
    #!The on top works the best. The bottom is a rather tedious way.
    #print(key, item)
    print(" ".join([key, item]))
'''
'''
num = int(input())
my_dict = OrderedDict()
final = ""
for i in range(1, num + 1):
    a = list(input().strip().split())
    name, price = " ".join(a[:-1]), int(a[-1])
    if name in my_dict:
        my_dict[name] += price
    else:
        my_dict[name] = price



for key, value in my_dict.values():
    print(key, value)
'''

my_dict = OrderedDict()
first_line = 0
second_line = ""
num = int(input())
for i in range(num):
    a = input()
    if a in my_dict:
        my_dict[a] = str(int(my_dict[a]) + 1)
    else:
        my_dict[a] = "1"
        first_line += 1

print(first_line)
print(" ".join(my_dict.values()))