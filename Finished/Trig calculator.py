import math
X = str(input("Name of Vertex 1 in upper case:"))
Y = str(input("Name of Vertex 2 in upper case:"))
Z = str(input("Name of Vertex 3 in upper case:"))
vertex_1 = input(str("Degree of " + X)+" ")
vertex_2 = input(str("Degree of " + Y)+" ")
vertex_3 = input(str("Degree of " + Z)+" ")
B = float(input("Degree of B:"))
C = float(input("Degree of C:"))
a = float(input("Length of a:"))
b = float(input("Length of b:"))
c = float(input("Length of c:"))
length_rounding = int(input("To what decimal place should I round lengths?:"))
degree_rounding = int(input("To what decimal place should I round angles?:"))
if type(A) == type(1) and 0<A<180:
    if type(B)== type(1) and  B>0 and A + B < 180:
        if type(C) == type(1) and A + B + C ==180:
            print("Infinite Solutions")
        else:
            print("Not a Triangle")
            



