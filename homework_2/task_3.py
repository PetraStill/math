"""Задача 3. Формування 'Команди мрії'
"""

import math

# Ініціалізуємо списки людей
backend_developers = ['Леонід', 'Іван', 'Сергій', 'Петро', 'Віталій', 'Василь', 'Тарас', 'Юрій']
frontend_developers = ['Tom', 'John', 'Stu', 'Stephen', 'Andrew', 'Max']
designers = ['Nancy', 'Suzy', 'Hanna', 'Natalya']

# Рахуємо комбінації 
backend_count = math.comb(len(backend_developers), 2)
frontend_count = math.comb(len(frontend_developers), 2)
designer_count = math.comb(len(designers), 1)

# Поєднуємо всі можливі комбінації
total = backend_count * frontend_count * designer_count 

print(f"Варіантів вибору 2 Back-end з 8: {backend_count}")
print(f"Варіантів вибору 2 Front-end з 6: {frontend_count}")
print(f"Варіантів вибору 1 Дизайнера з 4: {designer_count}")
print(f"Загальна кількість унікальних команд: {total}")