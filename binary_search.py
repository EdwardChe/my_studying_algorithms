# 1. Бинарный поиск.

import time

data_search = int(input('Введите данные поиска: '))
time_start = time.time()

def bynary_search(data_list):
    data_list = sorted(data_list)
    print(data_list)
    low = 0
    high = len(data_list) - 1
    while low <= high:              # пока не останется 1 элемент
        mid = (high + low) // 2     # определяем средний элемент
        guess = data_list[mid]
        if guess == data_search:    # значение найдено
            return mid
        if guess > data_search:     # больше 
            high = mid - 1
        else:                       # меньше 
            low = mid + 1
    return None                     # значение не существует

my_list = [2, 4, 7, 1, 3, 10]
print(bynary_search(my_list))

delta_time = time.time() - time_start
print(delta_time)

