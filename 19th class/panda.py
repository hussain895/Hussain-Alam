import pandas as pd

data = [10,20,30,40,50]
my_series = pd.Series(data)
print(my_series)

print("\n")
data = [10,23,'Hussain','Alam']
my_series1 = pd.Series(data)
print(my_series1)

print('\n')
data1 = [10,20,30,'Hussain']
my_series2 =pd.Series(data1 , index = ['U','W','Y','Z'])
print(my_series2)

print('\n')
grade = {'Maths':85 , 'Science':90 , 'English':78 , 'Urdu':88}
my_series3 = pd.Series(grade)
print(my_series3)

print('\n')
Frames = {'City':['Karachi','Lahore','Islamabad','Quetta'],
         'Population':[3370000 , 1100000 , 500000 , 200000],
         'Province':['Sindh' , 'Punjab' , 'Capital' , 'Balochistan']}
my_dataframe = pd.DataFrame(Frames)
print(my_dataframe)

print('\n')
DF1 = pd.DataFrame(Frames)
DF1.iloc[1]
print(DF1.iloc[1])
print(DF1.index)
print(DF1.index.values)

print('\n')
frame = [['Pakistan' , 'India' , 'China','USA','Turkey'],
         ['Islamabad' , 'New Delhi' , 'Beijing' , 'Washington DC' , 'Ankara'],
         ['220 Million' , '1.4 Billion' , '1.4 Billion' , '330 Million' , '80 Million']]
my_dataframe1 = pd.DataFrame(frame , index = ['Country' , 'Capital' , 'Population'])
print(my_dataframe1)

print('\n')
frame1 = [['Pakistan','Islamabad',220000000],
          ['India','New Delhi',1400000000],
          ['China','Beijing',1400000000],
          ['USA','Washington DC',330000000],
          ['Turkey','Ankara',80000000]]
my_dataframe2 = pd.DataFrame(frame1 , columns = ['Country' , 'Capital' , 'Population'])
print(my_dataframe2)

# df = pd.DataFrame(Frames)
# df.to_csv('city.csv')
# print("DataFrame saved to 'city.csv'")

print('\n')
n = [10,20,30,40,50]
my_series4 = pd.Series(n, index = ['A' , 'B' , 'C' , 'D' , 'E'])
print(my_series4)
# renaming index
my_series4.index = ['a' , 'b' , 'c' , 'd' , 'e']
print("\nAfter renaming index:")
print(my_series4)

print('\n')
DF = pd.DataFrame(n , index=pd.RangeIndex(1,6) , columns=['Numbers'])
print(DF)

print("\n")
DF2 = {'City':['Karachi','New York','Istanbul','Mumbai','Beijing','Osaka','Dhaka'],
       'Country':['Pakistan','USA','Turkey','India','China','Japan','Bangladesh'],
       'Places to Visit':['Clifton','Statue of Liberty','Hagia Sophia','Gateway of India','Great Wall','Osaka Castle','Cox\'s Bazar']}
my_dataframe3 = pd.DataFrame(DF2)
print(my_dataframe3.head(3))
print("\n")
print(my_dataframe3.head())

print("\n")
print(my_dataframe3.tail(2))
print("\n")
print(my_dataframe3.tail())

print("\n")
address = ['South City , Karachi' , 'Brooklyn , New York' , 'Fatih , Istanbul' , 'South Mumbai , Mumbai' ,
           'Haidian , Beijing' , 'Kita , Osaka' , 'Gulshan , Dhaka']
my_dataframe3['Address'] = address
print(my_dataframe3)
print(my_dataframe3.info())

print("\n")
my_dataframe3.loc[len(my_dataframe3.index)] = ['Sydney','Australia','Opera House','Sydney CBD , Sydney']
print(my_dataframe3) 

print("\n")
my_dataframe3.drop('Address' , axis=1 , inplace=True)
print(my_dataframe3)

print("\n")
my_dataframe3.drop(index=6 , inplace=True)
print(my_dataframe3)

print("\n")
print(my_dataframe3.duplicated())

import matplotlib.pyplot as plt

car = ['BMW' , 'Audi' , 'Toyota' , 'Honda' , 'Ford']
sales = [50 , 40 , 70 , 60 , 30]

data = {'Car':car, 'Sales':sales}
df = pd.DataFrame(data)
df.plot(kind='line' , x='Car' , y='Sales' , color=['lightgreen' , 'magenta' , 'yellow' , 'lightblue' , 'lightcoral'])
plt.xlabel('Car Brands')
plt.ylabel('Number of Sales')
plt.title('Car Sales Data')
plt.tight_layout()
plt.show()   
df.plot(kind='bar' , x='Car' , y='Sales' , color=['cyan' , 'magenta' , 'yellow' , 'lightblue' , 'orange'])
plt.xlabel('Car Brands')
plt.ylabel('Number of Sales')
plt.title('Car Sales Data')
plt.tight_layout()
plt.show()
df.plot(kind='pie' , y='Sales' , labels=df['Car'] , autopct='%1.1f%%', startangle=180, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink'])
plt.title('Car Sales Distribution')
plt.tight_layout()
plt.show()      
df.plot(kind='scatter' , x='Car' , y='Sales' , color=['r' , 'g' , 'y' , 'c' , 'm'])
plt.xlabel('Car Brands')
plt.ylabel('Number of Sales')
plt.title('Car Sales Data')
plt.tight_layout()
plt.show()

# combined all plots in one figure
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
df.plot(kind='line' , x='Car' , y='Sales' , color=['lightgreen','lightcoral','lightblue','lightskyblue','lightpink'] , ax=axs[0, 0])
axs[0, 0].set_title('Line Plot')
df.plot(kind='bar' , x='Car' , y='Sales' , color=['cyan','magenta','yellow','lightblue','orange'] , ax=axs[0, 1])
axs[0, 1].set_title('Bar Plot')
df.plot(kind='pie' , y='Sales' , labels=df['Car'] , autopct='%1.1f%%', startangle=120, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink'], ax=axs[1, 0])
axs[1, 0].set_title('Pie Chart')
df.plot(kind='scatter' , x='Car' , y='Sales' , color=['r' , 'g' , 'y' , 'c' , 'm'] , ax=axs[1, 1])
axs[1, 1].set_title('Scatter Plot')
plt.tight_layout()
plt.show()