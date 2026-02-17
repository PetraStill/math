import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Визначаємо функцію
def f(x):
    return (x - 3)**2 + 2

# Знаходимо мінімум
result = minimize_scalar(f, bounds=(0, 6), method='bounded')

print("Результати оптимізації:")
print(f"Мінімум знайдено в точці: x = {result.x:.6f}")
print(f"Значення функції: f(x) = {result.fun:.6f}")
print(f"Успішність: {result.success}")
print(f"Кількість ітерацій: {result.nit}")
print(f"Повідомлення: {result.message}")
