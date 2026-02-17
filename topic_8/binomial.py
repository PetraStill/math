"""
Розглянемо приклад A/B тесту. 
Нова версія кнопки на сайті має коефіцієнт конверсії 12%. 
Показуємо її 500 користувачам. Скільки конверсій ми очікуємо? 
Знайдемо математичне сподівання, дисперсію та ймовірність отримати рівно 60 конверсій.

"""

from scipy import stats
import numpy as np

n = 500     # к-сть користувачів
p = 0.12    # ймовірність, припущення
k = 60      # конверсія 

# Створюємо біноміальний розподіл
binom_dist = stats.binom(n, p)

# Ймовірність рівно k успіхів
prob_k = binom_dist.pmf(k)

print(f"Біноміальний розподіл: n = {n}, p = {p}")
print(f"P(X = {k}) = {prob_k:.4f}")

# Числові характеристики
mean = binom_dist.mean()
variance = binom_dist.var()
std = binom_dist.std()

print(f"\nЧислові характеристики:")
print(f"Математичне сподівання: {mean} (теоретично: {n*p})")
print(f"Дисперсія: {variance} (теоретично: {n*p*(1-p)})")
print(f"Стандартне відхилення: {std:.2f} (теоретично: {np.sqrt(n*p*(1-p)):.2f})")

# Квантилі
median = binom_dist.median()
q25 = binom_dist.ppf(0.25)
q75 = binom_dist.ppf(0.75)

print(f"\nКвантилі:")
print(f"Медіана: {median}")
print(f"25-й перцентиль: {q25}")
print(f"75-й перцентиль: {q75}")

# Ймовірність інтервалу P(55 <= X <= 65)
prob_interval = binom_dist.cdf(65) - binom_dist.cdf(54)

print(f"\nP(55 <= X <= 65) = {prob_interval:.4f}")

# Альтернативно: сума ймовірностей
prob_sum = sum(binom_dist.pmf(k) for k in range(55, 66))
print(f"Перевірка через суму: {prob_sum:.4f}")
