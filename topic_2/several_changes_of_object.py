"""
Лінійні перетворення можна комбінувати, застосовуючи їх послідовно. 
Порядок множення важливий!
"""
import numpy as np
import matplotlib.pyplot as plt

# Вихідна фігура — квадрат одиничного розміру
square = np.array([
    [0, 1, 1, 0],  # координати x
    [0, 0, 1, 1]   # координати y
])

# Спочатку масштабуємо, потім обертаємо
S = np.array([[2, 0], [0, 0.5]])
R = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
              [np.sin(np.pi/4), np.cos(np.pi/4)]])

# Композиція: спочатку S, потім R
composite = R @ S

print("Композиція перетворень:")
print("1. Масштабування:")
print(S)
print("2. Обертання:")
print(R)
print("Результат R @ S:")
print(composite)

square_composite = composite @ square

# Виведення результату
print("\nПочатковий квадрат (рядки: x, y):")
print(square)
print("\nПісля перетворення:")
print(square_composite)