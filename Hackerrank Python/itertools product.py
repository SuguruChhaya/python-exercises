from itertools import product
A = [[1, 2, 3]]
# print(*A)

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
print(*list(product(a, b)))
