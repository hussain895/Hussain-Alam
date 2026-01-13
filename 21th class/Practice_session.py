# n = int(input("Enter value: "))

# # Upper half
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*(2*i-1))

# # Lower half
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "*"*(2*i-1))




# string = input("Enter a string: ")

# vowels = "aeiou"


# for char in vowels:
#     count = string.lower().count(char)
#     print(f"{char}: {count}")
    
n = int(input("Enter The Value : "))
for i in range (1  , n +1):

    for j in range ( n , i-1 , -1):
        print(" ",end="")
    for k in range(1, i+1):
        print("*", end="")
    for l in range ( 2, i+1):
        print("*",end="")

    print()


for i in range (2  , i+1 ):

    for j in range ( 1 , i+1):
        print(" ",end="")
    for k in range(n, i-1, -1):
        print("*", end="")
    for l in range (n-1 , i-1,-1):
        print("*",end="")

    print()   