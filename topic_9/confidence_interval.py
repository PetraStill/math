import numpy as np
from scipy import stats

# Генеруємо дані для прикладу
np.random.seed(42)
user_times = np.random.uniform(5, 55, 100)  

# Крок 1: Рахуємо вибіркове середнє
sample_mean = np.mean(user_times)
print(f"Вибіркове середнє: {sample_mean:.2f} хв")

# Крок 2: Рахуємо вибіркове стандартне відхилення
# ddof=1 означає ділимо на (n-1) замість n
sample_std = np.std(user_times, ddof=1)
print(f"Вибіркове стандартне відхилення: {sample_std:.2f} хв")

# Крок 3: Рахуємо розмір вибірки
n = len(user_times)
print(f"Розмір вибірки: {n}")

# Крок 4: Рахуємо стандартну похибку
# sqrt – square root (квадратний корінь)
se = sample_std / np.sqrt(n)
print(f"Стандартна похибка SE = {se:.2f} хв")

# Крок 5: Знаходимо критичне значення t
# Для 95% довірчого інтервалу alpha = 0.05
confidence_level = 0.95
alpha = 1 - confidence_level
degrees_of_freedom = n - 1

# stats.t.ppf знаходить значення t, яке залишає задану ймовірність зліва
# Нам потрібно залишити 2.5% справа, тобто 97.5% зліва
t_critical = stats.t.ppf(1 - alpha/2, degrees_of_freedom)

print(f"\nКритичне значення t для {confidence_level*100}% довірчого інтервалу:")
print(f"Ступені свободи: {degrees_of_freedom}")
print(f"t-критичне: {t_critical:.3f}")

# Крок 6: Будуємо довірчий інтервал
margin_of_error = t_critical * se
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print(f"\n{confidence_level*100}% довірчий інтервал для середнього часу:")
print(f"Вибіркове середнє ± похибка: {sample_mean:.2f} ± {margin_of_error:.2f}")
print(f"Інтервал: [{lower_bound:.2f}, {upper_bound:.2f}] хв")
print(f"Ширина інтервалу: {upper_bound - lower_bound:.2f} хв")

print("~" * 20)
# Генеруємо велику генеральну сукупність
np.random.seed(42)
population = np.random.uniform(5, 55, 100000)

# Різні розміри вибірки
sample_sizes = [30, 100, 500, 1000]
confidence_level = 0.95

print("Ширина 95% довірчого інтервалу для різних розмірів вибірки:\n")

for n in sample_sizes:
    sample = np.random.choice(population, size=n, replace=False)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    se = sample_std / np.sqrt(n)
    
    degrees_of_freedom = n - 1
    t_critical = stats.t.ppf(0.975, degrees_of_freedom)
    margin_of_error = t_critical * se
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    width = upper_bound - lower_bound
    
    print(f"n = {n:4d}: [{lower_bound:.2f}, {upper_bound:.2f}], ширина = {width:.2f} хв")
