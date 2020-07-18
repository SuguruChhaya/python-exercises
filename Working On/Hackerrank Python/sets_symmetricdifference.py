'''
#*To add an item to a set use either the add or update method.
#!add() adds a single item to a list while update iterates over a list, set etc and adds the elements separately.

my_set = {1, 2, 3}
my_set2 = {1,2,6,7}
my_set.add(("3","4"))
my_set.update([3,4,5])


#*To remove an item, use the discard method
my_set.discard(3)
print(my_set)
print(my_set2)

#*There are couple of functions to compare two or more sets.
#Exist in either sets
print(my_set.union(my_set2))

#Exist in both sets
print(my_set.intersection(my_set2))

#Exist in a but not in b
print(my_set.difference(my_set2))
'''
#*Whenever I sort a set, the result is a list
print(sorted({'1', '3', '2'}))

first_input = int(input())
first_set = set(list(input().strip().split())[:first_input])
second_input = int(input())
second_set = set(list(input().strip().split())[:second_input])
first_set_union = first_set.union(second_set)
second_set_dif = first_set.intersection(second_set)
first_set_dif = first_set_union.difference(second_set_dif)
#!Remember that for strings, '11' is smaller than '5' because the first character is compared.
#*I had to convert them into int first, sort them, and reconvert them into string so I could join them.
print("\n".join(map(str, sorted(map(int, first_set_dif)))))

