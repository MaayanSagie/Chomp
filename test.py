import numpy as np
import random

arr = np.array([[1,2,0], [1,0,2]])
print (arr)
indices = np.where(arr==0)
print(indices)
rows_cols = list(zip(indices[0], indices[1]))
print(rows_cols)
print(random.choice(rows_cols))
print(random.choice(rows_cols))
print(random.choice(rows_cols))
print(random.choice(rows_cols))
