import numpy as np

# Вектор ознак (наприклад, вік, зарплата, стаж)
features = np.array([35, 50000, 7])
print("Оригінальні ознаки:", features)
print("  Вік: 35 років")
print("  Зарплата: 50000 грн")
print("  Стаж: 7 років")

# Масштабування кожної ознаки до діапазону [0, 1]
# Для простоти припустимо максимальні значення
max_values = np.array([100, 200000, 40])
normalized = features / max_values

print("   Нормалізовані ознаки:", normalized)
print(f"  Вік: {normalized[0]:.2f} (35/100)")
print(f"  Зарплата: {normalized[1]:.2f} (50000/200000)")
print(f"  Стаж: {normalized[2]:.2f} (7/40)")
