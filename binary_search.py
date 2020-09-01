# Бинарный поиск.

import time

data_search = int(input('Введите данные поиска: '))
time_start = time.time()

def bynary_search(data_list):
    data_list = sorted(data_list)
    print(data_list)
    low = 0
    high = len(data_list) - 1
    # пока не останется 1 элемент
    while low <= high: 
        # определяем средний элемент         
        mid = (high + low) // 2     
        guess = data_list[mid]
        # значение найдено
        if guess == data_search:    
            return mid
            # больше 
        if guess > data_search:     
            high = mid - 1
            # меньше 
        else:                       
            low = mid + 1
            # значение не существует
    return None                     
my_list = [2, 4, 7, 1, 3, 10, ]

print(bynary_search(my_list))
delta_time = time.time() - time_start
print(delta_time)

