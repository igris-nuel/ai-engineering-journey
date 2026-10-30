
def f(x):
    return x**2 - 4*x + 3


def evaluate_function(f, x_values):
    result = []

    for x in x_values:
        result.append((x, f(x)))

    return result


x_values = [-1, 0, 1, 2, 3, 4]

results = evaluate_function(f, x_values)

for x, y in results:
    print(f"x = {x}, f(x) = {y}")


def g(x):
    return x**3 - 2*x

gx_values = [-2,-1, 0,1,2]

g_results = evaluate_function(g, gx_values)

print(f"\n g results ")
for x, y in g_results:
    print(f" x = {x}, g(x) = {y}")


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


import math 




