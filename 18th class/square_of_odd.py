square = []

for x in range(1,21):
 square.append(x**2)

print("Squares : " , square)

odd_square = []
for x in range(1,21,2):
   odd_square.append(x**2)

print("Odd Squares : " , odd_square)

even_square = []
for x in range(0,22,2):
   even_square.append(x**2)
        
print("Even Squares : " , even_square)


sum_odd = sum(odd_square)
print("Sum of Odd Squares : " , sum_odd)

sum_even = sum(even_square)
print("Sum of Even Squares : " , sum_even)

add = sum_odd + sum_even
print("Sum of Odd and Even Squares : " , add)



