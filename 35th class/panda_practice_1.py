import pandas as pd

df = pd.DataFrame({
    'Name' : ['Ali' , 'Sara' , 'John'],
    'Age' : [28 , 30 , 26],
    'Salary' : [50000 , 55000 , 60000]
})

print(df[['Name' , 'Salary']])
print()
print("Sara's Salary : " , df.loc[1 , 'Salary'])
print()
print("Employess With Salary Greater Than 55000 : ")
print()
print(df[df['Salary'] > 55000])
print()
df['Department'] = ['HR' , 'Finance' , 'IT']
print(df)