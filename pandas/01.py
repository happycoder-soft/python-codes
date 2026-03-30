from hashlib import new

import pandas as pd
import openpyxl

# # Create a sample DataFrame using a dictionary
# data = {
#     'name':['happy','sachin','shivam','aditya','abhishek'],
#     'age':[20,26,24,24,22],
#     'city':['Motihari','Darbhanga', 'Darbhanga','Hajipur','Khagaria'],
#     'salary':[100000,60000,55000,45000,80000]
#     } 

# df=pd.DataFrame(data)
# print(df)
# # #save the DataFrame to an Excel/csc/json file
# # df.to_excel('data.xlsx',index=True)   

# # read the 3 row of the dataframe
# print(df.head(3))
# #summary of the dataframe
# print(df.info())

#describe the dataframe
# print(df.describe())
# #select the name column
# print(df['name'])
# #select the name and age column
# print(df[['name','age']])

# #know the data shape
# print(df.shape  )
# print(df.columns)
# print(df.index)
# f=df[['name','city']]
# print('\n f with name and city')

# #conditional selection
# high=df[df['age']>=21]
# print('age with more than 21')
# print(high)
# # #multiple conditions
# high1=df[(df['age']>22) & (df['city']=='Darbhanga')]
# print('age with more than 22 and city is darbhanga')
# print(high1)


# #using loc and iloc
# print(df.loc[0]) #loc is used to select rows by label
# print(df.iloc[2]) #iloc is used to select rows by index

# #using or conditional selection with loc and iloc
# high2=df.loc[(df['age']>22) | (df['city']=='Darbhanga')]
# print('age with more than 22 or city is darbhanga') 
# print(high2)

# # #using isin() method to select rows with specific values
# high3=df[df['city'].isin(['Darbhanga','Hajipur'])]
# print('city is darbhanga or hajipur')
# print(high3)

# #adding method
# df['age']=df['age']+5
# print(df)
# df['locality']=df['city']+',bihar'
# print(df)

# #using insert method to add a new column
# df.insert(3,'country','India')
# print(df)
# df.insert(2,'gender','Male')
# print(df)

# # condition apply
# df["job_role"] = df["age"].apply(lambda x: "Employee" if x > 22 else "Student")
# print(df)

# df.to_excel('01.xlsx',index=False)
# print("DataFrame saved to 01.xlsx")

# #update the data
# df.loc[1,'age']=23
# print(df)

# #increase salary by 10%
# df['salary']=df['salary']*1.1
# print(df)

# #removing column
# df.drop(columns=['salary'], inplace=True)
# print(df)

# #detect missing values
# print(df.isnull())

# #handle missing values by filling with a specific value
# df['city'].fillna('Unknown', inplace=True)
# print(df)   

# #handle missing values by dropping(deleting) rows with missing values
# df.dropna(inplace=True)
# print(df)


# # #handle missing values by filling with mean value
# df['age'].fillna(df['age'].mean(), inplace=True)
# print(df)

# #interpolate missing values
# df['age']=df['age'].interpolate(method='linear')
# print(df)

# #time based interpolation
# df['age']=df['age'].interpolate(method='time')
# print(df)

#polynomial interpolation
# df = pd.DataFrame({
#     'x': [1, 2, 3, 4, 5,6,7,8,9],
#     'y': [1, 8, 27, None, 125, 216, 343, None, 729]
# })

# df['y'] = df['y'].interpolate(method='polynomial', order=3)#order 3 means(3 value ke bad none value hona chahiye) cubic interpolation or 2 means quadratic interpolation

# print(df)

# #resampling time series data
# date_rng = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
# df = pd.DataFrame(date_rng, columns=['date'])
# df['data'] = pd.Series(range(len(df)))
# print(df)


#forward fill

# df = pd.DataFrame({
#     'A': [10, None, None, 40, None]
# })

# new=df.fillna() #forward fill method se missing value ko pichle value se fill karte hai
# print(new)

# #backward fill
# df = pd.DataFrame({
#       'A': [10, None, None, 40, None]
# })
# new=df.fillna(method='bfill') #backward fill method se missing value ko agle value se fill karte hai
# print(new)

# #sorting data
# w=df.sort_values(by='age', ascending=True) #age ke hisab se data ko descending order me sort karte hai
# print(w)
#ascending ko true or false karenge to ascending or descending order me sort karte hai

# #multiple column ke hisab se sort karte hai
# r=df.sort_values(by=['age','salary','city'],ascending=[True,True,True]) #age ke hisab se ascending order me sort karte hai aur salary ke hisab se descending order me sort karte hai
# print(r)

# #grouping data
# g=df.groupby('age')['salary'].sum().reset_index() #salary ke hisab se data ko group karte hai
# print(g)

# #multiple grouping
# g1=df.groupby([ 'age'])['salary'].sum().reset_index() #age aur name ke hisab se data ko group karte hai
# print(g1)

#aggregation functions
#merging & joining dataframes

# cus=pd.DataFrame({
#     'customer_id':[5,6,8,9],
#     'Name':['Happy','aditya','abhishek','sachin']
# })
# order=pd.DataFrame({
#     'customer_id':[1,8,5,6],
#     'order amount':[2000,3000,4000,5000]
# })

# m=pd.merge(cus,order,on='customer_id', how='right') #inner join se dono dataframe ke common value ko merge karte hai
# print(m)
    

# m=pd.merge(cus,order,on='customer_id', how='inner') #inner join se dono dataframe ke common value ko merge karte hai
# print(m)
    

# m=pd.merge(cus,order,on='customer_id', how='left') #inner join se dono dataframe ke common value ko merge karte hai
# print(m)
    

# m=pd.merge(cus,order,on='customer_id', how='outer') #inner join se dono dataframe ke common value ko merge karte hai
# print(m)
    
# #concatenating dataframes
# df1=pd.DataFrame({
#     'A':['happy','sachin','shivam'],
#     'B':[4,5,6]
# })
# df2=pd.DataFrame({
#     'A':['alice','bob','charlie'],
#     'B':[10,11,12]
# })
# c=pd.concat([df1,df2], axis=1) #axis 1 se columns ke hisab se concatenate karte hai
# c=pd.concat([df1,df2], axis=0) #axis 0 se rows ke hisab se concatenate karte hai

# print(c)

# d=pd.merge(df1,df2,on='B',how='inner',suffixes=('_left','_right')) #indicator=True se merge ke baad ek new column add hota hai jisme merge ke type ke baare me information hoti hai
# print(d)

#concatination with ignore index
df1=pd.DataFrame({
    'customer_id':[1,2,3],
    'Name':['happy','abishek','sachin']
})
df2=pd.DataFrame({
    'customer_id':[4,5,6],
    'name':['alice','bob','charlie']
})
con=pd.concat([df1,df2],axis=0,ignore_index=False) #ignore index se concatenate ke baad index ko reset karte hai
print(con)


















