"""
Операція обертання зберігає довжину вектора і кути між векторами, 
тобто не спотворює форму об’єкта, а лише змінює його орієнтацію в просторі.
Обертання навколо y.
"""

import numpy as np
import matplotlib.pyplot as plt

# Вихідна фігура — квадрат одиничного розміру
square = np.array([
    [0, 1, 1, 0],  # координати x
    [0, 0, 1, 1]   # координати y
])

# Обертання на 45 градусів
theta = np.pi / 4  # 45 градусів
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# Застосовуємо до квадрата
square_rotated = R @ square

# Виведення результату
print("Матриця Обертання R:")
print(R)
print("\nПочатковий квадрат (рядки: x, y):")
print(square)
print("\nПісля перетворення R · square:")
print(square_rotated)
