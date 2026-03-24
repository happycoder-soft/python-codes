import pandas as pd
import openpyxl

# Create a sample DataFrame
data = {
    'name':['happy','sachin','shivam','aditya','abhishek'],
    'age':[20,26,24,21,22],
    'city':['Motihari','Darbhanga','Darbhanga','Hajipur','Khagaria']
    } 
df=pd.DataFrame(data)
print(df)
#save the DataFrame to an Excel file
df.to_excel('data.xlsx',index=True)


