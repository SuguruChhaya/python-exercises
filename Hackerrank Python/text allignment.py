'''
# *Interesting text allignment stuff
width = 20
print("Hackerrank".ljust(width, "-"))
print("Hackerrank".rjust(width, "-"))
print("Hackerrank".center(width, "-"))
'''
'''
#!Think of text allignments as how many blocks of "thicknesses" (in this case 5 "H"s per thickness)
thickness = 5
c = "A"

# Top cone
# ?This creates visualization
for i in range(thickness):
    print(((c * i).rjust(thickness)) + (c*(i-1)).ljust(thickness))

# Top pillars
for i in range(thickness):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Middle bar
for i in range(int((thickness + 1)/2)):
    print((c * (thickness * 5)).center(thickness * 6))

# bottom pillar
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c*thickness).center(thickness * 6))

# bottom cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c +
           (c * (thickness - 1 - i)).ljust(thickness)).rjust(thickness * 6))
'''
# * Part 2, designing a door mattress

row, column = map(int, input().strip().split())
# top
for i in range(int((row - 1) / 2)):
    print(('.|.' * (2 * i + 1)).center(column, "-"))

print(('WELCOME').center(column, '-'))

for i in range(int((row - 1) / 2), 0, -1):
    print(('.|.' * (2 * i -1)).center(column, '-'))
