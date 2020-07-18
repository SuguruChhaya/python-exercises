'''
# * Approach 1: Don't even use the nested list and use a lot of for loops
if __name__ == '__main__':
    name_list = []
    score_list = []
    sorted_score_list = []
    runner_up_score = 0
    dictionary = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list += [name]
        score_list += [score]
        sorted_score_list += [score]
    # ?Python lists are mutable. That is why score_list and sorted_score_list have the same value
    # ?I think it is a good idea to make two separate lists in the for loop stage
    # ?So I don't need to base sorted_score_list off another list
    sorted_score_list.sort()
    #!I forgot that it was the second from the bottom we were looking for
    for item in range(len(sorted_score_list) - 1):
        if sorted_score_list[item] < sorted_score_list[item + 1]:
            runner_up_score = sorted_score_list[item + 1]
            break
    for make in range(len(name_list)):
        dictionary[name_list[make]] = score_list[make]
    #!The sorting is messing the dictionary up
    final_names = []
    for key, value in dictionary.items():
        if value == runner_up_score:
            final_names.append(key)
    final_names.sort()
    for item in final_names:
        print(item)
'''
'''
#* Approach 2: Actually use nested lists
marksheet = []
scoresheet = []
if __name__ == "__main__":
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #!Make sure to put two brackets around
        #!If I don't the list wouldn't be a nested list and I will have trouble while iterating
        marksheet += [[name, score]]
        scoresheet += [score]
    #!This following line gives the 2nd lowest mark
    #?Python sets are a different datatype from dictionaries.
    #?When converted to a set, all duplicates are deleted.
    #?Sets are immutable and isn't reliable to access through index because it can come out in random order
    #!But, after we sort the sort the set, we can confidently access it.
    #!You cannot prepare a set beforehand by assigning a variable to a "{}". This will cause to make a dictionary, not a set.
    #!The only way to make a set is by set()
    x = sorted(set(scoresheet))[1]
    for n, s in sorted(marksheet):
        if s == x:
            print(n)
'''
#*Approach 3: Similar to appraoch 2 but use dictionaries instead of nested lists
mydict = {}
score_tracker = []
if __name__ == "__main__":
    for i in range(int(input())):
        name = input()
        score = float(input())
        mydict[name] = score
        score_tracker +=[score]
    y = sorted(set(score_tracker))[1]
    #!I can also sort dictionaries, but in a different way
    #?https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/
    for i in sorted(mydict):
        if mydict[i] == y:
            print(i)

#*Reference
'''
a = [2,1]
b = a.sort()
print(b)
#!This will not return anything
#!The way to use sort() is after a list, and you can't print it.
b = sorted(a)
print(b)
#!But this returns [2,1]. sort() and sorted() do similar things but I have to use it in different ways

Additionally,
print(sorted(set([2,3,1])))
print({2,3,1}).sort()
.sort() is only for lists. but sorted() works for dictionary-like data structures too.

thislist = [1,1,2,3]
a = {}
for b in thislist:
    a.add(b)
print(a)
'''