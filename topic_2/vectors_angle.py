import numpy as np

# Два вектори на площині
u = np.array([3, 4])
v = np.array([4, 3])

# Обчислюємо скалярний добуток та норми
dot_product = u @ v
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

# Косинус кута
cos_theta = dot_product / (norm_u * norm_v)

# Кут у радіанах та градусах
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

print(f"Вектор u: {u}, норма: {norm_u:.2f}")
print(f"Вектор v: {v}, норма: {norm_v:.2f}")
print(f"\nСкалярний добуток u·v: {dot_product}")
print(f"cos(θ) = {cos_theta:.4f}")
print(f"Кут θ = {theta_rad:.4f} радіан або {theta_deg:.2f} градусів")
