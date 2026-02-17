import numpy as np
from scipy.integrate import solve_ivp

# Параметри задачі
T0 = 90  # початкова температура (°C)
T_room = 20  # кімнатна температура (°C)
k = 0.1  # коефіцієнт охолодження (1/хв)

# Диференціальне рівняння: dT/dt = -k(T - T_room)
def cooling(t, T):
    return -k * (T - T_room)

# Розв'язання задачі
t_span = (0, 30)  # інтервал часу від 0 до 30 хвилин
solution = solve_ivp(cooling, t_span, [T0], dense_output=True)

# Отримання значень температури в конкретні моменти часу
times = np.array([0, 5, 10, 15, 20, 25, 30])
temperatures = solution.sol(times)[0]

print("Час (хв) | Температура (°C)")
print("-" * 30)
for t, temp in zip(times, temperatures):
    print(f"{t:8.1f} | {temp:16.2f}")
