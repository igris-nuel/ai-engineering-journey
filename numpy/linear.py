import numpy as np
import matplotlib.pyplot as plt
# from utils import plot_lines

# −𝑥1+3𝑥2=7
# 3𝑥1+2𝑥2=1

A = np.array([
    [-1, 3],
    [3, 2]
], dtype= np.dtype(float))

b = np.array(
    [7, 1], 
    dtype = np.dtype(float))

matrix = np.linalg.solve(A, b)
# print(matrix)

# Evaluating Determinant of a Matrix
A_det = np.linalg.det(A)
# print(f"{A_det:.2f}")


# Representation of the system as a matrix

A_system = np.hstack((A,b.reshape(2,1)))

# print(A_system)
# plot_lines(A_system)

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# plt.plot(A, b)
# plt.show()


# System of Linear Equations with No Solutions

# −𝑥1+3𝑥2=7
#  3𝑥1−9𝑥2=1,

# calculate the determinant of the corresponding matrix
A_2 = np.array([[-1, 3], [3, -9]], dtype=float)
b_2 = np.array([7, 1], dtype=float)

A_det = np.linalg.det(A_2)
# print("Determinant:", A_det)

# try:
#     x_2 = np.linalg.solve(A_2, b_2)
#     # print(x_2)
# except np.linalg.LinAlgError as err:
    # print("Linear algebra error:", err)

A2_system = np.hstack((A_2, b_2.reshape(2, 1)))
# plt.plot(A2_system)
# plt.show()


#  System of Linear Equations with an Infinite Number of Solutions

# −𝑥1+3𝑥2=7
# 3𝑥1−9𝑥2=−21

A_3 = np.array([[-1, 3], [3, -9]], dtype=float)
b_3 = np.array([7, -21], dtype=float)

A3_system = np.hstack((A_3, b_3.reshape(2, 1)))

ma = np.linalg.solve(A_3, b_3)
print(ma)
