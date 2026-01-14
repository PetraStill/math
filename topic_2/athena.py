import numpy as np
import matplotlib.pyplot as plt

# Квадрат
square = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0]
])

# Афінне перетворення в однорідних координатах
# Обертання на 30° + зсув [2, 1]
theta = np.pi / 6  # 30 градусів

# Створюємо матрицю 3×3
affine_matrix = np.array([
    [np.cos(theta), -np.sin(theta), 2],
    [np.sin(theta), np.cos(theta), 1],
    [0, 0, 1]
])

# Перетворюємо квадрат в однорідні координати
square_homogeneous = np.vstack([square, np.ones(square.shape[1])])

# Застосовуємо перетворення одним множенням
square_transformed = affine_matrix @ square_homogeneous

print(f"\nПісля перетворення:")
print(square_transformed)

# Повертаємось до звичайних координат (відкидаємо третю координату)
square_result = square_transformed[:2, :]
print(f"\nКвадрат після обертання та зсуву (координати вершин):")
print(square_result)