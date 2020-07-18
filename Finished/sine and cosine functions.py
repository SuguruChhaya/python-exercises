import math
a = 5+6
def ree(a):
    return a-6

print(ree(a))

print(math.degrees(math.asin(0.5)))

def sine_law_to_solve_for_angle(a,b,B):
    return (math.asin((a * math.sin(B * math.pi /180)) / b) * 180 / math.pi)
c = (sine_law_to_solve_for_angle(4, 6, 190)) * 2
#An example of how to manipulate calculations given even further
print(c)

def sine_law_to_solve_for_length(A,b,B):
    return((b * math.sin(A * math.pi / 180)) / (math.sin(B * math.pi / 180)))
print(sine_law_to_solve_for_length(30,5,63))

def cosine_law_to_solve_for_angle(a,b,c):
    return((math.acos(((c ** 2) - (a ** 2) - (b ** 2)) / ((-2) * a * b))) * 180 / math.pi)
print(cosine_law_to_solve_for_angle(5,6,8))

def cosine_law_to_solve_for_side(a,b,C):
    return(a ** 2) + (b ** 2) - 2 * a * b * math.cos(C * math.pi / 180)
print(cosine_law_to_solve_for_side(4,5,60))

import math
def sine_law_to_solve_for_angle(a,B,b):
    return(math.asin((a * math.sin(B * math.pi /180)) / b) * 180 / math.pi)

def sine_law_to_solve_for_length(A,b,B):
    return((b * math.sin(A * math.pi / 180)) / (math.sin(B * math.pi / 180)))

def cosine_law_to_solve_for_angle(a,b,c):
    return((math.acos(((c ** 2) - (a ** 2) - (b ** 2)) / ((-2) * a * b))) * 180 / math.pi)

def cosine_law_to_solve_for_side(a,b,C):
    return(a ** 2) + (b ** 2) - 2 * a * b * math.cos(C * math.pi / 180

X = str(input("Name of Vertex 1 in Upper Case:"))
Y = str(input("Name of Vertex 2 in Upper Case:"))
Z = str(input("Name of Vertex 3 in Upper Case:"))
#Have to make sure X,Y,and Z are upper case strings
if type(X) == type(Y) == type(Z) == type("") and len(X) == len(Y) == len(Z) == 1 and X.isupper() and Y.isupper() and Z.isupper():
    A = input(str("Degree of " + X) + " ")
    B = input(str("Degree of " + Y) + " ")
    C = input(str("Degree of " + Z) + " ")
    a = input(str("\

