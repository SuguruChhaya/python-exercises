import numpy as np

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(2,6))
x3 = np.random.randint(10, size=(2,2,2, 3))
#!In numpy arrays, the commas are deleted in output
x4 = np.array([False,True,None])
#!When the number of items in each dimestion don't match,
#!Numpy just prints that the 2D part like (2,)
x5 = np.array([[0,1], [1,2,3], [1]])
print(x5.shape)

print(x4)
#!One dimensional numpy arrays return interesting things when the shape is printed
print(x4.shape)
print(x1.shape)
#print(x1)
#print(x2)
print(x3)
#*This returns the number of dimensions
print(x3.ndim)
#*Prints the dimesions, starting from the largest dimension
print(x3.shape)
#*Essentially prints the number of items (all the elements in shape multiples together)
print(x3.size)

#* Numpy recognizes the types of elements in the array
#The array can be all int, some str, etc
print(x3.dtype)
print(x4.dtype)

x6 = np.array([[12,  5,  2,  4],
       [ 7,  6,  8,  8],
       [ 1,  6,  7,  7]])

print(x6[:,0])

#* An interesting thing is that numpy arrays are mutable

x7 = [1,2,3]

x7_sub = x7[:2]
x7_sub[0] = 2
#* Original file is not mutated
print(x7_sub)
print(x7)

x8 = np.array(x7)

x8_sub = x8[:2]
x8_sub[0] = 2
#!in numpy, when you change the sliced one, it mutates to the original
print(x8_sub)
print(x8)

#!To make arrays unmutable, I have to use the copy() function
#*Can convert array types into different data type
x9 = np.array(["1", "2"], int)
print(x9.dtype)

#!This is what the reshape method does
x10 = np.arange(1,13)
print(x10.reshape(2,2,3))
x11 = x10[np.newaxis, :]
x12 = x11[np.newaxis, :]
#*The newaxis mrthod creates another dimension
#!You can do interesting slicing with it
x12 = x10[np.newaxis, :9:2]
print(x11)
print(x12)

ar1 = np.array([1,2,3])
ar2 = np.array([4,5,6])
ar3 = np.array([[1,2,3], [4,5,6]])
ar4 = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
#* This is the easiest way to concatenate
print(np.concatenate([ar1, ar2]))
print(np.concatenate([ar3, ar3]))
#* For the default way of concatenating without specifying axis, I need to put[] around the concatenation
#!If I concatenate two 2D arrays like this, I will get a 2D array


#*Concatenation

ar1 = np.array([1,2,3])
ar2 = np.array([4,5,6])
ar3 = np.array([[1,2,3], [4,5,6]])
ar4 = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(ar4.shape)
#* This is the easiest way to concatenate
#print(np.concatenate([ar1, ar2]))
#print(np.concatenate([ar3, ar3]))
#* For the default way of concatenating without specifying axis, I need to put[] around the concatenation
#!If I concatenate two 2D arrays like this, I will get a 2D array
#print(np.concatenate((ar4,ar4), axis=0))
#print(np.concatenate((ar4,ar4), axis=1))
#print(np.concatenate((ar4, ar4), axis=2))

ara = np.array([[['a','b'], ['c', 'd']], [['e', 'f'], ['g', 'h']]])

a = (np.concatenate((ara,ara), axis=0))
print(a.shape)
print(a)
b = (np.concatenate((ara, ara), axis=1))
print(b.shape)
print(b)
c = (np.concatenate((ara, ara), axis=2))
print(c.shape)
print(c)

#reference:https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html#Array-Concatenation-and-Splitting

