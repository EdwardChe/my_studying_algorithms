# Поиск в ширину

from collections import deque

# критерий соответствия результату поиска
def person_is_seller(name):                         
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

def search(name):
    # создание новой очереди
    search_queue = deque()    
    # добавление всех соседей                      
    search_queue += graph[name]
    # для отслеживания проверенных                     
    searched = []                                   
    while search_queue:
        # извлечение первого из очереди
        person = search_queue.popleft()             
        # проверка, что не повторно
        if not person in searched:
            # проверка, что является результатом поиска              
            if person_is_seller(person): 
                # если соответствует           
                print(person + ' is a seller!')      
                return True
            else:
                # если не соответствует
                search_queue +=graph[person]        
                searched.append(person)
    return False

search("you")
