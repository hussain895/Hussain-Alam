import numpy as np

random_number = np.random.randint(22, 32 , size=(1,1))

print(random_number)

avg = random_number.mean()

print("\n"f"The Average Of The Random Number Is : {avg}")

Hottest_Temp = random_number.argmax()
Collest_Temp = random_number.argmin()

print("\n"f"The Hottest Temperature Is : {Hottest_Temp}")
print("\n"f"The Collest Temperature Is : {Collest_Temp}")