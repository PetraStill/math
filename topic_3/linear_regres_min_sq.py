import numpy as np
import matplotlib.pyplot as plt

# Дані про квартири
np.random.seed(42)
area = np.array([32, 38, 45, 48, 52, 58, 61, 65, 70, 73, 
                 78, 82, 85, 88, 92, 95, 98, 102, 106, 110])

# Базова залежність: ціна ≈ 1.2 * площа + 15, плюс шум
price = 1.2 * area + 15 + np.random.normal(0, 5, size=len(area))

# Матриця A: перший стовпець - площа, другий - одиниці
A = np.column_stack([area, np.ones(len(area))])

b = price

print(f"Матриця A: {A}")
print(f"\nРозмір матриці A: {A.shape}")
print(f"Розмір вектора b: {b.shape}")

# Розв'язуємо МНК (методом найменших квадратів)
result = np.linalg.lstsq(A, b)
x_hat = result[0]
residuals = result[1]

a_opt = x_hat[0]
b_opt = x_hat[1] # коефіцієнт b – це базова ціна квартири. На практиці це інтерпретується як фіксовані витрати, не пов'язані з площею.

print(f"Оптимальні параметри:")
print(f"  a (коефіцієнт нахилу) = {a_opt:.4f} тис. дол./кв. м")
print(f"  b (зсув) = {b_opt:.4f} тис. дол.")

# Передбачення моделі
predictions = A @ x_hat

# Похибки
errors = b - predictions

print("Статистика похибок:")
print(f"  Середня абсолютна похибка: {np.mean(np.abs(errors)):.2f} тис. дол.")
print(f"  Максимальна похибка: {np.max(np.abs(errors)):.2f} тис. дол.")
print(f"  Стандартне відхилення похибок: {np.std(errors):.2f} тис. дол.")
print()

"""
Оцінка нової квартири за площею
"""

area_new = 75
price_predicted = a_opt * area_new + b_opt

print(f"Передбачення для квартири площею {area_new} кв.м²:")
print(f"  Очікувана ціна: {price_predicted:.2f} тис. дол.")