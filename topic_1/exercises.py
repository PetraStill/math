import numpy as np

"""
task 1
"""
a = np.array([2, -3, 1])
b = np.array([1, 4, -2])

              
sum_ab = a + b
dif_ab = a - b
scalar = 3

multiply = a * scalar

print(sum_ab)
print(dif_ab)
print(multiply)

"""
task2
c1*e1 + c2*e2 = target
"""

e1 = np.array([1, 0])
e2 = np.array([0, 1])
target = np.array([5, -3])
c1 = np.dot(target, e1)
c2 = np.dot(target, e2)

result = c1*e1 + c2*e2
print(f"{c1} and {c2}")
print(np.allclose(target, result))
print("~" * 10)

"""
task3
Напишіть функцію is_collinear(u, v), яка приймає два вектори 
та повертає True, якщо вони колінеарні, і False в іншому випадку.
"""

def is_collinear(u, v):
    if u.shape == v.shape:
        if np.all(u == 0) and np.all(v == 0):
            return (True, "collinear")
        if np.all(u == 0) and np.any(v != 0):
            return (False, "not collinear")  
        idx = np.where(u != 0)[0][0]
        lam = v[idx] / u[idx]
        is_col = np.allclose(v, lam * u)
        if is_col:
            return (True, "collinear")
        else:
            return (False, "not collinear")
    else: 
        return (False, "different sizes")

u = np.array([3, -1])
v = np.array([6, 2])
print(is_collinear(u, v))

"""
Від chat GPT

def is_collinear(u, v):
    if u.shape != v.shape:
        return (False, "different sizes")

    u_zero = np.all(u == 0)
    v_zero = np.all(v == 0)

    if u_zero and v_zero:
        return (True, "both zero vectors")
    if u_zero and not v_zero:
        return (False, "u is zero, v is not")
    if v_zero and not u_zero:
        return (True, "v is zero vector")  # бо v = 0 * u

    idx = np.where(u != 0)[0][0]
    lam = v[idx] / u[idx]
    is_col = np.allclose(v, lam * u)

    return (is_col, "collinear" if is_col else "not collinear")

"""