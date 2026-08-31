import numpy as np

# system of linear equations with more unknown variables
# 4𝑥1−3𝑥2+𝑥3=−10
# 2𝑥1+𝑥2+3𝑥3=0
# −𝑥1+2𝑥2−5𝑥3=17




A = np.array([
    [4, -3, 1],
    [2,  1, 3],
    [-1, 2, -5],
], dtype=np.dtype(float))

b = np.array([-10, 0, 17], dtype=np.dtype(float))

x = np.linalg.solve(A,b)
x_det = np.linalg.det(A)
# print(x)
# print(x_det)


# What happens if the system has no unique solution?

# 𝑥1+𝑥2+𝑥3=2,
# 𝑥2−3𝑥3=1,
# 2𝑥1+𝑥2+5𝑥3=0

A_2= np.array([
        [1, 1, 1],
        [0, 1, -3],
        [2, 1, 5]
    ], dtype=np.dtype(float))

b_2 = np.array([2, 1, 0], dtype=np.dtype(float))

# print(np.linalg.solve(A_2, b_2))
d_2 = np.linalg.det(A_2)
# print(d_2)