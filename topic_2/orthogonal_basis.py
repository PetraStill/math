"""
Розглянемо приклад ортогонального базису в R^2
"""
import numpy as np

# Ортогональний базис для R²
v1 = np.array([3, 0])
v2 = np.array([0, 4])

print("Ортогональний базис:")
print(f"  v1 = {v1}")
print(f"  v2 = {v2}")

# Виразимо вектор w через цей базис
w = np.array([6, 8])
print(f"\nВектор w = {w}")

# Коефіцієнти ортогонального базису:
alpha1 = (w @ v1) / (v1 @ v1)
alpha2 = (w @ v2) / (v2 @ v2)

print(f"w = {alpha1:.2f}*v1 + {alpha2:.2f}*v2")

# Перевірка
w_reconstructed = alpha1 * v1 + alpha2 * v2
print(f"Результат: {w_reconstructed}")
