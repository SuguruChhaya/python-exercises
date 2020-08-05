
# ?In this question, x, y, and z are dimensions of a 3D rectangular prism.
# ?I have to print[i,j,k] so that i<=x, j<=y, k<=z and i+j+k != n

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i, j, k] for i in range(x + 1) for j in range(y + 1)
       for k in range(z + 1) if ((i + j + k) != n)])

#!This is basically a for loop written short

#!Equivalent for loop is:
final = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                final += [[i, j, k]]
print(final)
