import numpy as np
from scipy import linalg

# Матриця системи
A = np.array([
    [2, 1, -1],
    [4, -1, 2],
    [-2, 2, 1]
], dtype=float)

# Обчислюємо LU-розклад один раз
P, L, U = linalg.lu(A)

print("Нижня трикутна матриця L:")
print(L)
print("\nВерхня трикутна матриця U:")
print(U)
print()

# Тепер можемо швидко розв'язувати системи для різних b
b = np.array([3, 13, 4], dtype=float)

print(f"Розв'язуємо Ax = b, де b = {b}")
print()

# Крок 1: Застосовуємо перестановку до b
Pb = P @ b
print(f"Після перестановки: Pb = {Pb}")

# Крок 2: Прямий хід - розв'язуємо Ly = Pb
y = linalg.solve_triangular(L, Pb, lower=True)
print(f"Після прямого ходу: y = {y}")

# Крок 3: Зворотний хід - розв'язуємо Ux = y
x = linalg.solve_triangular(U, y, lower=False)
print(f"Розв'язок: x = {x}")
print()

# Перевірка
print(f"Перевірка: Ax = {A @ x}")
print(f"Має дорівнювати b = {b}")
