import math
def exchange(entry):
    """Returns string with middle and last
       character exchanged.

       Preconditions:
       entry: string of odd length > 0

       Parameter:
       entry: string as basis for new string

       Returns: string like entry but with
                middle and last positions exchanged
    """

    
    mid = math.floor(len(entry) / 2)
    first_part = entry[:mid]
    middle_char = entry[mid]
    second_part = entry[mid + 1:mid * 2]
    last_char = entry[mid * 2]
    return first_part + last_char + second_part + middle_char

print(exchange("caterpillar"))
print(exchange("cat"))