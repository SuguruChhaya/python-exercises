import math
def sine_law_to_solve_for_angle(a,B,b):
    return(math.asin((a * math.sin(B * math.pi /180)) / b) * 180 / math.pi)

print(sine_law_to_solve_for_angle(44,60,7))