"""
Задача 2. Пошук схожих фільмів
"""
import numpy as np

# Ініціалізуємо вектори user та movies
user = np.array([8, 2, 5])
a_action_movie = np.array([9, 1, 2])
b_comedy_movie = np.array([1, 9, 8])
c_drama_movie = np.array([7, 2, 6])

# Обчислюємо скалярні добутки вектора user і векторів фільмів
dot_product_action = user @ a_action_movie
dot_product_comedy = user @ b_comedy_movie
dot_product_drama = user @ c_drama_movie

# Обчислюємо норми векторів
norm_user = np.linalg.norm(user)
norm_a_action_movie = np.linalg.norm(a_action_movie)
norm_b_comedy_movie = np.linalg.norm(b_comedy_movie)
norm_c_drama_movie = np.linalg.norm(c_drama_movie)

# Обчислюємо косинусну подібність
cos_action = dot_product_action / (norm_user * norm_a_action_movie)
cos_comedy = dot_product_comedy / (norm_user * norm_b_comedy_movie)
cos_drama = dot_product_drama / \
    (norm_user * norm_c_drama_movie)  # <-- виправлено

scores = {
    "A (Action Movie)": cos_action,
    "B (Comedy Movie)": cos_comedy,
    "C (Drama Movie)":  cos_drama
}

# Виводимо найбільш схожі фільми
for name, score in scores.items():
    print(f"{name}: {score:.4f}")

best_movie = max(scores, key=scores.get)
print(
    f"\nНайкраща рекомендація: {best_movie} (score={scores[best_movie]:.4f})")
