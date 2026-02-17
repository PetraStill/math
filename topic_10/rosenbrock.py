import numpy as np
from scipy.optimize import minimize

def rosenbrock(x):
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

# Початкова точка
x0 = np.array([0.0, 0.0])

# Методи для порівняння
methods = ['BFGS', 'Nelder-Mead', 'CG', 'Powell']

print("Порівняння методів оптимізації функції Розенброка:\n")
print(f"{'Метод':<15} {'x1':>10} {'x2':>10} {'f(x)':>12} {'Ітерації':>10} {'Обчислень':>11}")
print("-" * 75)

for method in methods:
    result = minimize(rosenbrock, x0, method=method)
    print(f"{method:<15} {result.x[0]:>10.6f} {result.x[1]:>10.6f} "
          f"{result.fun:>12.10f} {result.nit:>10} {result.nfev:>11}")
