"""
Приклад показує як числові характеристики працюють разом. 
    Середнє дає загальну картину, 
    медіана показує типовий випадок, 
    стандартне відхилення вимірює стабільність, 
    а квантилі показують як поводяться крайні випадки. 
Для прийняття рішень потрібні всі ці метрики, не лише середнє.
"""

import numpy as np
import matplotlib.pyplot as plt

# Генеруємо 1000 вимірювань часу відповіді (в мілісекундах)
np.random.seed(42)
response_times = np.random.lognormal(mean=4.5, sigma=0.5, size=1000)

print(f"Зібрано {len(response_times)} вимірювань часу відповіді")
print(f"Мінімальний час: {np.min(response_times):.2f} мс")
print(f"Максимальний час: {np.max(response_times):.2f} мс")

# Математичне сподівання
mean = np.mean(response_times)

# Дисперсія
variance = np.var(response_times)

# Стандартне відхилення
std = np.std(response_times)

# Медіана - 0.5-квантіль
median = np.median(response_times)

# Квантілі
q25 = np.percentile(response_times, 25)
q75 = np.percentile(response_times, 75)
q95 = np.percentile(response_times, 95)
q99 = np.percentile(response_times, 99)

print("\n=== Числові характеристики ===")
print(f"Математичне сподівання (середнє): {mean:.2f} мс")
print(f"Медіана: {median:.2f} мс")
print(f"Дисперсія: {variance:.2f}")
print(f"Стандартне відхилення: {std:.2f} мс")
print(f"\n=== Квантілі (перцентилі) ===")
print(f"25-й перцентиль (Q1): {q25:.2f} мс")
print(f"75-й перцентиль (Q3): {q75:.2f} мс")
print(f"95-й перцентиль: {q95:.2f} мс")
print(f"99-й перцентиль: {q99:.2f} мс")
