"""
Векторний добуток англійською — cross product.
Також уживають: vector product (рідше, більш формально).
"""
import numpy as np

# Вектори
u = np.array([2, 3, 4])
v = np.array([5, 6, 7])

# Через NumPy
w = np.cross(u, v)

print(f"Вектор u: {u}")
print(f"Вектор v: {v}")
print(f"\nВекторний добуток (NumPy): {w}")

# Перевірка ортогональності
print(f"\nОртогональність:")
print(f"  u · (u×v) = {u @ w}")
print(f"  v · (u×v) = {v @ w}")
