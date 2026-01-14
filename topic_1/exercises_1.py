import numpy as np

"""task 1"""
# 4×3 матриця з довільними цілими числами
A = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9],
    [10, 11, 12]
])

# 1) Розмірність матриці
print("Розмірність (shape):", A.shape)

# 2) Елемент на позиції (2, 3)
# У NumPy індексація з 0, тому (2,3) у людському сенсі = A[1,2]
print("Елемент (2,3):", A[1, 2])

# 3) Другий рядок
print("Другий рядок:", A[1])

# 4) Третій стовпець
print("Третій стовпець:", A[:, 2])

"""task 2"""

A1 = np.array([
    [1,  2,  3],
    [4,  5,  6]
])

A1_T = A1.T
print("\n Оригінальна матриця A1:")
print(A1)
print("\nТранспонована A1^T (3×2):")
print(A1_T)
print("(A1^T)^T = A1", np.array_equal(A1_T.T, A1))

"""task 3"""

B = np.random.randint(1, 11, (3, 3))
C = np.random.randint(1, 11, (3, 3))

adding = B + C
subtracting = B - C
alfa = 4
multiply = alfa * B
combination = 2 * B + 3 * C

print("Матриця B:")
print(B)
print("Матриця C:")
print(C)
print("Додавання B та C:\n", adding)
print("Віднімання В та С:\n", subtracting)
print("Множення матриці В на скаляр 4:\n", multiply)
print("Лінійна комбінація 2*B + 3*C:\n", combination)
