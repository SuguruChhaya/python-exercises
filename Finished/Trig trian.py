import math

def sine_law_to_solve_for_angle(a,B,b):
    return(math.asin((a * math.sin(B * math.pi /180)) / b) * 180 / math.pi)

def sine_law_to_solve_for_length(A,b,B):
    return((b * math.sin(A * math.pi / 180)) / (math.sin(B * math.pi / 180)))

def cosine_law_to_solve_for_angle(a,b,c):
    return((math.acos(((c ** 2) - (a ** 2) - (b ** 2)) / ((-2) * a * b))) * 180 / math.pi)

def cosine_law_to_solve_for_length(a,b,C):
    return(math.sqrt((a ** 2) + (b ** 2) - 2 * a * b * math.cos(C * math.pi / 180)))

X = input("Name of Vertex 1 in Upper Case: ")
Y = input("Name of Vertex 2 in Upper Case: ")
Z = input("Name of Vertex 3 in Upper Case: ")
if len(X) == len(Y) == len(Z) == 1 and X.isupper() and Y.isupper() and Z.isupper() and not (X == Y) and not(X == Z):
    A = str(input(str("Degree of " + X) + " = "))
    B = str(input(str("Degree of " + Y) + " = "))
    C = str(input(str("Degree of " + Z) + " = "))
    a = str(input(str("(No Units!!)Length of " + X.lower()) + " = "))
    b = str(input(str("(No Units!!)Length of " + Y.lower()) + " = "))
    c = str(input(str("(No Units!!)Length of " + Z.lower()) + " = "))
    d = input("What decimal place should I round lengths to?: ")
    e = input("What decimal place should I round degrees to?: ")
    if ((a).islower() or (a).isupper()):
        print("Enter Valid Lengths and Angle Measures!!")
    elif ((b).islower() or(b).isupper()):
        print("Enter Valid Lengths and Angle Measures!!")
    elif ((c).islower() or (c).isupper()):
        print("Enter Valid Lengths and Angle Measures!!")
    elif ((A).islower() or (A).isupper()):
        print("Enter Valid Lengths and Angle Measures!!")
    elif ((B).islower() or (B).isupper()):
        print("Enter Valid Lengths and Angle Measures!!")
    elif  ((C).islower() or (C).isupper()):
        print("Enter Valid Lengths and Angle Measures!!")
    elif (a).isalpha() or (b).isalpha() or (c).isalpha() or (A).isalpha() or (B).isalpha() or (C).isalpha():
        print("Enter Valid Lengths and Angle Measures!!")
    elif not (d).isdigit():
        print("Enter Valid Decimal Place to Round to!!")
    elif len(a) == 0:
        print("A")
    
    else:
        a = float(a)
        d = int(d)
        e = int(e)
        if len(b) == 0:
            if len(c) == 0:
                if len(A) == 0:
                    if len(B) == 0:
                        print("Unsolvable")
                    else:
                        B = float(B)
                        if len(C) == 0:
                            print("Unsolvable")
                        else:
                            #
                            C = float(C)
                            A = float(float(180) - B - C)
                            print(str(X) + " = " + str(round(float(A),e)))
                            print(str(Y).lower() + " = " + str(round(float(sine_law_to_solve_for_length(B,a,A)),d)))
                            print(str(Z).lower() + " = " + str(round(float(sine_law_to_solve_for_length(C,a,A)),d)))

                else:
                    A = float(A)
                    if len(B) == 0:
                        if len(C) == 0:
                            print("Unsolvable")
                        else:
                            C = float(C)
                            C = float(float(180) - A - B)
                            print(str(Z) + " = " + str(round(float(C),e)))
                            b = sine_law_to_solve_for_length(B,a,A)
                            print(str(Y).lower() + " = " + str(round(b,d)))
                            print(str(Z).lower() + " = " + str(round(float(cosine_law_to_solve_for_length(a,b,C)),d)))

                            
                    else:
                        
                        
            else:
                c = float(c)
                if len(A) == 0:
                    if len(B) == 0:
                        if len(C) == 0:
                            print("Unsolvable")
        else:
            b = float(b)
            if len(c) == 0:
                print("A")
            
            else:
                c = float(c)
                print(str(X) + " = " + str(round(float(cosine_law_to_solve_for_angle(b,c,a)),e)))
                print(str(Y) + " = " + str(round(float(cosine_law_to_solve_for_angle(a,c,b)),e)))
                print(str(Z) + " = " + str(round(float(cosine_law_to_solve_for_angle(a,b,c)),e)))
        
else:
    print("Enter Valid Vertices!!")
  
        
