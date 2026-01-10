import numpy as np

# Визначаємо два вектори у R^3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Виконуємо додавання
c = a + b

print("Вектор a:", a)
print("Вектор b:", b)
print("Сума a + b:", c)

# Базовий вектор
v = np.array([2, 3])

# Множення на різні скаляри
scalars = [0.5, 1, 2, -1]
results = {}

print("Множення вектора v = [2, 3] на різні скаляри: ")
for alpha in scalars:
    result = alpha * v
    results[alpha] = result
    print(f"  {alpha} × v = {result}")
