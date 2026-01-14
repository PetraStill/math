import numpy as np

# Одиничні вектори вздовж осей координат
e1 = np.array([1, 0])  # одиничний вектор по осі x
e2 = np.array([0, 1])  # одиничний вектор по осі y

# Довільний вектор
target = np.array([3, 2])

# Представлення через одиничні вектори
result = 3*e1 + 2*e2

print("Одиничні вектори вздовж осей:")
print(f"  e₁ = {e1} (вздовж осі x)")
print(f"  e₂ = {e2} (вздовж осі y)")
print(f"Цільовий вектор: {target}")
print(f"Лінійна комбінація:")
print(f"  3×e₁ + 2×e₂ = 3×{e1} + 2×{e2} = {result}")
print(f"Перевірка: {np.array_equal(result, target)}")
