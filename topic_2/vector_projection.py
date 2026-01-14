import numpy as np

# Два вектори
a = np.array([4, 3])
b = np.array([2, 1])

print(f"Вектор a = {a}")
print(f"Вектор b = {b}")

# Обчислюємо проєкцію a на b
proj_b_a = ((a @ b) / (b @ b)) * b

print(f"\nПроєкція a на b:")
print(f"  proj_b(a) = {proj_b_a}")
print(f"  Довжина проєкції: {np.linalg.norm(proj_b_a):.4f}")

# Скалярна проєкція
comp_b_a = (a @ b) / np.linalg.norm(b)
print(f"  Скалярна проєкція: {comp_b_a:.4f}")