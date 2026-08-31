import numpy as np

## one dimensional array
arr = np.array([1,2,3, 4,5,6])


b  = np.arange(3, 10, 2)
c  = np.linspace(0, 100, 5, dtype=int)
d= np.zeros(20, dtype=int)
e  = np.ones(20, dtype=int)
rand_arr = np.random.rand(3)

# print(arr)
# print(b)
# print(c)
# print(d)
# print(e)
# print(rand_arr)

# two dimensional array

two_d = np.array([[1, 2, 3], [4,5,6]])

# Multidimensional array using reshape()
multi_dim_arr = np.reshape(arr,(3,2))

# print(two_d)


## Finding size, shape and dimension
arrs = np.array([1,2, 3, 4,5,6,7,8,9,10,11,12])
multi = np.reshape(arrs, (4,3))

# print(multi_dim_arr)
# print(multi.ndim)
# print(multi.shape)
# print(multi.size)


## Array math operations

arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 4, 5])

addition = arr1 + arr2
sub = arr2 - arr1
mul = 2 * arr1
mult = arr1 * arr2

# print(addition)
# print(sub)
# print(mul)
# print(mult)


# Indexing

a = ([1, 2, 3, 4, 5])
# print(a[2])
# print(a[0])

two_dim = np.array(([1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]))

# print(two_dim[2][1])


# stacking

newArr = arr[0:4]
# print(newArr)

sliced_arr = arr[::3]
# print(arr[:])
# print(sliced_arr)

sliced_arr_1 = two_dim[0:2]
# print(sliced_arr_1)

sliced_two_dim_cols = two_dim[:,2]
# print(sliced_two_dim_cols)


# 5 - Stacking 
a1 = np.array([[1,1], 
               [2,2]])
a2 = np.array([[3,3], [4, 4]])

vert_stack =np.vstack((a1,a2))
hor_stack =np.hstack((a1,a2))
print(vert_stack)
print(hor_stack)