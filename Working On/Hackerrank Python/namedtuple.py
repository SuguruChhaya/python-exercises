from collections import namedtuple
'''
#*Named tuples are a dictionary-like object. I think it is like creating a class
#*The first argument is basically ignored. I think it corresponds to "self" in classes.
#*I have to store the attributes either in lists or space-separated strings. (that counts as multiple arguments.)

Student = namedtuple("Student", "Name Grade")
print(Student)

Suguru = Student("Suguru", 10)

print(Suguru.Name)
print(Suguru[1])
print(getattr(Suguru, "Name"))

#More info on https://www.geeksforgeeks.org/namedtuple-in-python/#:~:text=Python%20supports%20a%20type%20of%20container%20like%20dictionaries,keys%20that%20are%20hashed%20to%20a%20particular%20value.



#*Another interesting thing about print
#!By default, end=\n, meaning the next print will be on the next line, but I can modify that.
print("Student name: ", end="")
print(Suguru.Name)
'''

#*.split() can split spaces of more than len1
num = int(input())
first, second, third, fourth = input().split()
Student = namedtuple('Student', [first, second, third, fourth])
total = 0
student = 0
average = 0
for i in range(num):
    first_, second_, third_, fourth_ = input().split()
    a = Student(first_, second_, third_, fourth_)
    total += int(a.MARKS)
    student += 1

print(round(total / student, 2))