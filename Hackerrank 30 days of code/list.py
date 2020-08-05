
#!The list function checkes whether the items are covered with a []
#!If not, the list creates it
#!If it is, the list() doesn't do anything.
a = (1, 2, 3, 4, [5, 6, 7, 8], 9)
print(list(a))

b = [[[2, 3, 4]]]
print(list(b))


#!As you can see by running the following code, by using map() we can iterate over a sequence
#!and put them into a function. The list itself only contains what was returned, but the map()
#!also runs the steps in between (e.g. print("haha"))
def add(integer):
    print("haha")
    return integer + 1

print(list(map(add, (1, 2, 3))))

##The following is the hackerrank example
#?arr = list(map(int, input().rstrip().split()))

##The following explains it well
#https://www.quora.com/What-does-the-following-line-mean-in-Python-list-map-int-input-strip-split-I

#?strip() removes all trailing spaces from the BEGINNING AND THE END
#?rstrip() removes all trailing spaces from the END only
#?lstrip() removes all trailing spaces from the BEGINNING only
