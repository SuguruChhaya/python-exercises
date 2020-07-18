#Building better programs step 9
def my_function(first, second):
    second = second - first
    third = 10 + (second - first)
    return third

print(my_function(1, 100))

#iretation
def repeat_print(num):
    """Prints the input num times.
 
       Preconditions:
       num: positive integer 
    
       Parameter:
       num: the number of times and what is printed

       Side effect: prints num num times.
   """
    count = num
    while count > 0:
        print(num)
        count = count - 1

repeat_print(5)

def increase(num):
    """Determines the sum of num down to 1.

       Preconditions:
       num: int > 0

       Parameter:
       num: the starting number

       Returns: sum of num down to 1
    """
    total = 0
    while num > 0:
        total = total + num
        num = num - 1
    return total

print(increase(5))

def my_power(base, exponent):
    total = 1
    while exponent > 0:
        total = base * total
        exponent = exponent - 1
    return total

def add_up():
    response = input()
    total = 0
    while response != "Stop":
        total = int(response) + total
        print(total)
        response = input("Say Stop:")
    return total

print(add_up())

def no_nums(string):
    index = 0
    total = ""
    while index < len(string):
        if string[index].isdigit():
            index = index + 1
        else:
            total = total + string[index]
            index = index + 1
    return total

print(no_nums("d34"))
    
def swap_case(string):
    index = 0
    total = ""
    while index < len(string):
        if string[index].isupper():
            total = total + string[index].lower()
            index = index + 1
        elif string[index].islower():
            total = total + string[index].upper()
            index = index + 1
    return total

print(swap_case("abFAH"))
            
        
def multisplit(total, split):
    count = 0
    while total > 1:
        total = total / split
        count = count + 1
    return count

print(multisplit(8, 3))
    
#Storing elements in a sequence
def sum (seq):
    total = 0
    counter = 0
    while counter < len(seq):
        total = total + seq[counter]
        counter = counter + 1
    return total

def is_multiple(number, factor):
    return number % factor == 0

def divides_all(seq, factor):
    counter = 0
    while counter < len(seq):
        if is_multiple(seq[counter], factor) == False:
            return False
            counter = counter + 1
        counter = counter + 1
    return True

print(divides_all([4,6,12],2))

def remove_zero(a):
    if 0 in a:
        counter = 0
        while counter < len(a):
            if a[counter] == 0:
                a.remove(0)
            elif a[counter] != 0:
                counter = counter + 1
        return a
    
def no_zero(seq):
    new = []
    counter = 0
    while counter < len(seq):
        if seq[counter] == 0:
            counter = counter + 1
        elif seq[counter] != 0:
            new = new + [seq[counter]]
            counter = counter + 1
    return new

def reverse(seq):
    front = 0
    back = len(seq) - 1
    while (front <= len(seq) / 2) and (back >= len(seq) / 2):
        temp = seq[front]
        seq[front] = seq[back]
        seq[back] = temp
        front = front + 1
        back = back - 1
    return seq

print(reverse([]))

#Iteration using for
def has_digit(word):
    for char in word:
        if char.isdigit():
            return True
    else:
        return False
        
print(has_digit("sefweifiu43rsdfer"))

def my_power(base, exponent):
    total = 1
    for count in range(1, exponent + 1):
        total = total * base
    return total
    
print(my_power(2,3))

def no_nums(word):
    new = ""
    for char in word:
        if not char.isdigit():
            new = new + char
    return new

print(no_nums("sadjkew32joidjsif34"))
            
def swap_case(word):
    new = ""
    for char in word:
        if char.isupper():
            new = new + char.lower()
        elif char.islower():
            new = new + char.upper()
        else:
            new = new + char
    return new
    
def is_multiple(number, factor):
    return number % factor == 0
    
#Step 10
def rel_prime(a, b):
    if a < b:
        for counter in range(2, b + 1):
            if a % counter == 0 and b % counter == 0:
                return False
        return True
    if a > b:
        for counter in range(2, b + 1):
            if a % counter == 0 and b % counter == 0:
                return False
        return True

print(rel_prime(3,8))

def password(string):
    if len(string) >= 8:
        for upper in range(0, len(string)):
            if string[upper].isupper():
                for lower in range(0, len(string)):
                    if string[lower].islower():
                        for digit in range(0, len(string)):
                            if string[digit].isdigit():
                                return True
                            
    return False
           
def equals(a,b):
    if len(a) == len(b) == 0:
        return True
    elif len(a)==len(b):
        for checker in range(0, len(a)):
            if a[checker] == b[checker]:
                return True
            else:
                return False
    else:
        return False

print(equals([],[]))

def multisplit(total, split):
    count = 0
    for a in range(0, total):
        total = total / split
        count = count + 1
        if total <= 1:
            return count

print(multisplit(12, 3))

#Caeser's code
def helper(char, move):
    if move <= 0:
        if 90 >= ord(char) > (64 - move):
            a = ord(char) + move
            return chr(a)
        elif (64 - move) >= ord(char) >= 65:
            b = ord(char) - 65
            c = move + b
            return chr(91 + c)
    elif move > 0:
        if 90 >= ord(char) >= (91 - move):
            d = 90 - ord(char)
            e = move - d
            return chr(64 + e)
        elif (91 - move) > ord(char) >= 65:
            f = ord(char) + move
            return chr(f)

def caesar(string, offset):
    new = ""
    for counter in range(0, len(string)):
        new = new + helper(string[counter], offset)
    return new

print(caesar("ARCDE",3))

def compare(a,b):
    if len(a) == len(b) == 0:
        return "Equal"
    elif len(a)==len(b):
        for checker in range(0, len(a)):
            if a[checker] == b[checker]:
                continue
            elif a[checker] < b[checker]:
                return "Smaller"
            elif a[checker] > b[checker]:
                return "Larger"
        return "Equal"
    elif len(a) < len(b):
        for checker in range(0, len(a)):
            if a[checker] < b[checker]:
                return "Smaller"
            elif a[checker] > b[checker]:
                return "Larger"
            elif a[checker] == b[checker]:
                return "Smaller"
    
    elif len(a) > len(b):
        for checker in range(0, len(b)):
            if a[checker] < b[checker]:
                return "Smaller"
            elif a[checker] > b[checker]:
                return "Larger"
            elif a[checker] == b[checker]:
                return "Larger"

print(compare([1,3],[1,3]))

#11. Bundling information
class Egg:
    """Egg low and high range of mass
       and category name.
    
       Attributes:
       low: int > 0, lowest mass in grams
       high: int > 0, highest mass in grams
       name: nonempty string, category
    """
    
    def __init__(self, low, high, name):
        self.low = low
        self.high = high
        self.name = name
    
    def __str__(self):
        return str(self(low))
        
class Egg:
    """Egg low and high range of mass
       and category name.
    
       Attributes:
       low: int > 0, lowest mass in grams
       high: int > 0, highest mass in grams
       name: nonempty string, category
    """
    
    def __init__(self, low, high, name):
        self.low = low
        self.high = high
        self.name = name
    
    def __str__(self):
        return str(self(low))
    
    def is_size(self, num):
        if self.low <= num <= self.high:
            return True
        else:
            return False
        

class Circle:
    """Circle radius, x and y coordinates, colour

       Public methods:
       __init__: initializes a new object
    
       Attributes:
       radius: int or float >= 0; circle radius
       x: int >= 0; x-coordinate of centre
       y: int >= 0; y-coordinate of centre
       colour: string; colour of the circle
    """

    def __init__(self, radius, x, y, colour):
        """Creates new circle
        """

        self.radius = radius
        self.x = x
        self.y = y
        self.colour = colour

    def __str__(self):
        """Prints object
        """

        return self.colour + " circle of radius " + \
            str(self.radius) + " centred at (" + \
            str(self.x) + "," + str(self.y) + ")"

    def area(self):
        """Determines area.
        """
        return math.pi * self.radius ** 2
    
    def aligned(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

circ_1 = Circle(1,2,3,"a")
circ_2 = Circle(2,2,3,"b")
print(circ_1.aligned(circ_2))
        
class Circle:
    """Circle radius, x and y coordinates, colour

       Public methods:
       __init__: initializes a new object
    
       Attributes:
       radius: int or float >= 0; circle radius
       x: int >= 0; x-coordinate of centre
       y: int >= 0; y-coordinate of centre
       colour: string; colour of the circle
    """

    def __init__(self, radius, x, y, colour):
        """Creates new circle
        """

        self.radius = radius
        self.x = x
        self.y = y
        self.colour = colour

    def __str__(self):
        """Prints object
        """

        return self.colour + " circle of radius " + \
            str(self.radius) + " centred at (" + \
            str(self.x) + "," + str(self.y) + ")"

    def area(self):
        """Determines area.
        """
        return math.pi * self.radius ** 2
    
    def aligned(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def bigger(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

circ_1 = Circle(2,2,3,"a")
circ_2 = Circle(1,2,3,"b")
print(circ_1.aligned(circ_2))
print(circ_1.bigger(circ_2))

class Circle:
    """Circle radius, x and y coordinates, colour

       Public methods:
       __init__: initializes a new object
    
       Attributes:
       radius: int or float >= 0; circle radius
       x: int >= 0; x-coordinate of centre
       y: int >= 0; y-coordinate of centre
       colour: string; colour of the circle
    """

    def __init__(self, radius, x, y, colour):
        """Creates new circle
        """

        self.radius = radius
        self.x = x
        self.y = y
        self.colour = colour

    def __str__(self):
        """Prints object
        """

        return self.colour + " circle of radius " + \
            str(self.radius) + " centred at (" + \
            str(self.x) + "," + str(self.y) + ")"

    def area(self):
        """Determines area.
        """
        return math.pi * self.radius ** 2
    
    def aligned(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def bigger(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False
    
    def is_colour(self, col):
        if self.colour == col:
            return True
        else:
            return False

circ_1 = Circle(2,2,3,"a")
circ_2 = Circle(1,2,3,"b")
print(circ_1.aligned(circ_2))
print(circ_1.bigger(circ_2))
col = "a"
print(circ_1.is_colour(col))

class Time:
    """Time stored as hour and minutes

       Methods:
       __init__: initializes a new object
       __str__: prints an object
       earlier_time: returns earlier time

       Attributes:
       hour: int, 0 <= value < 24
       minute: int, 0 <= value < 60
    """

    def __init__(self, hour, minute):
        """Initializes a new object.

           Preconditions:
           hour: int, 0 <= value < 24
           minute: int, 0 <= value < 60

           Parameters:
           hour: hour in time
           minute: minutes in time

           Side effect: attributes set with values
        """
        self.hour = hour
        self.minute = minute
 
    def __str__(self):
        """Prints time.

           Side effect: prints 
        """

        if self.minute < 10:
            min_word = "0" + str(self.minute)
        else:
            min_word = str(self.minute)
        return str(self.hour) + ":" + \
            min_word

    def earlier_time(self, other):
        """Determines earlier of two Times.

           Preconditions:
           other: Time object

           Parameters:
           other: Time compared to self

           Returns: earlier of two times, 
           or other if equal 
        """

        if self.hour < other.hour:
            return self
        elif other.hour < self.hour:
            return other
        elif self.minute < other.minute:
            return self
        else:
            return other
    
    def safe(self):
        if type(self.hour) == type(1) and type(self.minute) == type(1):
            if 0 <= self.hour < 24:
                if 0 <= self.minute < 60:
                    return "Safe"
                else:
                    return "Minute out of range"
            else:
                return "Hour out of range"
        else:
            return "Incorrect type"

    def elapsed(self, other):
        total_minute_1 = self.hour * 60 + self.minute
        total_minute_2 = other.hour * 60 + other.minute
        return total_minute_2 - total_minute_1

    def overlap(self, b, c):
        if (self.hour == b.hour and self.minute == b.minute) \
        or (self.hour == c.hour and self.minute == c.minute) \
        or (self.elapsed(b) < 0 and self.elapsed(c) > 0):
            return True
        else:
            return False
        
#12. Structuring Data
def number_pixels(list_string, colour):
    count = 0
    for item in list_string:
        for each in item:
            if colour == each:
                count = count + 1
    return count

class Meal:
    """Meal name, cost, and list of allergens

       Public methods:
       __init__: initializes a new object

       Attributes:
       name: non-empty string; meal name
       cost: int >= 0; cost of meal
       allergens: list of strings; allergens
    """
    
    def __init__(self, name, cost, allergens):
        self.name = name
        self.cost = cost
        self.allergens = allergens
    
    def contains(self, eggs):
        if eggs in self.allergens:
            return True
        else:
            return False

dinner = Meal("dinner", 5, "eggs")
print(dinner.contains("eggs"))

def bound_chars(string,bound):
    string = tuple(string)
    count = {}
    for item in string:
        if item in count.keys():
            count[item] = count[item] + 1
        else:
            count[item] = 1
    
    if len(count) <= bound:
        return True
    return False

print(bound_chars("aaaa",4))
print(len({'r': 1, 'n': 1, 'o': 2, 'a': 1, 'c': 1}))



def shuffle(one, two):
    result = []
    for item, adjust in zip (one, two):
        result = result + [item] + [adjust]
    return result

def code(string, dictionary):
    new = ""
    for char in string:
        if char in dictionary.keys():
            new = new + dictionary[char]
        else:
            new = new + char
    return new

#12. Recursion
def has_digit(string):
    if len(string) == 0:
        return False
    else:
        return string[0].isdigit() or has_digit(string[1:])
        
def is_sorted(seq):
    if 0 <= len(seq) <= 1:
        return True
    else:
        return (seq[0] < seq[1]) and (is_sorted(seq[1:]))
    
    def all_equal(seq):
    if 0 <= len(seq) <= 1:
        return True
    else:
        return seq[0] == seq[1] and all_equal(seq[1:])
    
def is_multiple(number, factor):
    return number % factor == 0

def divides_all(seq, factor):
    if len(seq) == 0:
        return True
    else:
        return is_multiple(seq[0], factor) and divides_all(seq[1:], factor)
    
def contains(seq, item):
    if len(seq) == 0:
        return False
    else:
        return seq[0] == item or contains(seq[1:], item)
    
def reverse(seq):
    if len(seq) == 0 or len(seq) == 1:
        return seq
    else:
        return [seq[-1]] + reverse(seq[:-1])

print(reverse([1,2,3]))

import math
def multisplit(total, split):
    return math.ceil(math.log(total) / math.log(split))
        



        


    


            
    

        
        
        
    
        