import numpy as np

# Створюємо матрицю 3×2
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

print("Оригінальна матриця A (3×2):")
print(A)

# Транспонуємо
A_T = A.T

print("\nТранспонована A^T (2×3):")
print(A_T)

print(f"\nРозмірність A: {A.shape}")
print(f"Розмірність A^T: {A_T.shape}")

# Dataset: 3 студенти, 4 предмети
grades = np.array([
    [85, 90, 78, 92],  # студент 0
    [88, 85, 91, 87],  # студент 1
    [92, 89, 85, 90]   # студент 2
])

print("Оригінальний dataset (студенти × предмети):")
print(grades)
print(f"Розмірність: {grades.shape}")

# Транспонуємо: тепер рядки — предмети, стовпці — студенти
grades_T = grades.T

print("\nТранспонований dataset (предмети × студенти):")
print(grades_T)
print(f"Розмірність: {grades_T.shape}")

# Тепер легко обчислити середній бал по кожному предмету
print("\nСередній бал по предметах:")
for i, avg in enumerate(grades_T.mean(axis=1)):

    print(f"  Предмет {i+1}: {avg:.1f}")


# Вектор-рядок
v_row = np.array([[1, 2, 3, 4]])
print(f"Вектор-рядок shape: {v_row.shape}")
print(v_row)

# Транспонуємо у вектор-стовпець
v_col = v_row.T
print(f"\nВектор-стовпець shape: {v_col.shape}")
print(v_col)