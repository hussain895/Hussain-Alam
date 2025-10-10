def add(a , b):
    c = a + b
    print(c)

    
add(3, 4)


def add(a , b):
   c = a + b
   print("Add a and b = " , a+b)
   return(a ,b)



def sub(a , b):
   c = a - b
   print("Subtract a and b = " , a-b)
   return(a , b)



def multiply(a , b):
   c = a * b
   print("Multiply a and b = " , a*b)
   return(a , b)




def divide(a , b):
   c = a // b
   print("Divide a and b = " , a//b)
   return(a , b)

x = int(input("Enter The First Value = "))
y = int(input("Enter The Second Value = "))

sub(x,y)
multiply(x,y)
divide(x,y)
add(x,y)

