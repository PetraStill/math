"""Задача 3. Формування 'Команди мрії'
    Із використанням math lib та виведенням перших 5ти команд.
"""

import math
from itertools import combinations, product

backend_developers = ['Леонід', 'Іван', 'Сергій', 'Петро', 'Віталій', 'Василь', 'Тарас', 'Юрій']
frontend_developers = ['Tom', 'John', 'Stu', 'Stephen', 'Andrew', 'Max']
designers = ['Nancy', 'Suzy', 'Hanna', 'Natalya']

backend_count = math.comb(len(backend_developers), 2)
frontend_count = math.comb(len(frontend_developers), 2)
designer_count = math.comb(len(designers), 1)
total = backend_count * frontend_count * designer_count

print(f"Back варіантів: {backend_count}")
print(f"Front варіантів: {frontend_count}")
print(f"Design варіантів: {designer_count}")
print(f"Всього варіантів команд: {total}")

# Демонстрація перших 5 команд
all_back = list(combinations(backend_developers, 2))
all_front = list(combinations(frontend_developers, 2))
all_designers = list(combinations(designers, 1))
all_teams = product(all_back, all_front, all_designers)

print("Перші п'ять варіантів команд:")
for i, (b, f, d) in enumerate(all_teams, 1):
    print(f"{i}. {', '.join(b + f + d)}")
    if i == 5:
        break
