"""
Приклад коду для багатофакторної лінійної регресії (4 фічі + вільний член).
"""
import numpy as np

# Приклад даних (m спостережень)
# x1=площа, x2=поверх, x3=вік будинку, x4=відстань до центру
X = np.array([
    [32,  3, 10, 4.2],
    [45,  7,  5, 2.1],
    [55,  2, 30, 6.8],
    [70, 10,  2, 1.5],
    [90,  5, 15, 3.0],
], dtype=float)

# y = ціна (тис. дол.)
y = np.array([65, 95, 85, 140, 160], dtype=float)

m = X.shape[0]

# Матриця A: [x1 x2 x3 x4 1]
A = np.column_stack([X, np.ones(m)])

# МНК: A @ params ≈ y
params, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

a1, a2, a3, a4, b = params

print("Коефіцієнти:")
print(f"a1 (площа)    = {a1:.4f}")
print(f"a2 (поверх)   = {a2:.4f}")
print(f"a3 (вік)      = {a3:.4f}")
print(f"a4 (відстань) = {a4:.4f}")
print(f"b (зсув)      = {b:.4f}")

print("\nДіагностика:")
print(f"rank(A) = {rank}")
print(f"residuals = {residuals}")   # може бути порожнім залежно від задачі

# Прогноз для нової квартири
x_new = np.array([75, 6, 8, 2.5], dtype=float)
y_pred = np.dot(np.append(x_new, 1.0), params)

print(f"\nПрогноз для {x_new}: y ≈ {y_pred:.2f} тис. дол.")
