import numpy as np

# Матриця, у якій другий рядок — це подвоєний перший
A = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 1]
])

print("Матриця A:")
print(A)
print(f"\nРозмір матриці: {A.shape[0]} × {A.shape[1]}")

rank = np.linalg.matrix_rank(A)
print(f"Ранг матриці: {rank}")
