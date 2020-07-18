def uk_code(entry):
    def code_ending(x):
       """Determines if a string can be a postal code.

       Preconditions:
       entry: string of letters, digits, spaces only

       Parameters:
       entry: possible postal code

       Returns "Code" if of one of the following forms:
       "A9 9AA", "A9A 9AA", "A99 9AA", "AA9 9AA",
       "AA9A 9AA", "AA99 9AA" where 9 is any digit and
       A is any letter,
       and "Not code" otherwise
       """
    ## Return "Not code" if the length is not between 6 and 8
        if not len(x) == (6 or 7 or 8):
            return "Not Code"
    ## Return "Not code" if it does not start with a letter 
    ## or end of the form  ' 9AA'
        elif not type(x[-3]) == type(1) and type(x[0]) == type(x[-1]) == type(x[-2]) == type("") and type(x[-4]).isspace:
            return "Not Code"
    ## Return "Code" for valid codes of length 6
        elif len(x) == 6 and type(x[1]) == type(1):
            return "Code"
    ## Return "Code" for valid codes of length 7
        elif len(x) == 7 and type(x[1]) == type(1) and type(x[2]) == (type(1) or type("")):
            return "Code"
    ## Return "Code" for valid codes of length 8
        elif len(x) == 8 and type(x[1]) == type(1) and type(x[2]) == type(1) and type(x[3]) == (type(1) or type("")):
            return "Code"
    ## Return "Not code" for all other inputs
        else:
            return "Not Code"


