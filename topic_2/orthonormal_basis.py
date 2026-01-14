"""
Стандартний базис простору R^n, який складається зі стовпців одиничної матриці, 
є ортонормованим базисом. 
"""

import numpy as np

# Ортогональний базис для R²
v1 = np.array([3, 0])
v2 = np.array([0, 4])

print("Ортогональний базис:")
print(f"  v1 = {v1}, ||v1|| = {np.linalg.norm(v1)}")
print(f"  v2 = {v2}, ||v2|| = {np.linalg.norm(v2)}")

# Нормалізуємо вектори
u1 = v1 / np.linalg.norm(v1)
u2 = v2 / np.linalg.norm(v2)

print("\nОртонормований базис:")
print(f"  u1 = {u1}, ||u1|| = {np.linalg.norm(u1):.4f}")
print(f"  u2 = {u2}, ||u2|| = {np.linalg.norm(u2):.4f}")

# Коефіцієнти ортонормованого базису
w = np.array([6, 8])
beta1 = w @ u1
beta2 = w @ u2

print(f"\nВиразимо w = {w} через ортонормований базис:")
print(f"w = {beta1:.2f}*u1 + {beta2:.2f}*u2")