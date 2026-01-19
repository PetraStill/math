import numpy as np

A1 = np.array([[3, 1], [0, 2]], dtype=float)

# Обчислюємо власні значення та власні вектори
eigenvalues, eigenvectors = np.linalg.eig(A1)

print("Власні значення λ:")
print(eigenvalues)
print("\nВласні вектори (стовпці матриці):")
print(eigenvectors)
print("~" * 20)

"""
Знайдемо власні значення та власні вектори
"""

A = np.array([[2, 1], [1, 2]], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Власні значення:")
print(eigenvalues)
print("\nВласні вектори:")
print(eigenvectors)

v1 = eigenvectors[:, 0] # Перший стовпець
v2 = eigenvectors[:, 1] # Другий стовпець
lambda1 = eigenvalues[0]
lambda2 = eigenvalues[1]

print(f"\nλ₁ = {lambda1:.4f}, v₁ = [{v1[0]:.4f}, {v1[1]:.4f}]")
print(f"λ₂ = {lambda2:.4f}, v₂ = [{v2[0]:.4f}, {v2[1]:.4f}]")
print("~" * 20)

"""
Ця матриця обертає всі існуючи вектори.
У виведенні NumPy позначає уявну одиницю як j, тому результат виглядає як 1.j та -1.j. 
Для матриці обертання в дійсному просторі не існує дійсних власних векторів. 
Жоден дійсний вектор не залишається на своєму напрямку при повороті.
"""

R = np.array([[0, -1], [1, 0]], dtype=complex)

eigenvalues, eigenvectors = np.linalg.eig(R)

print("Власні значення:")
print(eigenvalues)
print("\nВласні вектори:")
print(eigenvectors)
