import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

# Генеруємо дані
np.random.seed(42)
n = 100

age = np.random.uniform(18, 65, n)
time_in_app = 10 + 0.5 * age + np.random.normal(0, 8, n)

correlation, p_value = stats.pearsonr(age, time_in_app)

print(f"Коефіцієнт кореляції Пірсона: r = {correlation:.3f}")
print(f"p-value: {p_value:.4f}")

X = age.reshape(-1, 1)
y = time_in_app

model = LinearRegression()
model.fit(X, y)

beta_0 = model.intercept_
beta_1 = model.coef_[0]

print(f"Коефіцієнти регресії:")
print(f"intercept = {beta_0:.2f}")
print(f"slope = {beta_1:.3f}")
print(f"\nРівняння: ŷ = {beta_0:.2f} + {beta_1:.3f} * x")

r_squared = model.score(X, y)

print(f"Коефіцієнт детермінації: R² = {r_squared:.5f}")
print(f"Модель пояснює {r_squared*100:.1f}% варіації даних")
print(f"\nДля простої лінійної регресії R² має дорівнювати r² = {correlation**2:.3f}")

new_age = 40
new_age_array = np.array([[new_age]])
predicted_time = model.predict(new_age_array)[0]

print(f"Передбачення для користувача віком {new_age} років:")
print(f"Очікуваний час у застосунку: {predicted_time:.1f} хв")

y_predicted_all = model.predict(X)
residuals = y - y_predicted_all
residual_std = np.std(residuals, ddof=1)

print(f"\nСтандартне відхилення залишків: {residual_std:.2f} хв")
print(f"Типова похибка передбачення: ±{residual_std:.2f} хв")
print(f"Тобто реальне значення ймовірно від {predicted_time - residual_std:.1f} до {predicted_time + residual_std:.1f} хв")
