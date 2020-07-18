import numpy

'''
list_1 = [1, [2, 3]]
list_2 = [4, [5, [6, 7]]]
print(list_1 + list_2)
#!This is normal concatenation of lists. You can't control many things.

# ?This is from hackerrank's concantenate question
# *Approach 1: (Simplest) store the first values and create a list for all the lines and concatenate it
import numpy as np
a, b, c = map(int, input().split())
arrA = np.array([input().split() for _ in range(a)], int)
print(arrA)
arrB = np.array([input().split() for _ in range(b)], int)
print(np.concatenate((arrA, arrB), axis=0))

simplar version:

import numpy
row1, row2, column = map(int, input().strip().split())

row1_list = []
row2_list = []
for a in range(row1):
    row1_list.append(list(map(int, input().strip().split())))

for b in range(row2):
    row2_list.append(list(map(int,input().strip().split())))

row1_numpy = numpy.array(row1_list)
row2_numpy = numpy.array(row2_list)

print(numpy.concatenate((row1_numpy, row2_numpy), axis=0))
'''
'''
#!Simpler version
import numpy
input_list = list(map(int, input().strip().split()))
print(input_list)
'''

# ?In numpy concatenate, all nested lists should have the same length
# ?The axis

# *Approach 2: don't use numpy concatenate
'''
import numpy
row1, row2, column = map(int, input().strip().split())

row_list = []

for a in range(row1 + row2):
    row_list.append(list(map(int, input().strip().split())))

print(numpy.array(row_list))
'''
