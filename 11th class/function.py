def fun():
    print("Welcome To Habib University")

fun()


def add(num1: int , num2: int):
    "ADD TWO NUMBERS"
    num3 = num1 + num2
    return num3

num1 = 10
num2 = 17
result = add(num1 , num2)
print(f"The Addition of {num1} and {num2} is : {result}")


def evenodd(x):
    if (x % 2 == 0):
        print("Even")
    else:
        print("Odd")

evenodd(5)
evenodd(17)
evenodd(2)
evenodd(7)
evenodd(10)

def myfun(x , y=50):
    print("x" , x)
    print("y" , y)

myfun(10)
myfun(10,5)

def student(firstname , lastname):
    print(firstname , lastname)

student(firstname="Habib" , lastname="University")
student(lastname="Alam Zaidi" , firstname="Syed Hussain")

def nameage(name , age):
    print("Hi , I am " , name)
    print("My Age is " , age)

print("Case-1:")
nameage("Syed Hussain Alam Zaidi" , 17)



def square(number):
    return number*number

result = square(5)
print(result)


def square(x,y):
    return x*y

result = square(5,7)
print(result)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
num = 5
result = factorial(num)
print(f"The Factorial of {num} is : {result}")


def fibonacci(n):
    if n ==0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = 7
result = fibonacci(num)
print(f"The Fibonacci of {num} is : {result}")


def calculate_total(prices , discount_rate,tax_rate):
    payment_mode = input("Enter The Payment Mode (cash/card):").lower()
    subtotal = sum(prices)
    discount = subtotal * discount_rate
    taxed_amount = (subtotal - discount) * tax_rate
    if subtotal > 10000:
        print("You Have A 10% Discount!")
      
        discount_rate = 0.1
    else:
        discount_rate = 0.0
    if payment_mode == "cash":
        print("You Have A 5% Tax!")
        tax_rate = 0.05
    else:
        tax_rate = 0.0
   
    return subtotal - discount + taxed_amount
prices = input("Enter The Prices Of Items (Space-Separated):")
prices = prices.split()
print(prices)
prices = [float(price) for price in prices]
discount_rate = 0.0

tax_rate = 0.0
total_amount = calculate_total(prices , discount_rate , tax_rate)
print(f"The Total Amount is : {total_amount}")

