import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def f_complex(x):
    return np.sin(x) + 0.1*x

# Знаходимо мінімум
result = minimize_scalar(f_complex, bounds=(0, 15), method='bounded')

print("Результати оптимізації:")
print(f"Мінімум знайдено в точці: x = {result.x:.6f}")
print(f"Значення функції: f(x) = {result.fun:.6f}")
