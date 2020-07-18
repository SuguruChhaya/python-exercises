#Initialization basic templte. self is referring to the object itself and self.radius is the attribute(radius) of the object(self)

class circle:
    def __init__(self, radius, xcoord, ycoord, colour):
        self.radius = radius
        self.x = xcoord
        self.y = ycoord
        self.colour = colour
        
#Printing function       
    def __str__(self):
        return self.colour + " yeet " + str(self.x)
    
eye = circle(1,2,3,"blue")
bad = circle(2,3,5.6,"yellow")
print(eye.radius)
eye.radius = 5.39384 #mutable
print(eye.radius)
print(bad)
#To check whether object is in that class
print(isinstance(bad, circle))
#To check whether object has an attribute of that given name
print(hasattr(eye, "ycoord"))


#Storing information in a grid
"""1 is black and 0 is white
"""
image = [[1,1,0],[0,0,1]]
print(image[0][1])

#Example of nesting and calling
def flatten(list_list):
    flat = []
    for each in list_list:
        for item in each:
            for yeet in item:
                flat.append(yeet)
    return flat
    
print(flatten(["1","2",["3",["4","5"]]]))

#Tuples are immutable sequences
(6,2,3,4)

"""Rules
1. Tuples with len(1) e.g. (1) is not a tuple but (1,) is a tuple
2.But a parenthasis around a len() is a tuple, () is a tuple
3. Tuple len: len((1,2,3))
Index: (1,2,3)[0]
concatenation: (1,2) + (3,)
repeated 2 * (1,2)
slice : (1,2,3)[1:-1] = (2,)
(1,2) < (2,3) is True
4. print(tuple(1,2,3)) wouldn't work because you can only touple a sequence
5. print(tuple("12")) divides stringinto (1,2)
print(min( and print(max works with tuples
to count how many times element appears: tup.count()
tupe.index(7) gives the index of the first appearance of 7 in tuple
2 in touple checks for membership
list(tup) gives a list [1....]
sorted(tup) gives sorted as a list
6. you cannot remove or append in a tuple
7. when you index for a tuple, an element comes out; no longer a tuple
"""

"""An associative array consists of keys and value and is also called a dictionary
Keys, values are mutable in dictionaries
to make a dictionary: curly brackets
unicode = {"a":97, "b":100, "c":95}
extract keys as a list: print(unicode.keys())
to extract a key, value pair as a list of tuples: print(unicode.items())
membership: print("a"" in unicode)
"""

#Example code for finding a key in a dictionary:
def is_in(dictionary, target):
    for key, value in dictionary.items():
        if key == target:
            return value
    return "Not Found"

print(is_in({"a":76,"b":3}, "c"))
    
    
#Good example of using dictionaries
def max_colour(seq):
    counts={}
    for item in seq:
        if item in counts.keys():
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    
    most = 0
    best = "Empty"
    for colour, num in counts.items():
        if num > most:
            most = num
            best = colour
    return best

print(max_colour(["red", "blue", "red"]))

"""In this code, we are looking thorugh the list for strings (colours) we have already encountered before.
We then make the dictionary, "counts" so that the key is the string and the value is the number of times we
seen that string so far. "item" is the individual colours in the list. "counts[items]" shows the key value
in the dictionary, which is the # of times we have seen the colour before. we then update the counts[item]
if we see it again in the list. Then we scan through the dictionary to find tha colour with most counts[item]
value
"""

#An example of looping through a pair of lists
def change(salaries, boosters):
    result = []
    for item, adjust in zip(salaries, boosters):
        result = result + [item * adjust]
    return result

print(change([2,3],[4,5]))

"""In this code, we use zip to join salaries and boosters. The "item" refers to the two elements in the first
list (2 and 3) and "adjust" refers to the two items in the second list (4 and 5) which they each get multiplied
with each other.
"""







