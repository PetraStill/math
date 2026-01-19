"""
Так само як в арифметиці, в булевій логіці операції мають свій порядок виконання.
Розташуємо логічні операції за пріоритетом від найвищого до найнижчого:
1. Заперечення (¬
    ¬, NOT) — найвищий пріоритет
2. Кон‘юнкція (∧
    ∧, AND) — наступна
3. Диз’юнкція (∨
    ∨, OR) та виключне АБО (⊕
    ⊕, XOR) — найнижчий пріоритет
"""


p = True
q = False
r = True

# Без дужок - Python дотримується пріоритетів
result = not p and q or r   # ¬p∧q∨r
print(f"not p and q or r = {result}") # 1 not p → False; 2 False and q → False; 3 False or r → True

# Вираз A: p∧q∨r
# Вираз B: p∧(q∨r)

p = False
q = False
r = True

# Вираз A: p and q or r
expr_A = p and q or r
print(f"p and q or r = {expr_A}")

# Вираз B: p and (q or r)
expr_B = p and (q or r)
print(f"p and (q or r) = {expr_B}")
print("~" * 20)

"""
Закони
    Закони нейтрального елемента.
    Закони домінування.
    Закон поглинання. 
"""

# Приклад нейтрального елемента
# True (істина) є нейтральним елементом для and,
# False (хиба) — нейтральним елементом для or.

email_verified = True

expr_and = True and email_verified
expr_or = False or email_verified

print("True AND p:", expr_and)
print("False OR p:", expr_or)
print("~" * 20)

# Приклад закону домінування
# True домінує в or → результат завжди True
# False домінує в and → результат завжди False
has_permission = False

check_or = has_permission or True
check_and = has_permission and False

print("p OR True:", check_or)
print("p AND False:", check_and)
print("~" * 20)

# Приклад закону поглинання
is_admin = True
is_moderator = False

# Складна умова
has_rights_complex = is_admin and (is_admin or is_moderator)

# Спрощена
has_rights_simple = is_admin

print(f"Складна умова: {has_rights_complex}")
print(f"Проста умова: {has_rights_simple}")

print("~~~Закони де Моргана~~~")
# Заперечення кон‘юнкції ¬(p∧q)=¬p∨¬q
# Заперечення диз’юнкції ¬(p∨q)=¬p∧¬q

is_authenticated = True
has_subscription = False

# Замість складного виразу з запереченням:
if not (is_authenticated and has_subscription):
    print("Access denied")

# Можна написати еквівалентно, але зрозуміліше:
if not is_authenticated or not has_subscription: # ¬(p ∧ q) = ¬p ∨ ¬q
    print("Access denied")

