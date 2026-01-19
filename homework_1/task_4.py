"""
Задача 4. Прогноз тренду

Дано виміри завантаження CPU y протягом 5 годин t:
    Час t=[1,2,3,4,5]
    Навантаження y=[22,28,37,45,53]
"""

import numpy as np

# Ініціалізуємо вектори і створюємо матрицю
t = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([22, 28, 37, 45, 53], dtype=float)
A = np.column_stack([t, np.ones_like(t)])

print("Матриця A:\n", A)
print("Вектор y:\n", y)

# МНК: знаходимо коефіцієнти k i b – coefficient
coefficient, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)
k, b = coefficient

print("Коефіцієнти:")
print(f"k    = {k:.4f}")
print(f"b   = {b:.4f}")

# Робимо прогноз на шосту годину y^=k⋅6+b
y6 = k * 6 + b

print("\nРівняння тренду: y_hat = {:.4f} * t + {:.4f}".format(k, b))
print("Прогноз на шосту годину: y_hat(6) =", y6)

