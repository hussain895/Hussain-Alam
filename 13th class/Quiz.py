# print("My Name Is Syed Hussain Alam Zaidi")
# print("My Age Is 17")
# print("My Favourite Language Is Python")

# print("--------------------------------------------------------------------------------------")

# a = 2
# b = 2.5
# c = True
# d = "Hussain"
# e  =[10 ,11,12]
# f = (10,11,12)
# dict = {11,12,13}

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(dict))

# print("--------------------------------------------------------------------------------------")

# a = 2.5
# print(int(a))

# print("--------------------------------------------------------------------------------------")

# k = 3
# c = 4
# k = c + k
# c = k - c
# k = k - c
# print(k)
# print(c)

# print("--------------------------------------------------------------------------------------")

# a = input("Enter Your Name : ")
# print(f"Welcome " , a )

# print("--------------------------------------------------------------------------------------")

# B = 10
# C = 20

# A = B*C/2
# print(f"Area Of A Triangle Is {A}")

# u = A + B + C
# print(f"Perimeter Of A Triangle Is {u}")

# print("--------------------------------------------------------------------------------------")

# Math = 25
# Physics = 23
# Computer = 22
# English = 24

# Obtained_Marks = Math+Physics+Computer+English

# Total_Marks = 150

# per = Obtained_Marks/Total_Marks*100
# print(f"Your Obtained Marks is {Obtained_Marks}")
# print(f"Your Percentage Is {per} %")

# print("--------------------------------------------------------------------------------------")

# Celsius = int(input("Enter The Temperature In Celsius = "))
# fahrenheit = (Celsius*9/5)+32
# print(f"The Temperature In Fahrenheit Is = {fahrenheit}")

# print("--------------------------------------------------------------------------------------")

# a = int(input("Enter A Number = "))
# b = a*a
# c = a*a*a
# print(f"The Square Of a Is = {a}")
# print(f"The Cube Of a Is = {c}")

# print("--------------------------------------------------------------------------------------")

# a = str(input("Enter Your Name : "))
# count = 0

# vowels = "aeiouAEIOU"

# for char in a:
#     if char in vowels:
#         count+=1
#         print(char)
#         print(count)

# print("--------------------------------------------------------------------------------------")

# a = "My Name Hussain "
# print(a[::-1])

# print("--------------------------------------------------------------------------------------")

# b = "maham"
# if b == b[::-1]:
#     print("It Is A Palindrome")
# else:
#     print("It Is Not a Palindrome")

# print("--------------------------------------------------------------------------------------")

# sentence = input("Enter The Sentence : ")
# word = input("Enter The Word : ").lower()

# count = sentence.split().count(word)
# print(f"The Word {word} Appear {count} times")


# print("--------------------------------------------------------------------------------------")

# n = int(input("Enter The Number : "))

# if n < 0 :
#     print(" The Number Is Negative ")
# elif n > 0 :
#     print(" The Number Is Positive ")
# elif n == 0 :
#     print(" The Number Is Equal To 0 ")

# print("--------------------------------------------------------------------------------------")

# a = "hussain489@gmail.com" 
# b = "@hussain"

# c = input("Enter The Username : ")
# d = input("Enter The Password : ")

# if a==c and b==d:
#     print("Your Account Is Correct")
# else:
#     print("Your Account Is Incorrect")


# print("--------------------------------------------------------------------------------------")


# year = int(input("Enter A Year : "))

# if year % 4 == 0:
#     print(year,"It is a Leap Year ")
# else:
#     print(year,"It is not a leap year ")

# print("--------------------------------------------------------------------------------------")

# print("   Find The Largest Value  ")

# a = int(input("Enter The Value Of a : "))
# b = int(input("Enter The Value Of b : "))
# c = int(input("Enter The Value Of c : "))


# if a>b and a>c:
#     print("A is the largest value")
# elif b>a and b>c:
#       print("B is the largest value")
# else:
#       print("C is the largest value")

# print("--------------------------------------------------------------------------------------")

# natural_number = int(input("Enter A Natural Number : "))
# sum = 0
# for i in range(1, natural_number + 1):
#     sum += i
# print(f"The Sum Of First {natural_number} Natural Numbers Is {sum}")

# print("--------------------------------------------------------------------------------------")

# print(" TABLE ")

# a = int(input("  Enter The Value : "))
# b = int(input(" Give A Range : "))

# for i in range (1 , b+1):
    
#     print(f"{a} x {i} = {a*i}")

# print("--------------------------------------------------------------------------------------")

# number = input("Enter A Numbers : ")
# digit_sum = 0
# for digit in number:
#     digit_sum += int(digit)
# print(f"The Sum Of The Digits In The Number {number} Is {digit_sum}")

# print("--------------------------------------------------------------------------------------")

# fibonacci_terms = int(input("Enter The Number Of Terms : "))
# a, b = 0, 1
# print("Fibonacci Sequence:")
# for _ in range(fibonacci_terms):
#     print(a, end=' ')
#     a, b = b, a + b 

# print("--------------------------------------------------------------------------------------")


# for i in range(1, 50+1):

#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")


# print("--------------------------------------------------------------------------------------")

# a = int(input("Enter A Number : "))

# if a % 2 != 0:
#     print(f"{a} is Prime Number")
# else:
#     print(f"{a} is not Prime Number")


# print("--------------------------------------------------------------------------------------")

# def factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num*factorial(num-1)
    
# num=int(input("Enter a Number : "))
    
# if num<0:
#         print("Factorial cannot be found for negative number")
# elif num == 1:
#         print("Factorial of 0 to 1 ")
# else:
#      print(f"Factorial of {num} is :",factorial(num))


print("--------------------------------------------------------------------------------------")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_value = max(a)
min_value = min(a)
print(f"Maximum Value: {max_value}")
print(f"Minimum Value: {min_value}")

print("--------------------------------------------------------------------------------------")

# remove duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
list = list(set(my_list))
print(f"List after removing duplicates: {list}")

print("--------------------------------------------------------------------------------------")

# count occurrences of a each element in a list
my_list = [1, 2, 2, 3, 4, 4, 5]
occurrences = {}
for item in my_list:
    if item in occurrences:
        occurrences[item] += 1
    else:
        occurrences[item] = 1
print("Occurrences of each element:")
for item, count in occurrences.items():
    print(f"{item}: {count}")
  

print("--------------------------------------------------------------------------------------")

# Demonstrate tuple unpacking with an example
my_tuple = (1, 2, 3)
tuple1 = (5,6,7)
tuple2 = my_tuple + tuple1
a, b, c, d, e, f = tuple2
print(f"Unpacked values: {a}, {b}, {c}, {d}, {e}, {f}") 



print("--------------------------------------------------------------------------------------")

#Comcatenate two tuples and display the result
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated Tuple: {concatenated_tuple}")      

print("--------------------------------------------------------------------------------------")

# Create a dic of 5 students with their names as keys and their marks as values.print the average marks of the students.
students_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eva": 95
}

average_marks = sum(students_marks.values()) / len(students_marks)
print(f"Average Marks: {average_marks}")

print("--------------------------------------------------------------------------------------")

# write a program to add and remove items from a dict
my_dict = {"a": 1, "b": 2, "c": 3}  
# Add an item
my_dict["d"] = 4
# Remove an item
del my_dict["b"]
print(f"Updated Dictionary: {my_dict}")

print("--------------------------------------------------------------------------------------")

# merge two dicts and display the result
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(f"Merged Dictionary: {merged_dict}")

print("--------------------------------------------------------------------------------------")

# write a program to count the frequency of characters in a string using a dict
input_string = "hello world"
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print("Character Frequency:")
for char, count in char_frequency.items():
    print(f"{char}: {count}")   

print("--------------------------------------------------------------------------------------")

# check if a given key exists in a dict
my_dict = {"a": 1, "b": 2, "c": 3}
key_to_check = "b"
if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")