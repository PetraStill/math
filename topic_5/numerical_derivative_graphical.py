"""
Крок не можна робити нескінченно малим, адже тоді обчислення втратять точність 
через обмежену кількість бітів у числовому представленні.
Щоб переконатися в цьому, проведемо короткий експеримент і подивимося, 
як саме похибка змінюється залежно від величини h.
Ми поступово зменшуватимемо крок h у кілька разів і щоразу порівнюватимемо 
отриману чисельну похідну з аналітичною. Очікується, що для занадто великого h похибка буде значною, 
бо ми грубо наближаємо похідну.
Коли h стане меншим, наближення покращиться, але після певної межі похибка знову зросте 
через втрату точності при відніманні дуже близьких чисел. 
Цей ефект є класичним прикладом впливу машинної точності.
"""

import numpy as np
import matplotlib.pyplot as plt

def numerical_derivative(f, x, h):
    return (f(x + h) - f(x)) / h

f = np.sin
x_point = np.pi / 4
f_prime_analytic = np.cos(x_point)

# Перевіримо широкий діапазон значень h
h_values = np.logspace(-10, -1, 100)
errors = []

for h in h_values:
    f_prime_num = numerical_derivative(f, x_point, h)
    error = abs(f_prime_num - f_prime_analytic)
    errors.append(error)

plt.figure(figsize=(9, 5))
plt.loglog(h_values, errors, 'b-', linewidth=2)
plt.xlabel('Крок h')
plt.ylabel('Абсолютна похибка')
plt.title('Залежність похибки від кроку h (метод forward difference)')
plt.grid(True, which='both', alpha=0.3)
plt.show()
