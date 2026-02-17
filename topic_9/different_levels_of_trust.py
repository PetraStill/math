import numpy as np
from scipy import stats

# Та сама вибірка що і раніше
np.random.seed(42)
user_times = np.random.uniform(5, 55, 100)

sample_mean = np.mean(user_times)
sample_std = np.std(user_times, ddof=1)
n = len(user_times)
se = sample_std / np.sqrt(n)
degrees_of_freedom = n - 1

# Різні рівні довіри
confidence_levels = [0.90, 0.95, 0.99]

print(f"Вибіркове середнє: {sample_mean:.2f} хв")
print(f"Стандартна похибка: {se:.2f} хв\n")

for conf_level in confidence_levels:
    alpha = 1 - conf_level
    t_critical = stats.t.ppf(1 - alpha/2, degrees_of_freedom)
    margin_of_error = t_critical * se
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    width = upper_bound - lower_bound
    
    print(f"{int(conf_level*100)}% довірчий інтервал:")
    print(f"  Критичне значення t: {t_critical:.3f}")
    print(f"  Інтервал: [{lower_bound:.2f}, {upper_bound:.2f}] хв")
    print(f"  Ширина: {width:.2f} хв\n")
