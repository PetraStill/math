"""
У метода stats.norm параметри нормального розподілу задаються як loc та scale. 
Параметр scale це стандартне відхилення σ, loc - математичне сподівання μ.
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Створюємо нормальний розподіл N(100, 15^2)
mu = 100  # середнє
sigma = 15  # стандартне відхилення
norm_dist = stats.norm(loc=mu, scale=sigma)

# Числові характеристики
mean = norm_dist.mean()
variance = norm_dist.var()
std = norm_dist.std()

print(f"Нормальний розподіл N({mu}, {sigma}^2)")
print(f"Математичне сподівання: {mean} мс")
print(f"Дисперсія: {variance}")
print(f"Стандартне відхілення: {std} мс")
