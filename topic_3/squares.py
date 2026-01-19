import numpy as np

# Матриця A: кожен рядок - це [x_i, 1]
A = np.array([
    [1, 1],
    [2, 1],
    [3, 1]
], dtype=float)

# Вектор b: значення y_i
b = np.array([2, 3, 5], dtype=float)

print("Матриця A (3×2):")
print(A)
print(f"\nВектор b: {b}")

# Спроба розв'язати систему
try:
    x = np.linalg.solve(A, b)
    print(f"\nРозв'язок: {x}")
except np.linalg.LinAlgError as e:
    print(f"\nПомилка бо матриця не квадратна: {e}")
    print("Система не має точного розв'язку")
