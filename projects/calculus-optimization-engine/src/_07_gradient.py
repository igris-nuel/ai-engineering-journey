from _06_partial_derivatives import (
    partial_derivative_x, partial_derivative_y
)

def gradient(f, x, y, h=0.001):
    dx = partial_derivative_x(f, x, y, h)
    dy =partial_derivative_y(f, x, y, h)

    return [dx, dy]

def f(x, y):
    return x**2 + y**2

gradient_xy = gradient(f,2, 3)

print(gradient_xy)

