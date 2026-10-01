import numpy as np
from cholesky import cholesky

A = np.array([
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98],
],dtype=float)

L = cholesky(A)

print("A:")
print(A)

print("\nL:")
print(L)

print("\nLL^T:")
print(L @ L.T)