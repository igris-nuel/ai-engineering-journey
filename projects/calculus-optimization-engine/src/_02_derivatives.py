import math
from _01_functions import f

# Numerical derivative

# forward difference

def numerical_derivative_forward(f, x, h):
        return (f(x + h) - f(x)) / h

h_values = [
    1,
    0.1,
    0.01,
    0.001,
    0.0001,
    0.00001,
    0.000001,
    0.0000001,
    0.00000001
]

print("\n numerical derivatives:")
for h in h_values:
    result = numerical_derivative_forward(f, 2, h)
    print(f"h = {h}, derivative ≈ {result}")

# central difference

def numerical_derivative_central(f, x, h=0.001):
    return (f(x + h) - f(x - h)) / (2*h)

def analytical_derivative(x):
    return 2 * x - 4

x = 1.5
h = 0.01

true_value = analytical_derivative(x)
forward = numerical_derivative_forward(f, x, h)
central = numerical_derivative_central(f, x, h)

print("True:", true_value)
print("Forward:", forward)
print("Central:", central)


def derivative_x(x):
    return 1 / (2 * math.sqrt(x))



def derivative_function(f, h=0.001):
    def derivative(x):
        return numerical_derivative_central(f, x, h)
    return derivative

def nth_derivative(f,n, h=0.001):
    derivative=f
    for _ in range(n):
        derivative = derivative_function(derivative,h)
    return derivative