import pandas as pd
import numpy as np

# Dataset: 5 людей, 3 ознаки (зріст, вага, вік)
data = np.array([
    [170, 70, 25],  # людина 0
    [165, 60, 30],  # людина 1
    [180, 80, 22],  # людина 2
    [175, 75, 28],  # людина 3
    [160, 55, 35]   # людина 4
])

# Створюємо DataFrame з іменованими стовпцями
df = pd.DataFrame(data, columns=['Зріст (см)', 'Вага (кг)', 'Вік (роки)'])

print("DataFrame:")
print(df)

# Статистика по кожній ознаці
print("\nОписова статистика:")
print(df.describe())

"""
Як у прикладі вище NumPy-матриця перетворюється в DataFrame, 
так і NumPy-матрицю ми можемо отримати назад:
"""
numpy_array = df.to_numpy()
print("NumPy-масив з DataFrame:")
print(numpy_array)
print(f"Тип: {type(numpy_array)}")
