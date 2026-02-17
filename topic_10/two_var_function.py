import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Визначаємо функцію двох змінних
def f_2d(x):
    return x[0]**2 + 2*x[1]**2 - 2*x[0] - 8*x[1] + 10

# Початкова точка пошуку
x0 = np.array([0.0, 0.0])

# Знаходимо мінімум методом BFGS
result = minimize(f_2d, x0, method='BFGS')

print("Результати оптимізації:")
print(f"Мінімум знайдено в точці: x1 = {result.x[0]:.6f}, x2 = {result.x[1]:.6f}")
print(f"Значення функції: f(x) = {result.fun:.6f}")
print(f"Успішність: {result.success}")
print(f"Кількість ітерацій: {result.nit}")
print(f"Кількість обчислень функції: {result.nfev}")
