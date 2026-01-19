import numpy as np
import matplotlib.pyplot as plt

# Матриця коефіцієнтів та вектор правої частини
A = np.array([
    [2, 1],
    [1, -1]
])
b = np.array([5, 1])

# Розв'язуємо систему
x_solution = np.linalg.solve(A, b)
print(f"Розв'язок системи: x₁ = {x_solution[0]:.2f}, x₂ = {x_solution[1]:.2f}")

print("~" * 20)
# Система трьох рівнянь з трьома невідомими
A_3d = np.array([
    [1, 1, 1],
    [2, -1, 1],
    [1, 2, -1]
])
b_3d = np.array([6, 3, 2])

# Розв'язуємо систему
x_sol_3d = np.linalg.solve(A_3d, b_3d)
print(f"Розв'язок системи 3×3:")
print(f"  x₁ = {x_sol_3d[0]:.2f}")
print(f"  x₂ = {x_sol_3d[1]:.2f}")
print(f"  x₃ = {x_sol_3d[2]:.2f}")

# Перевірка
print(f"\nПеревірка: A @ x = {A_3d @ x_sol_3d}")
print(f"Має дорівнювати b = {b_3d}")

print("~" * 20)
# Система 4 рівняння, 4 невідомих
A_4d = np.array([
    [1, 2, -1, 3],
    [2, -1, 1, 1],
    [1, 1, 1, -1],
    [3, 1, -2, 2]
])
b_4d = np.array([5, 4, 6, 7])

# Розв'язуємо
x_sol_4d = np.linalg.solve(A_4d, b_4d)

print(f"\nРозв'язок системи 4 x 4:")
for i, val in enumerate(x_sol_4d, 1):
    print(f"  x_{i} = {val:.4f}")

# Перевірка розв'язку
residual = A_4d @ x_sol_4d - b_4d
print(f"\nПохибка: {np.linalg.norm(residual):.2e}")