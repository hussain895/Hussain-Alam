def compute_hcf(x , y):
   
    while(y):
     x , y = y , x % y
    return x
a = int(input("Enter a value : "))
b = int(input("Enter a Value : "))

hcf = compute_hcf( a , b)
print("The HCF is " , hcf) 