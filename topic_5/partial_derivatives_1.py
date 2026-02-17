import numpy as np
from scipy.optimize import approx_fprime

# Функція f(x, y) = x^3*y^2 + 2*x*y + 5
def f(coords):
    x, y = coords
    return x**3 * y**2 + 2*x*y + 5

# Точка, в якій обчислюємо похідні
point = np.array([2.0, 3.0])

# Чисельне обчислення частинних похідних
epsilon = 1e-8
partial_derivatives = approx_fprime(point, f, epsilon)

print(f"\nЧисельні частинні похідні:")
print(f"∂f/∂x = {partial_derivatives[0]:.6f}")
print(f"∂f/∂y = {partial_derivatives[1]:.6f}")
