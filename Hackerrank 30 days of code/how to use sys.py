# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
'''
n = int(input())

dictionary = {}
for i in range(0, n):
    divide = input().strip().split()
    dictionary[divide[0]] = divide[1]

find = sys.stdin.readline().strip()
# ?This is another way of saying input()
#!This while loop works because strings are usually assigned the value, "True"
#!I have to find how the to exit readline later
while find:
    phone_number = dictionary.get(find)
    if phone_number:
        print(f"{find} = {phone_number}")
    else:
        print("Not found")
    find = sys.stdin.readline().strip()
    #!There is a reason why this works and input() doesn't.
    # ?Check https://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu.
    #!Basically, readline() reads until there is no more input, successfully ending the while loop
    #!On the other hand, input() returns an EOF error (the one I got in hackerrank) when there are no more inputs
    #!If the code is testing for multiple lines of input at once, it will be a better practice to use readline
    # ?Also, both int, and readline accept empty spaces, so it might be a good practice to strip() it so unintentional empty spaces
    # ?don't affect the input
'''

