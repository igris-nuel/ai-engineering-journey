

def partial_derivative_x(f,x,y,h=0.0001):
    return (f(x + h, y) - f(x - h, y))/ 2 * h

def partial_derivative_y(f,x,y,h=0.0001):
    return (f(y + h, x) - f(y - h, x))/ 2 * h

def f(x, y):
    return x**2 + y**2

x = 2
y = 3

dx = partial_derivative_x(f, x, y)
dy = partial_derivative_y(f, x, y)

print("df/dx:", dx)
print("df/dy:", dy)