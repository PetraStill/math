import numpy as np
from scipy.integrate import solve_ivp

# Параметри задачі
N0 = 10  # початкова кількість переглядів
r = 0.5  # швидкість розповсюдження
K = 10000  # максимальна аудиторія

# Диференціальне рівняння: dN/dt = r * N * (1 - N/K)


def viral_spread(t, N):
    return r * N * (1 - N / K)


# Розв'язання задачі
t_span = (0, 20)  # інтервал часу від 0 до 20 годин
solution = solve_ivp(viral_spread, t_span, [N0], dense_output=True)

# Отримання значень у конкретні моменти часу
times = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
views = solution.sol(times)[0]

print("Час (год) | Кількість переглядів")
print("-" * 35)
for t, n in zip(times, views):
    print(f"{t:9.0f} | {n:20.0f}")

# Час до досягнення різних рівнів охоплення
times_dense = np.linspace(0, 20, 1000)
views_dense = solution.sol(times_dense)[0]

for threshold in [0.1, 0.5, 0.9]:
    idx = np.argmax(views_dense >= threshold * K)
    if idx > 0:
        print(
            f"{int(threshold*100)}% аудиторії досягнуто за {times_dense[idx]:.2f} годин")
