import numpy as np

# Площина, задана двома ортогональними векторами
v1 = np.array([1, 1, 0])
v2 = np.array([-1, 1, 0])

# Нормалізуємо для отримання ортонормованого базису
u1 = v1 / np.linalg.norm(v1)
u2 = v2 / np.linalg.norm(v2)

# Матричне представлення
Q = np.column_stack([u1, u2])
print(f"Матриця базису Q:")
print(Q)

# Матриця проєкції
P = Q @ Q.T
print(f"\nМатриця проєкції P = Q Q^T:")
print(P)

# Проєкція через матричне множення
v = np.array([3, 2, 4])
proj_matrix = P @ v

print(f"\nВектор v = {v}")
print(f"Проєкція через матрицю: P @ v = {proj_matrix}")

# Перевірка ідемпотентності
P_squared = P @ P
print(f"\nПеревірка P² = P:")
print(f"  Різниця ||P² - P|| = {np.linalg.norm(P_squared - P):.10f}")