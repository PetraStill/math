"""Задача 3. Формування 'Команди мрії'
    Розв'язок через product and combinations.
"""

from itertools import combinations
from itertools import product

backend_developers = ['Леонід', 'Іван', 'Сергій', 'Петро', 'Віталій', 'Василь', 'Тарас', 'Юрій']
frontend_developers = ['Tom', 'John', 'Stu', 'Stephen', 'Andrew', 'Max']
designers = ['Nancy', 'Suzy', 'Hanna', 'Natalya']

# Генеруємо всі можливі двійки backend_developers
all_back = list(combinations(backend_developers, 2))

# Генеруємо всі можливі двійки frontend_developers
all_front = list(combinations(frontend_developers, 2))

# Генеруємо всі можливі двійки designers
all_designers = list(combinations(designers, 1))

all_teams = list(product(all_back, all_front, all_designers))

print("Back варіантів:", len(all_back))
print("Front варіантів:", len(all_front))
print("Design варіантів:", len(all_designers))
print("Всього варіантів команд:", len(all_teams))  

print(f"Перші п'ять варіантів команд: ")
for i, team in enumerate(all_teams[:5], 1):
    b = team[0]
    f = team[1]
    d = team[2]
    full_team = list(b) + list(f) + list(d)
    print(f"{i}. {', '.join(full_team)}")