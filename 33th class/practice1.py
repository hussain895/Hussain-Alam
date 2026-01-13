import numpy as np

temp = np.array([28 , 35 , 42 , 39 , 45 , 30 ])
idx = np.where(temp > 40)

print("High Tempertures : " , temp[idx])
print("Indices : " ,idx)
print()

idex = np.where(temp > 38)
print("High Tempertures : " , temp[idex])
print("Indices : " ,idex)
print()

counts = len(idex[0])
print("These are the numbers that exceed the limit(38) : " , counts)