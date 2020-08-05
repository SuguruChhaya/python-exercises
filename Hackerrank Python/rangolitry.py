'''
row_alpha = chr(96 + 3)
current_ord = 96 + 3
#*Top including middle bar
for i in range(3):
    for a in range(i):
        print(row_alpha)
        row_alpha += ("-" + chr(current_ord - 1))
        current_ord -= 1
        print(row_alpha)

'''

row_alpha = chr(96 + 3)
print(row_alpha)
current_ord = 96 + 3
for i in range(1, 3):
    row_alpha += "-" + chr(current_ord - i)
    print(row_alpha)
