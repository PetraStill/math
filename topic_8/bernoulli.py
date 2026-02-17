from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Створюємо розподіл Бернуллі з p = 0.08
p = 0.08
bernoulli_dist = stats.bernoulli(p)

# Обчислюємо числові характеристики
mean = bernoulli_dist.mean()
variance = bernoulli_dist.var()
std = bernoulli_dist.std()

print(f"Розподіл Бернуллі з p = {p}")
print(f"Математичне сподівання: {mean}")
print(f"Дисперсія: {variance:.4f}")
print(f"Стандартне відхілення: {std:.4f}")

# PMF для обох можливих значень
print(f"\nФункція маси ймовірності:")
print(f"P(X = 0) = {bernoulli_dist.pmf(0):.2f}")
print(f"P(X = 1) = {bernoulli_dist.pmf(1):.2f}")

# Генеруємо 1000 випадкових спроб Бернуллі
samples = bernoulli_dist.rvs(size=1000, random_state=42)

# Підраховуємо частоти
unique, counts = np.unique(samples, return_counts=True)
frequencies = counts / len(samples)

print(f"\nЗгенеровано {len(samples)} спроб")
print(f"Кількість 0: {counts[0]} ({frequencies[0]:.1%})")
print(f"Кількість 1: {counts[1]} ({frequencies[1]:.1%})")
print(f"Теоретично очікували: 0 = {1-p:.1%}, 1 = {p:.1%}")
