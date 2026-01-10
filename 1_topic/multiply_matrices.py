import numpy as np

# Матриці з прикладу
A = np.array([[1, 2, 3],
       [4, 5, 6]]) # 2×3

B = np.array([[7, 8],
       [9, 10],
       [11, 12]])  # 3×2

D = np.array([[3, 7],
              [5, 9]]) # 2x2

F = np.array([[2, 8],
              [6, 10]]) # 2x2

# Множення A @ B
C = A @ B

print("Матриця A (2×3):")
print(A)
print("\nМатриця B (3×2):")
print(B)
print(f"\nРезультат C = A @ B ({C.shape[0]}×{C.shape[1]}):") # A.shape — це властивість (property); повертає кортеж розмірів: (рядки, стовпці)
print(C)


def safe_check_matrices(name, fn):
    try:
        left, right = fn()
        print("\n" + name)
        print("LEFT:")
        print(left)
        print("RIGHT:")
        print(right)
        print("allclose:", np.allclose(left, right))
    except ValueError as e:
        print("\n" + name, "— не вийшло через розміри:", e)


# Асоціативність: (AB)C=A(BC)

safe_check_matrices("Асоціативність (A @ B) @ D, A @ (B @ D)", 
                    lambda: ((A @ B) @ D, A @ (B @ D)))


# Дистрибутивність відносно додавання: A(B+C)=AB+AC

safe_check_matrices("Дистрибутивність (A @ (B + D), A @ B + A @ D)", 
                    lambda: (A @ (B + D), A @ B + A @ D))
safe_check_matrices("Дистрибутивність (B @ (D + F), B @ D + B @ F)", 
                    lambda: (B @ (D + F), B @ D + B @ F))

# Властивість транспонування (AB)^T=B^TA^T

safe_check_matrices("Транспонування ((A@B).T == B.T@A.T)",
           lambda: ((A @ B).T, B.T @ A.T))