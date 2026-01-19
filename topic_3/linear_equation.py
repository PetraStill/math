import numpy as np

# Система: 2x₁ + 3x₂ = 8
#          x₁ - x₂ = 1

A = np.array([
    [2, 3],
    [1, -1]
])

b = np.array([8, 1])

print("Матриця коефіцієнтів A:")
print(A)
print(f"\\nВектор правої частини b: {b}")

# Розв'язуємо систему
x = np.linalg.solve(A, b)

print(f"\nРозв'язок системи x: {x}")
print(f"  x₁ = {x[0]}")
print(f"  x₂ = {x[1]}")

# Перевірка: A @ x має дорівнювати b
result = A @ x
print(f"\nПеревірка A @ x = {result}")

print("~" * 20)

# Система з 4 рівнянь і 4 невідомих
A = np.array([
    [2, 1, -1, 3],
    [1, 3, 2, -1],
    [3, -1, 1, 2],
    [1, 2, 3, 1]
])

b = np.array([7, 8, 5, 10])

x = np.linalg.solve(A, b)

print(f"\nРозв'язок для системи з 4 рівнянь і 4 невідомих:")
for i, val in enumerate(x, 1):
    print(f"  x_{i} = {val:.4f}")

# Перевірка
solution_error = A @ x - b
print(f"\nПохибка розв'язку: {np.linalg.norm(solution_error):.2e}")

print("~" * 20)
# Несумісна система
A_inconsistent = np.array([
    [1, 1],
    [1, 1]
])

b_inconsistent = np.array([2, 3])

try:
    x = np.linalg.solve(A_inconsistent, b_inconsistent)
    print(f"Розв'язок несумісної системи: {x}")
except np.linalg.LinAlgError as e:
    print(f"\nПомилка: {e}")
    print("Система не має розв'язку або матриця вироджена")