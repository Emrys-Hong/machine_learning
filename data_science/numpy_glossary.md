# material is from:
'''https://docs.scipy.org/doc/numpy-dev/user/quickstart.html'''
'''https://www.tutorialspoint.com/numpy/numpy_linear_algebra.htm'''
## this create a numpy array, reshape and resize
```np.array([],dtype=np.float32) 
np.arange(start,stop,step).reshape(n1,n0) # create a numpy array
np.linspace(start,stop,num_points).resize(n1,n0) # resize a shaped array
```
## + - * / are all applicable for numpy array, and they will operate on each elements one by one.
# array attributes
```a = np.array([1,1,1])
a.itemsize # how much space one datatype occupy # output 4
a.size # how many items
a.shape # shape
a.ndim # what is the dimension
a.dtype # data type
```

np.zeros( (3,4) )
np.ones( (3,4) )
# flatten
```a.ravel() # same as flatten()
a.flatten()
```
# min max
```a.min()
a.max()
a.sum(axis=1) # sum all the row together)
a.cumsum() # the output have the same dimension as the a
# See also
'''all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, 
corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, 
mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose,
var, vdot, vectorize, where'''
```
# other operations
```a.T #transpose
a.dot(b)
a*b
np.dot(a,b)
sin(a)
np.sqrt(a) # sqrt
np.std(a) # standard diviation
# slicing
a[1:2,3]

for i in a.flat:
  print(i)
```
# combine arrays
```np.hstack([a,b]) # stack horizontally
np.vstack([a,b]) # stack vertically
np.hsplit(a,3) # split horizontally
np.vsplit(a,3) # split horizontally
>>> np.r_[1:4,0,4] # the same for np.c_
array([1, 2, 3, 0, 4])
```

# select particular entry
```a = np.arange(12).reshape(3,4)
b = a > 4
print(b)
>> array([[False,False,Flase,False],[False,True,True......])
a[b] = 100
print(a)
# array([0,1,2,3],[4,100,100,100],...])
>>> a = np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> i = np.array( [ [0,1],                        # indices for the first dim of a
...                 [1,2] ] )
>>> j = np.array( [ [2,1],                        # indices for the second dim
...                 [3,3] ] )
>>>
>>> a[i,j]                                     # i and j must have equal shape
array([[ 2,  5],
       [ 7, 11]])
# find all the index of entries equal to a particular number
import numpy as np
values = np.array([1,2,3,1,2,4,5,6,3,2,1])
searchval = 3
ii = np.where(values == searchval)[0]

returns:

ii ==>array([2, 8])
```
# nditer
```for x in np.nditer(a,order='C'): # this is printing in row order
    print(x)
    
# 0,1,2,3,4,5....

for x in np.nditer(a, order='F'): # printing in column order
    print(x)
    
# 0,4,8,1,5,9

for x in np.nditer(a, order='F', flags=['external_loop']):
    print(x)
# [0,4,8]
#[1,5,9]
.....

for x in np.nditer(a, order='F', flags=['readwrite']):
    x[...] = x**2
# change all the enties to square

for x,y in np.nditer([a,b]):
    print(x,y)
 # x and y must have the same colum dimension

>>> c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
...                 [ 10, 12, 13]],
...                [[100,101,102],
...                 [110,112,113]]])
>>> c.shape
(2, 2, 3)
>>> c[1,...]                                   # same as c[1,:,:] or c[1]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[...,2]                                   # same as c[:,:,2]
array([[  2,  13],
       [102, 113]])
```
# shallow copy
```>>> c = a.view()
>>> c is a
False
>>> c.base is a                        # c is a view of the data owned by a
True
>>> c.flags.owndata
False
>>>
>>> c.shape = 2,6                      # a's shape doesn't change
>>> a.shape
(3, 4)
>>> c[0,4] = 1234                      # a's data changes
>>> a
array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])

# deepcopy
>>> d = a.copy()                          # a new array object with new data is created
>>> d is a
False
>>> d.base is a                           # d doesn't share anything with a
False
>>> d[0,0] = 9999
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```

# get index of entry
```
ind = data.argmax(axis=0)  

# all and any
np.all(data_max == data.max(axis=0))
>>> True
```
# ix function can create difference shapes
```>>> a = np.array([2,3,4,5])
>>> b = np.array([8,5,4])
>>> c = np.array([5,4,6,8,3])
>>> ax,bx,cx = np.ix_(a,b,c)
>>> ax
array([[[2]],
       [[3]],
       [[4]],
       [[5]]])
>>> bx
array([[[8],
        [5],
        [4]]])
>>> ax.shape, bx.shape, cx.shape
((4, 1, 1), (1, 3, 1), (1, 1, 5))
```
# linear algebra
```np.linalg.inv(a)
np.transpose(a)
np.eye(some number) # identity matrix interger stands for the size
np.trace(a)

x = np.array([[0, 2], [1, 1], [2, 0]]).T
np.cov(x)
array([[ 1., -1.],
       [-1.,  1.]])

a = np.array([[1.0, 2.0], [3.0, 4.0]])
y = np.array([[5.], [7.]])
>>> np.linalg.solve(a, y)
array([[-3.],
       [ 4.]])
np.linalg.eig(j)
(array([ 0.+1.j,  0.-1.j]), array([[ 0.70710678+0.j        ,  0.70710678-0.j        ],
       [ 0.00000000-0.70710678j,  0.00000000+0.70710678j]]))

 (n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
>>> plt.plot(.5*(bins[1:]+bins[:-1]), n)
>>> plt.show()
```
# random
```
v = np.random.normal(mu,sigma,10000)
```

# if you want to swap the rows
```arr = np.array([10, 20, 30, 40, 50])
idx = [1, 0, 3, 4, 2]
arr[idx]
array([20, 10, 40, 50, 30])
```
