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
# q=np.array([80,90,78,95,14,25,95])
# new_q=np.append(q,[95,78])
# print(new_q)

#concatenate method
# c=np.array([[5,9,6],[9,8,7]])
# d=np.array([[5,9,6],[6,4,1]])
# new_c=np.concatenate((c,d))
# print(new_c)

# #delete method
# d=np.array([80,9,7,80,90,60,40,50])
# new_d=np.delete(d,5) #deleting element at index 5
# print(new_d)

# #two dimensional array
# p=np.array([[6,8],[8,3]])
# new_p=np.delete(p,1,axis=1) #deleting column at index 1 
# print(new_p)

#unique method
# q=np.array([80,90,78,95,14,25,95])
# unique_q=np.unique(q)
# print(unique_q)

# #stacking arrays
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# d=np.vstack((a,b)) #vertical stacking
# print(d)
# g=np.hstack((a,b)) #horizontal stacking
# print(g)


#splite method
# f=np.array([10,20,30,40,50,60,70,80,90,96,63,69])
# split_f=np.split(f,4) #splitting into 3 equal parts
# split_d=np.split(f,6) #splitting into 2 equal parts
# print(split_f)
# print(split_d)

# #brodcasting & vectorization
# v=np.array([40,80,9,60,80,70,60,20])
# discount=20
# final=v-(discount*v/100) #applying discount to each element
# print(final)

# su=v-20 #subtracting 20 from each element
# ad=v+200 #adding 200 to each element
# mul=v*2 #multiplying each element by 2  
# div=v/2 #dividing each element by 2 
# print(su)
# print(ad)
# print(mul)
# print(div)

# q=np.array([10,20,30])
# # w=np.array([40,90,80])
# # print(q+w) #element-wise addition
# a=np.array([50])
# print(q+a) #broadcasting a to q
# e=np.array([1,8,9])
# t=np.array([7,8,9])
# print(e*t) #element-wise multiplication

# # handling missing data
# p=np.array([10,50,80,60,np.nan,50,60,np.nan,70])
# print(np.isnan(p))
# clean=np.nan_to_num(p,nan=40) #replacing nan with 40
# print(clean)
# p2=np.array([10,50,80,60,-np.inf,50,60,np.inf,70])
# print(np.nan_to_num(p2,posinf=100,neginf=-100)) #replacing inf with 100 and -inf with -100

# # #masking
# mask=np.isnan(p)
# print(p[mask])


# #random modules
# r=np.random.rand(1,5) #random numbers between 0 and 1
# print(r)
# q=np.random.randint(5,50,3) #random integers between 5 and 50
# # print(q)
# r=np.random.normal(0,1,2) #random numbers from normal distribution with mean 0 and std 1
# print(r)
# e=np.random.choice([10,20,30,40,50],3) #randomly choosing 3 elements from the list
# # print(e)
# t=np.random.seed(100) #setting seed for reproducibility
# # print(np.random.rand(1,5)) #random numbers between 0 and 1 with
# o=np.random.rand(5,5) #random numbers between 0 and 1 with shape 5x5
# print(o)

