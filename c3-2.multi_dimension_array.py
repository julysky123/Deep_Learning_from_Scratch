import numpy as np

A=np.array([1,2,3,4])
print(np.ndim(A))       #1
print(A.shape)         #(4,)

A=np.array([[i+j for i in range(3)] for j in range(3)])
print(A)

#다음에 계속.