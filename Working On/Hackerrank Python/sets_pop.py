'''
#*Another method is pop() which removes an item from the sequence and can store the item.
#!In lists, I can remove items based on indexes, but since sets are not in order, pop() can't take any arguments.
my_set = {2, 3,4,5}
a= my_set.pop()
b = my_set.pop()
print(my_set)
print(a)
print(b)
'''

#*For the pop() example where no second arguument will be given, I can use the exception of ValueError
n = int(input())
s = set(map(int, input().split()))

num2 = int(input())
for i in range(num2):
    try:
        input_string = input().strip()
        command, value = input_string.split()
        if command == "remove":
            try:
                s.remove(int(value))
            except KeyError:
                pass
        elif command == "discard":
            s.discard(int(value))
    except ValueError:
        if input_string == "pop":
            s.pop()

print(sum(s))