import numpy as np

# #creating sequence of numbers in numpy
# a = np.arange(10)
# print(a)
# #creating sequence of numbers with step size
# b = np.arange(0, 20, 2)
# print(b)

# #creating sequence of numbers with linspace
# c = np.linspace(0, 1, 5)    
# print(c)

# #creating sequence of numbers with logspace
# d = np.logspace(0, 2, 5)    
# print(d)

# #creating sequence of numbers with geomspace    
# e = np.geomspace(1, 100, 5)
# print(e)

# #creating sequence of numbers with arange and reshape
# f = np.arange(12).reshape(3, 4)
# print(f)

# #creating identity matrix
# c=np.eye(4)
# print(c)

# #creating diagonal matrix
# d=np.diag([1,2,3,4])
# print(d)

# #creating arrays from python lists
# a=np.array([1,2,3,4])
# print(a)

# #creating arrays from python tuples
# b=np.array((5,6,7,8))     
# print(b)

# #creating arrays from python lists of lists
# c=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(c)

# #creating arrays from python tuples of tuples
# d=np.array(((10,11,12),(13,14,15),(16,17,18)))
# print(d)

# #array with default values
# q=np.zeros((2,3))
# w=np.zeros((2), dtype=int)
# print(q)
# print(w)

# #full (shape,value
# e=np.full((2,3), 8 , dtype=float)
# print(e)

# #array properties and calculations
# a=np.array([[1,2,3]
#             ,[4,5,6]
#             ,[7,8,9]
#             ,[10,44,43]])
# print(a.shape)
# print(a.size)

#ndim - know array type of array
# a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(a.ndim)

# #dtype - know data type of array
# q=np.array([10,85,97.2,78])
# print(q.dtype)

# #astype - change data type of array
# e=np.array([54,98,63])
# t=e.astype(float)
# print(t)

# e1=np.array([54,98.68,63])
# t1=e1.astype(int)
# print(t1)

#mathematical operations on arrays
# y=np.array([52,90,70,60])
# print(y+50)
# print(y-50)
# print(y*2)
# print(y/5)
# print(y%5)  #remainder
# print(y//10) #floor division
# print(y**2) #exponentiation
# print(y**0.5) #square root
# print(np.sin(y)) #sine
# print(np.cos(y)) #cosine    
# print(np.tan(y)) #tangent
# print(np.log(y)) #logarithm
# print(np.exp(y)) #exponential
# print(np.sqrt(y)) #square root

#AGGERATION FUNCTIONS
# y=np.array([52,90,70,60])
# print(np.sum(y)) #sum of all elements
# print(np.mean(y)) #mean of all elements
# print(np.median(y)) #median of all elements
# print(np.min(y)) #minimum element
# print(np.max(y)) #maximum element       
# print(np.std(y)) #standard deviation
# print(np.var(y)) #variance


# #indexing and slicing
# q=np.array([60,80,60,70,90,20])
# print(q[0]) #first element
# print(q[1]) #second element 
# print(q[-1]) #last element

# #slicing
# print(q[1:4]) #slicing from index 1 to 3
# print(q[:3]) #slicing from start to index 2
# print(q[3:]) #slicing from index 3 to end
# print(q[::2]) #slicing with step size 2
# print(q[::-1])#licing with step size -2 (reverse order)

# #reshaping and transposing
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(a.reshape(1,9)) #reshaping to 1 row and 9 columns
# print(a.reshape(9,1)) #reshaping to 9 rows and 1
# # print(a.T) #transposing the array
# print(a.ravel()) #flattening the array
# print(a.flatten()) #flattening the array

# #fancy indexing
# w=np.array([10,95,85,75,65,35,12])
# print(w[w>20])
# print(w[w%2==0 ]) #even numbers
# print(w[w%2!=0 ]) #odd numbers
# print(w[[0,5,3]])

#insert method
# g=np.array([60,80,90,40,50,60,70,80])
# new_g=np.insert(g,5,80)
# print(new_g)

# #two dimensional array
# l=np.array([[1,5],[2,9]])
# new_l=np.insert(l,2,[65,87],axis=0) #inserting row at index 2
# print(new_l)


#append method
