import numpy as np 

distances = np.array([ 4 , 9 , 16 , 25 ])
print(np.sqrt(distances))
print(np.square(distances))

print()
for distance in distances:
    print(np.sqrt(distance))
print()

result = []
for d in distances:
    result.append(d ** 0.5)

print(result)
print()