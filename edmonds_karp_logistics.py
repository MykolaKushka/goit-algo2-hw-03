from collections import defaultdict, deque

# Опис ребер у вигляді (від, до, пропускна здатність)
edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
    ("Джерело", "Термінал 1", float("inf")),
    ("Джерело", "Термінал 2", float("inf")),
    ("Магазин 1", "Стік", float("inf")),
    ("Магазин 2", "Стік", float("inf")),
    ("Магазин 3", "Стік", float("inf")),
    ("Магазин 4", "Стік", float("inf")),
    ("Магазин 5", "Стік", float("inf")),
    ("Магазин 6", "Стік", float("inf")),
    ("Магазин 7", "Стік", float("inf")),
    ("Магазин 8", "Стік", float("inf")),
    ("Магазин 9", "Стік", float("inf")),
    ("Магазин 10", "Стік", float("inf")),
    ("Магазин 11", "Стік", float("inf")),
    ("Магазин 12", "Стік", float("inf")),
    ("Магазин 13", "Стік", float("inf")),
    ("Магазин 14", "Стік", float("inf")),
]

# Пошук шляху збільшення потоку
def bfs(capacity, flow, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        u = queue.popleft()
        for v in capacity[u]:
            if v not in visited and capacity[u][v] - flow[u][v] > 0:
                parent[v] = u
                visited.add(v)
                if v == sink:
                    return True
                queue.append(v)
    return False

# Алгоритм Едмондса-Карпа
def edmonds_karp(graph, source, sink):
    capacity = defaultdict(dict)
    flow = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v in graph[u]:
            capacity[u][v] = graph[u][v]
    parent = {}
    max_flow = 0
    while bfs(capacity, flow, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]
        parent = {}
    return max_flow, flow

# Побудова графа
graph = defaultdict(dict)
for u, v, c in edges:
    graph[u][v] = c

# Виконання алгоритму
max_flow, flow_dict = edmonds_karp(graph, "Джерело", "Стік")

# Вивід результату
print(f"Максимальний потік: {max_flow}")
