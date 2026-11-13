from _02_derivatives import nth_derivative
import math

def taylor_approximation(f,x,a,order, h=0.001):

    approximation = 0.0

    for k in range(order + 1):
        derivative = nth_derivative(f,k, h)
        derivative_value = derivative(a)

        term = (
            (derivative_value/math.factorial(k)) * (x - a)**k
        )

        approximation +=term

    return approximation

def f(x):
    return math.exp(x)

app = taylor_approximation(f,0.5,0,5)

print("exponential:",app)