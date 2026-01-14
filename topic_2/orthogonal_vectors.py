import numpy as np

# Приклад 1: Стандартні базисні вектори
e1 = np.array([1, 0, 0])
e2 = np.array([0, 1, 0])
e3 = np.array([0, 0, 1])

print("Стандартні базисні вектори:")
print(f"  e₁ = {e1}")
print(f"  e₂ = {e2}")
print(f"  e₃ = {e3}")
print(f"\ne₁ · e₂ = {e1 @ e2}")
print(f"e₁ · e₃ = {e1 @ e3}")
print(f"e₂ · e₃ = {e2 @ e3}")
print("\nУсі три вектори попарно ортогональні")

print("~" * 10)

"""
Наприклад, синус і косинус - це дві такі незалежні "форми" коливань. 
Вони ортогональні, тобто не впливають одна на одну. 
Якщо поєднати їх у різних пропорціях, ми отримаємо новий сигнал, 
але завжди можемо розділити його назад на частини, бо вони не змішуються.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)

signal_cos = np.cos(t)
signal_sin = np.sin(t)

# Перевірка ортогональності (інтеграл добутку ≈ 0)
orthogonality = np.trapezoid(signal_cos * signal_sin, t)
print(f"∫ cos(t)·sin(t) dt ≈ {orthogonality:.10f}")

# Створимо складний сигнал як суму двох ортогональних компонент
complex_signal = 3*signal_cos + 2*signal_sin

plt.figure(figsize=(10, 6))
plt.plot(t, complex_signal, 'g-', linewidth=2, label='3·cos(t) + 2·sin(t)')
plt.plot(t, signal_cos, 'b--', alpha=0.7, label='cos(t)')
plt.plot(t, signal_sin, 'r--', alpha=0.7, label='sin(t)')
plt.title('Складний сигнал як сума ортогональних компонент')
plt.xlabel('Час t')
plt.ylabel('Амплітуда')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
