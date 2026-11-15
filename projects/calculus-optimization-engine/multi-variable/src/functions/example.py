import numpy as np

from function import Function


def f(x):
    return x[0]**2 + 3*x[0]*x[1] + 2*x[1]**2

def g(x):
    return np.array([
        x[0]**2 + x[1],
        x[0] * x[1]
    ])

scalar_function = Function(
    func=f,
    input_dim=2,
    output_dim=None,
    name="scalar_function"
)
vector_function = Function(
    func=g,
    input_dim=2,
    output_dim=2,
    name="vector_function"
)


x = np.array([2.0, 3.0])

print(scalar_function(x))
print(vector_function(x))

print(scalar_function)
print(vector_function)