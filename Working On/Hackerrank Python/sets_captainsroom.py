'''
#*I initially tried this code but took so much runtime (obviously)
len_dif = int(input())
my_list = list(input().strip().split())
my_set = set(my_list)
for item in my_set:
    if my_list.count(item) == 1:
        print(item)
'''
#*A simpler approach was to try doing it mathematically.
k = int(input())
my_list = list(map(int, input().strip().split()))
my_set = set(my_list)

#*Total if there were "k" number of captains.
setTotal = sum(my_set) * k
list_Total = sum(my_list)
captainDifference = (setTotal - list_Total) / (k - 1)
print(captainDifference)
