# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

dictionary = {}
for i in range(0, n):
    divide = input().strip().split()
    dictionary[divide[0]] = divide[1]
find = input()
if find in dictionary:
    print(f"{find} = {dictionary[find]}")
else:
    print("Not found")
