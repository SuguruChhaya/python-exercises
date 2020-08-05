from itertools import permutations

string, number = input().strip().split()
number = int(number)

my_list = []
for i in string:
    my_list.append(i)

my_list.sort()
save = list(permutations(my_list, number))

for item in save:
    print("".join(item))
