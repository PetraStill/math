"""
Задача 9: чисельне обчислення частинних похідних (forward difference)
Forward difference — це спосіб чисельно наблизити похідну, 
дивлячись вперед від поточної точки.
"""

# Функція
def f(x, y):
    return x**2 + y**2

# Точка і крок
x0, y0 = 1.0, 2.0
h = 0.001

# Базове значення
f0 = f(x0, y0)

# 1) Чисельне наближення ∂f/∂x (forward difference)
df_dx_num = (f(x0 + h, y0) - f0) / h

# 2) Чисельне наближення ∂f/∂y (forward difference)
df_dy_num = (f(x0, y0 + h) - f0) / h

# 3) Аналітичні значення (бо f = x^2 + y^2)
# ∂f/∂x = 2x, ∂f/∂y = 2y
df_dx_anal = 2 * x0
df_dy_anal = 2 * y0

# Похибки
err_x = abs(df_dx_num - df_dx_anal)
err_y = abs(df_dy_num - df_dy_anal)

print("Точка (x0, y0) =", (x0, y0))
print("Крок h =", h)
print()

print("∂f/∂x(1,2):")
print(f"  чисельно     = {df_dx_num:.6f}")
print(f"  аналітично   = {df_dx_anal:.6f}")
print(f"  |похибка|    = {err_x:.6e}")
print()

print("∂f/∂y(1,2):")
print(f"  чисельно     = {df_dy_num:.6f}")
print(f"  аналітично   = {df_dy_anal:.6f}")
print(f"  |похибка|    = {err_y:.6e}")
