"""
Початкова задача максимізувати z=3x+2y за умов:
    x + 2y ≤ 8
    3x + 2y ≤ 12
    x ≥ 0, y ≥ 0
"""

from scipy.optimize import linprog

# Мінімізуємо: -3x - 2y
c = [-3, -2]

# Обмеження: Ax <= b
A = [
    [1, 2],
    [3, 2]
]
b = [8, 12]

# Обмеження на змінні: x ≥ 0, y ≥ 0
bounds = [(0, None), (0, None)]

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

print("Статус:", res.message)
print("Оптимальне значення:", -res.fun)
print("Оптимальне розв'язання:", res.x)
