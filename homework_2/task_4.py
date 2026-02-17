"""
Задача 4. Аналіз соціальної мережі компанії
"""

"""1. Три різні представлення цього графа"""

# 1. Список суміжності (як словник)

adj_list = {
    'Анна': ['Богдан', 'Віктор', 'Ганна'],
    'Богдан': ['Анна', 'Віктор', 'Дмитро'],
    'Віктор': ['Анна', 'Богдан', 'Ганна', 'Дмитро'],
    'Ганна': ['Анна', 'Віктор', 'Євген'],
    'Дмитро': ['Богдан', 'Віктор', 'Євген'],
    'Євген': ['Ганна', 'Дмитро']

}

print("Список суміжності:")
for vertex, neighbors in adj_list.items():
    print(f"{vertex}: {neighbors}")

print() # Тут і надалі пустий рядок, щоб розділити те, що виводиться. 


# 2. Список ребер (як список кортежів)

# Формуємо список ребер на основі списку суміжності
edges_set = set()

# Проходимо по ключам словника і зберігаємо їх значення в змінну neighbors
for u in adj_list:
    neighbors = adj_list[u]

    # Проходимо циклом по елементах neighbors і створюємо кортежі: усі ребра
    for v in neighbors:
        edge = tuple(sorted([u, v]))
        edges_set.add(edge)

# Сортуємо і виводимо список ребер (як список кортежів)
edges = sorted(edges_set)
print("Список усіх ребер:\n" + "\n".join(map(str, edges)))
print()


# 3. Матриця суміжності (як вкладені списки)

# Створюємо список ключів словника (вершин) і беремо його довжину
vertices = sorted(adj_list.keys())      
n = len(vertices)

# Створюємо словник idx: ім'я вершини -> її індекс у списку vertices 
# (для доступу до рядка/колонки матриці)
idx = {}
for row_col, name in enumerate(vertices):
    idx[name] = row_col

# Ініціалізуємо порожню матрицю nxn
adjacency_matrix = []
for _ in range(n):
    adjacency_matrix.append([0] * n)

# Заповнюємо матрицю за списком суміжності
for u in adj_list:
    for v in adj_list[u]:
        row = idx[u]
        col = idx[v]
        adjacency_matrix[row][col] = 1
        adjacency_matrix[col][row] = 1 # бо граф неорієнтований

# Виводимо матрицю
print("Порядок вершин (рядки/колонки):\n", vertices)
for row in adjacency_matrix:
    print(row)

print()


"""Степінь кожної вершини"""

print("Степінь кожної вершини:")
for vertex, neighbors in adj_list.items():
    print(f"{vertex}: {len(neighbors)}")
  

most_social = max(adj_list, key=lambda v: len(adj_list[v]))
print(f"Найбільш комунікабельним є {most_social}.")


least_social = min(adj_list, key=lambda v: len(adj_list[v]))
print(f"Найменш комунікабельним є {least_social}.")
print()

"""Теорема про суму степенів"""

# Рахуємо суму степенів (для формули)
degree_sum = sum(len(neighbors) for neighbors in adj_list.values())
print(f"Сума степенів: {degree_sum}.")


# Обчислюємо кількість ребер
edges_count = len(edges)
print(f"Кількість ребер: {edges_count}.")


# Перевіряємо значення із формули і обчислення 
print(f"Чи співпадають значення: {degree_sum == 2 * edges_count}")
