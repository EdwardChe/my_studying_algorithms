# Алгоритм Дейкстры

# граф
graph = {}
graph["start"]={}           
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["final"] = 1
graph["b"] = {}
graph["b"]["final"] = 5
graph["b"]["a"] = 3
graph["final"] = {}

# стоимости
infinity = float("inf")     
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["final"] = infinity

# родители
parents ={}
parents["a"] = "start"
parents["b"] = "start"
parents["final"] = None

# массив для отслеживания обработанных узлов
processed = []

# нахождение узла с наименьшей стоимостью
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            # назначение нового узла с наименьшей стоимостью
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)     
# пока есть необработанные узлы
while node is not None:
    # получение стоимости найденного узла
    cost = costs[node]
    # получение соседей найденного узла
    neighbors = graph[node]
    # перебор всех соседей текущего узла
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            # обновление стоимости узла
            costs[n] = new_cost
            parents[n] = node
    # узел обработан
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
