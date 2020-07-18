BULLETS = 351
FINE = 321
BRILLIANT = 291
SUPERIOR = 261
LARGE = 231
EXTRA_LARGE = 201
JUMBO = 181
EXTRA_JUMBO = 161
GIANT = 141
COLOSSAL = 121
SUPER_COLOSSAL = 111
MAMMOTH = 101
SUPER_MAMMOTH = 91

def olive_sizes(number):
    """Returns a string for the type of olive
       given the number per kilogram.

       Preconditions:
       number: integer in range from 91 to 351, inclusive

       Parameter:
       number: number of olives in one kilogram

       Return: a string giving type of olive
    """

    if number < MAMMOTH:
        return "Super Mammoth"
    elif number < SUPER_COLOSSAL:
        return "Mammoth"
    elif number < COLOSSAL:
        return "Super Colossal"
    elif number < GIANT:
        return "Colossal"
    elif number < EXTRA_JUMBO:
        return "Giant"
    elif number < JUMBO:
        return "Extra Jumbo"
    elif number < EXTRA_LARGE:
        return "Jumbo"
    elif number < LARGE:
        return "Extra Large"
    elif number < SUPERIOR:
        return "Large"
    elif number < BRILLIANT:
        return "Superior"
    elif number < FINE:
        return "Brilliant"
    elif number < BULLETS:
        return "Fine"
    else:
        return "Bullets"

print(olive_sizes(351))