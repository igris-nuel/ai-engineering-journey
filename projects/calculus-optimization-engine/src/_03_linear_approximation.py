import math
from _02_derivatives import derivative_x

def linear_approximation(f, derivative, a, x):
    return f(a) + derivative(a) * (x - a)


def f(x):
    return math.sqrt(x)


x= 4.1
a=4
approximation = linear_approximation(f, derivative_x, a, x)

actual = f(x)

print("Approximation:", approximation)
print("Actual:", actual)
print("Error:", abs(actual - approximation))


x_values = [
    4.01,
    4.1,
    4.5,
    5,
    6,
    8,
    10
]

print("\n")

for x in x_values:
    appro= linear_approximation(f, derivative_X, a, x)
    actual = f(x)
    error = abs(actual - appro)

    print(
        
        f"x={x}, "
        f"actual={actual}, "
        f"approximation={approximation}, "
        f"error={error}"
    )

# The farther we move from the point of approximation, the worse the linear approximation generally becomes.

# That's not a bug.
# The tangent line is a local model.