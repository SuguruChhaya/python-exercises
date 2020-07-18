import math
def solve_triangle (a,b,c,A,B,C):
    a = float(input("Length of a:"))
    b = float(input("Length of b:"))
    c = float(input("Length of c:"))
    A = float(input("Degree of A:"))
    B = float(input("Degree of B:"))
    C = float(input("Degree of C:"))
    length_rounding = int(input("To what decimal place should I round lengths?:"))
    degree_rounding = int(input("To what decimal place should I round angles?:"))
    if type(A) == type(1) and 0<A<180:
        if type(B)== type(1) and  A + B < 180:
            if type(C) == type(1) and A + B + C ==180:
                return "Infinite Solutions"
            else:
                return "Not a Triangle"


