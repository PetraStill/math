import numpy as np

# Дві матриці 2×3
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

print("Матриця A:")
print(A)
print("\nМатриця B:")
print(B)

# Додавання
C = A + B
print("\nA + B:")
print(C)

# Віднімання
D = A - B
print("\nA - B:")
print(D)

# Множення на скаляр
E = 3 * A
print("\n3 × A:")
print(E)

# Комбінована операція
F = 2*A + 3*B
print("\n2×A + 3×B:")
print(F)

# Dataset: 5 зразків, 3 ознаки
data = np.array([[170, 70, 25],
                 [165, 60, 30],
                 [180, 80, 22],
                 [175, 75, 28],
                 [160, 55, 35]])

print("Оригінальні дані:")
print(data)

# Обчислюємо середнє та стандартне відхилення по кожній ознаці
mean = data.mean(axis=0)  # shape (3,)
std = data.std(axis=0)    # shape (3,)

print(f"\nСереднє: {mean}")
print(f"Стандартне відхилення: {std}")

# Нормалізація: (data - mean) / std
# NumPy автоматично розширює mean та std 
normalized = (data - mean) / std

print("\nНормалізовані дані:")
print(normalized)

# Перевірка: середнє має бути ~0, std ~1
print(f"\nНове середнє: {normalized.mean(axis=0)}")
print(f"Нове std: {normalized.std(axis=0)}")
