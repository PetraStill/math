"""
API отримує в середньому 3 запити в секунду. 
Час між сусідніми запитами має показовий (exponential) розподіл. 
Знайдіть середній час між запитами та ймовірність, 
що між двома запитами пройде більше чим 0.5 секунди.

!!!
В scipy параметр показового розподілу задається як scale = 1/λ, а не λ безпосередньо. 
Параметр scale у метода expon, це математичне сподівання 1/λ. 
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Створюємо показовий розподіл з λ = 3
lam = 3  # запити/сек
exp_dist = stats.expon(scale=1/lam)

# Числові характеристики
mean = exp_dist.mean()
variance = exp_dist.var()
std = exp_dist.std()

print(f"Показовий розподіл з λ = {lam} запити/сек")
print(f"Математичне сподівання: {mean:.4f} сек")
print(f"Дисперсія: {variance:.4f}")
print(f"Стандартне відхилення: {std:.4f} сек")

# Ймовірність P(T > 0.5)
prob_greater = 1 - exp_dist.cdf(0.5)
print(f"\nP(T > 0.5) = {prob_greater:.4f} або {prob_greater:.2%}")

# Генеруємо 1000 випадкових часів між запитами
samples = exp_dist.rvs(size=1000, random_state=42)

print(f"\nЗгенеровано {len(samples)} часів між запитами")
print(f"Середній час (дані): {np.mean(samples):.4f} сек")
print(f"Середній час (теорія): {mean:.4f} сек")
print(f"Стандартне відхилення (дані): {np.std(samples):.4f} сек")
print(f"Стандартне відхилення (теорія): {std:.4f} сек")

# Частка значень більше 0.5 сек
empirical_prob = np.mean(samples > 0.5)
print(f"\nЧастка T > 0.5 (дані): {empirical_prob:.2%}")
print(f"P(T > 0.5) (теорія): {prob_greater:.2%}")
