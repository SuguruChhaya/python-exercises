happy_count, unhappy_count = input().strip().split()
array = list(input().strip().split())


happy_set = set(input().strip().split())
unhappy_set = set(input().strip().split())


happiness = 0
for item in array:
    if item in happy_set:
        happiness += 1
    elif item in unhappy_set:
        happiness -= 1

print(happiness)
