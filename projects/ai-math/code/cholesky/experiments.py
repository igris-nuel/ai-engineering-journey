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
print(np.allclose(L @ L.T, A))


b = np.array([6.0, 7.0, 6.0])

x1 = np.linalg.solve(A, b)

y = np.linalg.solve(L,b)

x2 = np.linalg.solve(L.T,y)

print(np.allclose(x1, x2))

