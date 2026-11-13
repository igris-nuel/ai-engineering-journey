from _02_derivatives import numerical_derivative_central as nd

def newton_step(f,a,derivative, i=100,  tolerance=1e-8):
     
    for _ in range(i):
        if abs(f(a)) < tolerance:
            return a

        dfx = derivative(f,a)

        if dfx == 0:
            raise ValueError(
                "Newton's method failed: derivative is zero."
            )

        a = a - f(a) / dfx

    return a

def f(x):
    return  x**2 - 4

appr = newton_step(f, 3,nd )

print("approximation:",appr)