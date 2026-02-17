"""
Задача 3: оптимальний план виробництва (лінійне програмування).
Максимізуємо прибуток P(x, y) = 500x + 800y за обмежень ресурсів.
Оскільки linprog мінімізує, мінімізуємо -P(x, y).
"""

import numpy as np
from scipy.optimize import linprog

# 1) Ініціалізуємо коефіцієнти цільової функції для мінімізації:
# мінімізуємо -500x - 800y
c = np.array([-500, -800])

# 2) Ініціалізуємо матрицю обмежень A_ub та вектор b_ub:
# 2x + 4y <= 120  (деревина)
# 3x + 2y <= 90   (робочий час)
A_ub = np.array([
    [2, 4],
    [3, 2]
])
b_ub = np.array([120, 90])

# 3) Ініціалізуємо межі змінних (невід’ємність)
bounds = [(0, None), (0, None)]  # x >= 0, y >= 0

# 4) Запускаємо linprog
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

# 5) Витягуємо оптимальні x, y та максимальний прибуток
x_opt, y_opt = res.x
profit_max = 500 * x_opt + 800 * y_opt

# 6) Рахуємо використання ресурсів та залишки
wood_used = 2 * x_opt + 4 * y_opt
time_used = 3 * x_opt + 2 * y_opt

wood_left = 120 - wood_used
time_left = 90 - time_used

print("Оптимальний план:")
print("x (стільці) =", x_opt)
print("y (столи)   =", y_opt)
print("Максимальний прибуток =", profit_max)
print()

print("\nРесурси:")
print("Деревина використано =", wood_used, "| залишок =", wood_left)
print("Час використано      =", time_used, "| залишок =", time_left)
print()

if abs(wood_left) < 1e-9 and abs(time_left) < 1e-9:
    print("\nВисновок: обидва ресурси використані повністю.")
else:
    print("\nВисновок: є залишок ресурсів (див. значення вище).")

print("\nУспіх:", res.success, "| Повідомлення:", res.message)
