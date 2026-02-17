import numpy as np
from scipy.optimize import approx_fprime

# Функція f(x, y) = x^2*y + y^3
def f(coords):
    x, y = coords
    return x**2 * y + y**3

# Точка
point = np.array([2.0, 1.0])

# Обчислення градієнта
gradient = approx_fprime(point, f, epsilon=1e-8)

print(f"Градієнт в точці ({point[0]}, {point[1]}): {gradient}")
print(f"∇f = ({gradient[0]:.6f}, {gradient[1]:.6f})")

# Довжина градієнта
magnitude = np.linalg.norm(gradient)
print(f"Довжина градієнта: |∇f| = {magnitude:.6f}")

# Одиничний вектор в напрямку градієнта
direction = gradient / magnitude
print(f"Напрямок найшвидшого зростання: ({direction[0]:.6f}, {direction[1]:.6f})")
