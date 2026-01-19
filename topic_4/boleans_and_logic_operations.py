# Обчислимо істинність простих висловлювань:

print(5 > 3)        # True
print(10 == 7)      # False
print(2 + 2 == 4)   # True
print("кіт" == "пес")  # False
print("~" * 20)
"""
Нехай:
    p = "Користувач авторизований". 
        В програмі це може бути, наприклад, результатом перевірки user.token is not None
    q = "Користувач має права адміністратора". 
        В програмі це може бути, наприклад, перевіркою user.role == "admin"
Тепер ми можемо говорити про різні комбінації цих висловлювань. 
Наприклад, "Користувач авторизований та має права адміністратора" можна записати як "p і q".
"""

# У програмуванні змінні можуть зберігати булеві значення напряму:
is_authenticated = True
is_admin = False
is_premium_user = True

# Перевірка статусу
print(f"Авторизований: {is_authenticated}")
print(f"Адміністратор: {is_admin}")
print(f"Преміум користувач: {is_premium_user}")
print("~" * 20)

# Висловлювання з перевірками:
temperature = 75
pressure = 120

# Створюємо висловлювання
is_temperature_normal = (temperature >= 36) and (temperature <= 100)
is_pressure_high = pressure > 140

print(f"Температура в нормі: {is_temperature_normal}")
print(f"Високий тиск: {is_pressure_high}")
print("~" * 20)

"""
Заперечення

Найпростіша логічна операція — це заперечення. 
Вона змінює істинність висловлювання на протилежну. 
Якщо висловлювання було істинним — заперечення робить його хибним, і навпаки.
"""

# Позначення: ¬p або NOT p
# Для заперечення все просто: коли вхід 0 (хиба), вихід 1 (істина), і навпаки.

is_logged_in = False

# Заперечення
is_guest = not is_logged_in

print(f"Користувач увійшов: {is_logged_in}")
print(f"Це гість: {is_guest}")

"""
Кон’юкція

Це логічна операція "І". 
Результат істинний тільки тоді, коли обидва висловлювання істинні одночасно.
"""

# Позначення: p∧q або p AND q
# Розглянемо програмно перевірку права на дію:
is_authenticated = True
has_permission = True
is_account_active = False

# Кон'юнкція: всі умови мають бути істинними
can_edit_post = is_authenticated and has_permission and is_account_active

print(f"Може редагувати пост: {can_edit_post}")

"""
Диз’юнкція

Диз'юнкція — це логічна операція "АБО". 
Результат істинний, якщо хоча б одне з висловлювань істинне.
"""

# Позначення: p∨q або p OR q
# Розглянемо приклад перевірки способу оплати, який ілюструє роботу диз’юнкції:
has_credit_card = False
has_cash = True
has_online_payment = False

# Диз'юнкція: достатньо одного способу
can_pay = has_credit_card or has_cash or has_online_payment

print(f"Може оплатити: {can_pay}")

"""
Виключне АБО

Виключне АБО (exclusive OR) — це операція, яка повертає істину 
тільки коли висловлювання мають різні значення істинності. 
Якщо обидва істинні або обидва хибні, результат буде хибним.
"""

# Позначення: p⊕q або p XOR q
# Виключне АБО можна виразити через інші операції: 
# p⊕q=(p∨q)∧¬(p∧q) – "p або q, але не обидва одночасно".

# Виконаємо перевірку, що ввімкнено рівно один режим роботи програми:
test_mode = True
default_mode = False

valid_configuration = (test_mode or default_mode) and not (test_mode and default_mode)
# або 
# valid_configuration = test_mode != default_mode

print(f"Коректний запуск: {valid_configuration}")

