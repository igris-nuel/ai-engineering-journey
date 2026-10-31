
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

