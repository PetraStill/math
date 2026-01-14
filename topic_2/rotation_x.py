"""
Приклад коду для відображення відносно осі x.
"""

import numpy as np
import matplotlib.pyplot as plt

# Вихідна фігура — квадрат одиничного розміру
square = np.array([
    [0, 1, 1, 0],  # координати x
    [0, 0, 1, 1]   # координати y
])

# Відображення відносно осі x
M_x = np.array([
    [1, 0],
    [0, -1]
])

square_reflected = M_x @ square

# Виведення результату
print("Матриця Відображення M_x:")
print(M_x)
print("\nПочатковий квадрат (рядки: x, y):")
print(square)
print("\nПісля перетворення M_x · square:")
print(square_reflected)