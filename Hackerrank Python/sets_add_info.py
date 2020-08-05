num = int(input())
#!To declare a set, I cannot use {} since this is for dictionaries.
my_set = set()
for i in range(num):
    country = input()
    my_set.add(country)

print(len(my_set))
