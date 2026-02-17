import numpy as np
from scipy.optimize import approx_fprime

# Функція
def f(x):
    """Функція для диференціювання"""
    return np.sin(x[0])  # x — це масив, беремо перший елемент

x_point = np.array([np.pi / 4])  # Обгортаємо в масив

# Чисельна похідна через SciPy
# epsilon — крок для обчислення похідної
f_prime_scipy = approx_fprime(x_point, f, epsilon=1e-5)[0]

# Аналітична похідна
f_prime_analytic = np.cos(np.pi / 4)

print(f"Аналітична похідна: {f_prime_analytic:.10f}")
print(f"SciPy похідна: {f_prime_scipy:.10f}")
print(f"Похибка: {abs(f_prime_analytic - f_prime_scipy):.2e}")


"""
Якщо ваша функція вже написана та приймає скаляр, а не масив, 
можна створити просту обгортку, яка перетворює масив у скаляр перед викликом функції.
"""

from scipy.optimize import approx_fprime

# Функція, що приймає скаляр
def f_scalar(x):
    return np.sin(x)

# Обгортка для approx_fprime
def f_vector(x):
    return f_scalar(x[0])

x_point = np.array([np.pi / 4])
f_prime = approx_fprime(x_point, f_vector, epsilon=1e-5)[0]

print(f"Похідна: {f_prime:.10f}")
