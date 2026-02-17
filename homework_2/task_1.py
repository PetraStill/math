"""
Задача 1. Аналітика музичного сервісу
"""

rock_fans = {101, 102, 103, 105, 107, 109, 110, 112, 115, 118}
pop_fans = {102, 104, 105, 106, 108, 110, 111, 113, 115, 117}
jazz_fans = {103, 105, 108, 110, 112, 114, 115, 116, 119, 120}

# Визначаємо загальне охоплення: 
# скільки унікальних користувачів слухали хоча б один із цих жанрів?

unique = rock_fans | pop_fans | jazz_fans
print(f"Загальне охоплення: {len(unique)}.")

# Знаходимо "всеїдних меломанів" — користувачів, які слухали всі три жанри. 
# Виводимо їхні ID та кількість.

meloman = rock_fans & pop_fans & jazz_fans
print(f"Кількість всеїдних меломанів: {len(meloman)}.")
print(f"IDs меломанів: {sorted(meloman)}.")

# Знаходимо цільову аудиторію для нішевої реклами: 
# "чисті рокери" — ті, хто слухав рок, але НЕ слухав ні поп, ні джаз.

rockers = rock_fans - (pop_fans | jazz_fans)
print(f"Кількість рокерів: {len(rockers)}.")
print(f"IDs рокерів: {rockers}.")

# Знаходимо користувачів, які слухали рівно два жанри (будь-яку пару, але не всі три).

both_rock_pop = (rock_fans & pop_fans) - jazz_fans
both_rock_jazz = (rock_fans & jazz_fans) - pop_fans
both_pop_jazz = (pop_fans & jazz_fans) - rock_fans

exactly_two = both_rock_pop | both_rock_jazz | both_pop_jazz
print(f"Будь-яка пара» = Rock+Pop або Rock+Jazz або Pop+Jazz: {len(exactly_two)}.")

# Будуємо візуалізацію перетинів (діаграму Венна) за допомогою бібліотеки matplotlib_venn.

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

venn3([rock_fans, pop_fans, jazz_fans], ('Рок', 'Поп', 'Джаз'))
plt.title("Візуалізація перетинів для слухачів")
plt.show() 
