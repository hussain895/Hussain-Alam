list = [10 , 24 , 14 , 45 , 67]
print("\n List Of Numbers : ")
list.append(2)
print(list[1])
print(list[3])
print(list)
print(len(list))
list2 = ['car' , 'bike']
list.append(list2)
print(list)
list.insert(3 , "cat")
print(list)
list.reverse()
print(list)
list.remove(2)
print(list)
for i in range(24,10):
    list.remove(i)
print(list)
print(list.index(10))



# lisr = [['car','are'],['life']]

# print(list[0][1])
# print(list[1][0])


# string = input("Enter Elements (Space-Separated):")
# lst = string.split()
# print("The List Is : " , lst)


# n = int(input("Enter The Size Of List : "))ss

# lst = list(map(int,input("Enter The Integer Element : " ).strip().split()))[:n]
# for i in range(len(lst)):
#     list1 =lst[i]*lst[i]

#     print("The List Is : " , list1)




tuple1 = (" car " , " Bike " , " Airplane " , 1  , 3.5)
print(tuple)
a , b , c , x , y = tuple1
print(a)
print(b)
print(c)
print(x)
print(y)
tuple2 = (" Cycle " , " Bus ")
tuple3 = tuple1 + tuple2
print(tuple3)
del tuple3
print(tuple3)
