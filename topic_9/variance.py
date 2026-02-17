import numpy as np

# Припустимо, ми зібрали дані про 1000 користувачів
# Час у застосунку в хвилинах

data = np.random.uniform(10, 60, 1000)  # для прикладу генеруємо випадкові дані

# Вибіркове середнє
sample_mean = np.mean(data)
print(f"Вибіркове середнє: {sample_mean:.2f} хвилин")

# Вибіркова дисперсія
# ddof=1 означає "ділимо на n-1"
# ddof розшифровується як Delta Degrees Of Freedom.
# Degrees of freedom (ступені свободи) — це кількість незалежних значень, 
# які залишаються після оцінювання параметрів.
sample_variance = np.var(data, ddof=1)
print(f"Вибіркова дисперсія: {sample_variance:.2f} хвилин²")

# Стандартне відхилення
# std – standard deviation – квадратний корінь із дисперсії.
# Функція np.std(data, ddof=1) рахує стандартне відхилення - це еквівалентно np.sqrt(np.var(data, ddof=1))
# sqrt – square root (квадратний корінь)
sample_std = np.std(data, ddof=1)
print(f"Стандартне відхилення: {sample_std:.2f} хвилин")
