from scipy.spatial import distance
import numpy as np

A = np.array([2, 3])
B = np.array([5, 7])

# Різниця векторів
diff = B - A
print(f"Точка A: {A}")
print(f"Точка B: {B}")
print(f"Різниця B - A: {diff}")

# Різні відстані
d_L2 = np.linalg.norm(diff, ord=2)
d_L1 = np.linalg.norm(diff, ord=1)
d_Linf = np.linalg.norm(diff, ord=np.inf)

print(f"\nЕвклідова відстань: {d_L2:.2f}")
print(f"Мангеттенська відстань: {d_L1:.2f}")
print(f"Чебишова відстань: {d_Linf:.2f}")

print("~" * 20)
print("from scipy.spatial import distance")
"""
Для багатьох точок зручно використовувати готові функції 
з бібліотеки scipy.spatial.distance, де реалізовано всі основні метрики.
"""


# Різні метрики через scipy
euclidean = distance.euclidean(A, B)
manhattan = distance.cityblock(A, B)  # cityblock = Manhattan
chebyshev = distance.chebyshev(A, B)  # Chebyshev

print(f"Евклідова: {euclidean:.2f}")
print(f"Мангеттенська: {manhattan:.2f}")
print(f"Чебишова: {chebyshev:.2f}")
