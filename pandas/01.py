from hashlib import new

import pandas as pd
import openpyxl

# Create a sample DataFrame using a dictionary
data = {
    'name':['happy','sachin','shivam','aditya','abhishek'],
    'age':[20,26,24,24,22],
    'city':['Motihari','Darbhanga', 'Darbhanga','Hajipur','Khagaria'],
    'salary':[100000,60000,55000,45000,80000]
    } 

df=pd.DataFrame(data)
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

#grouping data
g=df.groupby('age')['salary'].sum() #age ke hisab se data ko group karte hai
print(g)
























