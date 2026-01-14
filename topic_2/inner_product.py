"""
Скалярний добуток (inner product; dot product) у NumPy можна обчислити кількома способами, 
але на практиці використовують два основних.
"""

import numpy as np

u = np.array([2, 3])
v = np.array([4, -1])

dot = np.dot(u, v) # 1 варіант

print(f"Скалярний добуток через np.dot(): {dot}")

dot1 = u @ v # 2 варіант
print(f"Скалярний добуток через @: {dot1}")

