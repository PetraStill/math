"""
Якщо ми складемо матрицю з наших векторів як стовпців, 
то її ранг покаже, скільки серед них незалежних.
"""
import numpy as np

# Три вектори в R²
v1 = np.array([1, 0])
v2 = np.array([0, 1])
v3 = np.array([2, 3])

# Складаємо матрицю з векторів як стовпців
A = np.column_stack([v1, v2, v3])
print("Матриця з векторів v1, v2, v3:")
print(A)

rank = np.linalg.matrix_rank(A)
print(f"\nРанг матриці: {rank}")
print(f"Кількість векторів: {A.shape[1]}")

if rank < A.shape[1]:
    print(f"Вектори лінійно залежні")
    print(f"Лінійно незалежних серед них: {rank}")
else:
    print(f"Вектори лінійно незалежні")

print("~" * 20)
# Лише перші два вектори
A2 = np.column_stack([v1, v2])
rank2 = np.linalg.matrix_rank(A2)
print(f"\nМатриця з v1 та v2:")
print(A2)
print(f"Ранг: {rank2}")
print(f"Кількість векторів: {A2.shape[1]}")