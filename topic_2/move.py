"""
Приклад перетворення, що змінює форму об’єкта, але не його площу.
"""

import numpy as np
import matplotlib.pyplot as plt

# Вихідна фігура — квадрат одиничного розміру
square = np.array([
    [0, 1, 1, 0],  # координати x
    [0, 0, 1, 1]   # координати y
])

# Горизонтальний зсув
k = 0.5
H = np.array([
    [1, k],
    [0, 1]
])

square_sheared = H @ square

# Виведення результату
print("Матриця горизонтального зсуву H:")
print(H)
print("\nПочатковий квадрат (рядки: x, y):")
print(square)
print("\nПісля перетворення H · square:")
print(square_sheared)
