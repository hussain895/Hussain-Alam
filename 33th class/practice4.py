import numpy as np

data = np.arange(24)
reshaped = data.reshape(6 , 4)
print(reshaped)
print()

data = np.arange(24)
reshapeds = data.reshape(8 , 3)
print(reshapeds)
print()
print("cannot reshape array of size 24 into shape (2,9)")
print()
data = np.arange(24)
reshape = data.reshape(2 , 9)
print(reshape)
