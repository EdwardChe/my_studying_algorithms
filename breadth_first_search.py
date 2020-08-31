from collections import deque

def person_is_seller(name):                         # критерий соответствия результату поиска
    return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(graph)
def search(name):
    search_queue = deque()                          # создание новой очереди
    search_queue += graph[name]                     # добавление всех соседей
    searched = []                                   # для отслеживания проверенных
    while search_queue:
        person = search_queue.popleft()             # извлечение первого из очереди
        if not person in searched:                  # проверка, что не повторно
            if person_is_seller(person):            # проверка, что является результатом поиска
                print(person + ' is a seller!')     # если соответствует 
                return True
            else:
                search_queue +=graph[person]        # если не соответствует
                searched.append(person)
    return False

search("you")
