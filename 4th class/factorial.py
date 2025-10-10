def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)
    
num=int(input("Enter a Number : "))
    
if num<0:
        print("Factorial cannot be foward for negative number")
elif num == 1:
        print("Factotial of 0 to 1 ")
else:
     print("Factorial of num is : ",factorial(num))


       
    
        
      