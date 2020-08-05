# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

a = int(input())
b = list(map(int, input().strip().split()))
b = Counter(b)
c = int(input())
total = 0
for i in range(c):
    size, price = map(int, input().strip().split())
    if size in b.keys() and b[size] > 0:
        total += price
        b[size] -= 1
        
print(total)


