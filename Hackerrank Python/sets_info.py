
#*sets are surrounded with curly brackets. Same values are deleted, and is printed in random order.
#*I can use sorted to put in order, but that makes it a list.
'''
print(len(set("abca")))

print(sorted(set([1,2,3,1,4,0,2,3,1,2])))

#*In default when a dictionary is made into a set, it contains only the keys.
print(set({"Suguru":"Chhaya", "age":"15"}))
print(set({"Suguru":"Chhaya", "age":"15"}.values()))

a = set({"Suguru":"Chhaya", "age":"15"}.items())
print(a)

#!I can't run the code below because I can't slice sets
#print(type(a[0]))
for item in a:
    print(item)
    print(type(item))

#*This shows that a dictionary key, value pairs are stored as tuples in a set

#*enumerate can keep track of the original order
print(set(enumerate("Suguru")))

'''
def average(array):
    # your code goes here
    my_set = set(array)
    total = 0
    for item in my_set:
        total += item

    return total / len(my_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

