def exchange_first_and_middle_character(string):
    return string[(len(string) - 1) / 2] + string[1:(len(string) - 3) / 2] + string[0] + string[((len(string) + 1) / 2):]

print(exchange_first_and_middle_character("water"))