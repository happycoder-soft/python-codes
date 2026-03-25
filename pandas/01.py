import pandas as pd
import openpyxl

# Create a sample DataFrame using a dictionary
data = {
    'name':['happy','sachin','shivam','aditya','abhishek'],
    'age':[20,26,24,21,22],
    'city':['Motihari','Darbhanga','Darbhanga','Hajipur','Khagaria']
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














