
# ?This hackerrank question asks to find the runners up number in a list of numbers

# *First approach: sort the list and run a forloop
#!"n" is the number of items the number will contain
from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
#!This is how you can sort a list. You can only print the sorted list on the next line.
arr.sort()
#!Can be confusing but remeber that the ending is not inclusive
for i in range(n - 1, 0, -1):
    if arr[i] != arr[i - 1]:
        print(arr[i - 1])
        break
'''
# *Second approach: Create a list with duplicates delted
n = int(input())
arr = list(map(int, input().split()))

new_list = []
for item in range(n):
    if not arr[item] in new_list:
        new_list.append(arr[item])
new_list.sort()
print(new_list[-2])


# *Third approach: Delete the duplicates using "Counter" from the 'collections' library
#!One demerit of this method is that the "n" value really means nothing.
if __name__ == '__main__':
    n = int(input())
    # ?The "Counter" makes a dictionary in which the keys are the numbers in the list and the list.
    # ?The values are how many times they show up in the list
    # ?Using ".keys()", I can extract the keys and make them in a list in which all the duplicates are removed
    arr = list(Counter(map(int, input().split())).keys())
    arr.sort()
    print(arr[-2])
'''