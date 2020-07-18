def my_power(base, exponent):
    total = 1 
    while exponent > 0:
        exponent = exponent - 1
        total = total * base
    return total
        
print(my_power(5.5, 4))