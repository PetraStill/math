"""
Задача 2. Конфігуратор доступу до системи

Система має 4 рівні доступу. Доступ надається (True), якщо виконується логічна умова:

Base (Базовий): Користувач є співробітником ТА верифікований ТА НЕ заблокований.
Premium (Преміум): (Користувач є співробітником АБО має преміум) ТА верифікований ТА НЕ заблокований.
Admin (Адмін-панель): Користувач є адміністратором ТА верифікований ТА НЕ заблокований.
Secret (Секретні матеріали): (Користувач є адміністратором АБО (є співробітником ТА має преміум)) ТА верифікований ТА НЕ заблокований.
"""

from itertools import product

def check_access(is_employee, is_verified, is_premium, is_admin, is_banned):
    access_data = {}

    if not is_banned and is_verified:
        # Base
        if is_employee:
            access_data['Base'] = True
        else:
            access_data['Base'] = False

        # Premium
        if is_employee or is_premium:
            access_data['Premium'] = True
        else:
            access_data['Premium'] = False

        # Admin
        if is_admin:
            access_data['Admin'] = True
        else:
            access_data['Admin'] = False

        # Secret
        if is_admin or (is_employee and is_premium):
            access_data['Secret'] = True
        else:
            access_data['Secret'] = False

    else:
        access_data['Base'] = False
        access_data['Premium'] = False
        access_data['Admin'] = False
        access_data['Secret'] = False

    return access_data


# Таблиця істинності (0/1)
print("Emp Ver Prem Adm Ban | Base Prem Adm Secr")
print("-" * 44)

for emp, ver, prem, adm, ban in product([True, False], repeat=5):
    a = check_access(emp, ver, prem, adm, ban)

    # True/False перетворюємо на 1/0 через int(...)
    print(f"{int(emp):>3} {int(ver):>3} {int(prem):>4} {int(adm):>3} {int(ban):>3} |"
          f" {int(a['Base']):>4} {int(a['Premium']):>4} {int(a['Admin']):>3} {int(a['Secret']):>4}")


"""
Відповіді на питання з аналізу

1. У скількох випадках є повний доступ до всіх 4 секцій одночасно? – У двох.
        Коли is_verified=1, is_banned=0, is_employee=1, is_admin=1, а is_premium може бути 0 або 1.

2. Чи існує комбінація, де є доступ до Premium, але немає доступу до Base?
    Так, існує (2 комбінації):
        1) is_employee=0, is_verified=1, is_premium=1, is_banned=0, is_admin=0
        2) is_employee=0, is_verified=1, is_premium=1, is_banned=0, is_admin=1
    Пояснення: Premium дозволяє доступ, якщо користувач – або співробітник, або має преміум, 
    а Base вимагає обов’язково співробітника.
"""