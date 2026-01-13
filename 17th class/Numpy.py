# import numpy as np
# # rank 1 array

# array = np.array([1,2,3])
# print(array)
# print("\n------------------------------------------------------------------------------\n")
# # rank 2 array

# arrray = np.array([[1,2,3],[2,3,4]])
# print(arrray)

# print("\n------------------------------------------------------------------------------\n")

# # Initail Array
# arr = np.array([
#     [2,5,6,7],
#     [-4,6,7,-8],
#     [5,6,8,9],
#     [4,8,5,3]])
# print("Initial Array")
# print(arr)

# print("\n------------------------------------------------------------------------------\n")


# # Printing a range of Array
# # With the use of slicing method

# sliced_arr = arr[:2, ::2]
# print("Array with first 2 rows and"
#       " alternate columns (o and 2 ):\n",sliced_arr)

# print("\n------------------------------------------------------------------------------\n")

# # Printing elements at
# # Specific Indices
# index_arr = arr[[1,1,0,3],
#                 [3,2,1,0]]
# print("\n Elements at indices (1,3),"
#     "(1,2),(0,1),(3,0):\n",index_arr)

# print("\n------------------------------------------------------------------------------\n")

# a = np.array([1,2,3,4])
# b = np.array([2,3,4,5])

# print(a)
# print(b)
# print(a+b)
# print(a+1)

# print("\n------------------------------------------------------------------------------\n")

# arrr = np.zeros(4)
# print(arrr)

# print("\n------------------------------------------------------------------------------\n")

# arra = np.ones(2)
# print(arra)

# print("\n------------------------------------------------------------------------------\n")

# lis = np.random.rand(5)
# print(lis)

# print("\n------------------------------------------------------------------------------\n")

# array1 = np.array([1,2,3,4.5],dtype='int32')

# print(array1 , array1.dtype)

# print("\n------------------------------------------------------------------------------\n")

# arr1 = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
# trans_arr = arr1.T
# sqrt = np.sqrt(arr1)
# print(trans_arr)
# print(sqrt)


# print("\n------------------------------------------------------------------------\n")

import numpy as np

# 10 rows, 7 columns, random temperatures between 25 and 50
temperature_random = 25 + (50 - 25) * np.random.randint(size=(10, 7))

print("Random Temperature Array (10x7):")
print(temperature_random)

# Average temperature
avg_temp = np.mean(temperature_random)
print("\nAverage Temperature:", avg_temp)

for i , avg in enumerate(avg_temp):
    print(f"city{i} : {avg}")

# print("\n------------------------------------------------------------------------\n")

# array4 = np.array([[1,2,3,4],[4,5,6,7]])
# np.save('/home/steampup-qbh/Desktop/Hussain Alam (XI)/Hussain-Alam/17th class/hussan.npy', array4)


# loadd_array=np.load('/home/steampup-qbh/Desktop/Hussain Alam (XI)/Hussain-Alam/17th class/hussan.npy')
# print(loadd_array)

# print("\n------------------------------------------------------------------------\n")

# array5 = np.array([[1,2,3],[3,4,5]])
# array6 = np.array([[5,5,6],[3,4,5]])

# np.savez('/home/steampup-qbh/Desktop/Hussain Alam (XI)/Hussain-Alam/17th class/File.npy.npz',file1 = array5 , file2 = array6)

# load = np.load('/home/steampup-qbh/Desktop/Hussain Alam (XI)/Hussain-Alam/17th class/File.npy.npz') 
# print(load)

# print("\n------------------------------------------------------------------------\n")

# np.seterr(divide='raise')
# result = np.divide(array5,array6)
# print(result)


# calcl = np.exp(1000)
# print(calcl)

# import matplotlib.pyplot as plt

# car =  np.array(['TESLA','MEHRAN','CULTAS','COROLLA','AUDI','BMW'])
# weight = np.array([1000,1597,3000,1789,2434,1423])
# color = np.array(['r','g','b','y','r','g'])

# plt.plot(car,weight)
# plt.show()
# size = np.array([20,30,50,35,40,25])
# plt.scatter(car,weight ,c=color ,s=size)
# plt.show()

# plt.bar(car,weight  , color=color)
# plt.show()

plt.hist(weight , color='green')
plt.show()

plt.pie(weight , labels=car , explode=(0.1,0,0,0,0,0) , shadow=True,autopct='%1.1f%%',startangle=140)
plt.show()
