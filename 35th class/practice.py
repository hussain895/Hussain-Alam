import numpy as np

transaction = np.array([100 , 200 , 300 ])
transaction = transaction.astype(float)
print(transaction , transaction.dtype ,"\n","Item Size : ", transaction.itemsize)
print()
transactions = transaction.astype(str)
print(transactions , transactions.dtype ,"\n","Item Size : ", transactions.itemsize)