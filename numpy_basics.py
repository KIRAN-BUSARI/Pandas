import numpy as np

l = [1,2,3,4,5]
arr = np.array(l)
print(arr)
print(type(arr))

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)

print(arr.ndim)
print(arr1.ndim)

mat = np.matrix(l)
print(mat)

asarray = np.asanyarray(l)
print(asarray)

matrix_array = np.asarray(mat)
print(matrix_array) # There is no change for this line bcoz it is already present in one fo the form we can't change the existing form of matrix to array

b = np.copy(arr)
print("This is b ;",b)

arr[0] = 100 # This is a copying operation this and known as shallow copying operation
print("This is after assigning a value",arr)


foo = np.fromfunction(lambda i,j : i==j , (4,4))
print(foo)

foo1 = list(i*i for i in range(5))
print(foo1)

iterable = (i*i for i in range(5))
iterables = np.fromiter(iterable,int)
iterables1 = np.fromiter(iterable,float)

print(iterables)
print(iterables1)

fromstring = np.fromstring("12 11 13 14",sep=' ')
print(fromstring)

fromstring = np.fromstring("12,11,13,14",sep=',')
print(fromstring)

print(arr.size)
print(arr1.size)
print(foo.size)
print(fromstring.size)

print(arr.dtype)

print("Hello, " + "World!")