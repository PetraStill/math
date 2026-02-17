import numpy as np
from scipy import stats

# Генеруємо дані: 100 користувачів
np.random.seed(42)
user_times = np.random.normal(32, 15, 100)

# Перевіряємо гіпотезу що μ = 30
mu_0 = 30

# Виконуємо одновибірковий t-test
t_statistic, p_value = stats.ttest_1samp(user_times, mu_0)

print(f"Вибіркове середнє: {np.mean(user_times):.2f} хв")
print(f"Вибіркове стандартне відхилення: {np.std(user_times, ddof=1):.2f} хв")
print(f"Розмір вибірки: {len(user_times)}")

print(f"\nТестова статистика: t = {t_statistic:.3f}")
print(f"p-value = {p_value:.4f}")

if p_value < 0.05:
    print(f"\nВисновок: відкидаємо H₀ (p < 0.05)")
    print(f"Середній час статистично значущо відрізняється від {mu_0} хв")
else:
    print(f"\nВисновок: не відкидаємо H₀ (p ≥ 0.05)")
    print(f"Немає достатніх доказів що середній час відрізняється від {mu_0} хв")
