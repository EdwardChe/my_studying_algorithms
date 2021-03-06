# Сортировка выбором

# нахождение наименьшего значения
def find_small_element(arr):            
    small_element = arr[0]  
    small_element_index = 0
    for i in range(1, len(arr)):
        if arr[i] < small_element:
            small_element = arr[i]
            # сохранение индекса нименьшего значения
            small_element_index = i     
    return small_element_index

# сортировка массива
def selection_sort(arr):                
    new_array = []
    for i in range(len(arr)):
        smallest_element = find_small_element(arr)
        new_array.append(arr.pop(smallest_element))
    return new_array

data_array = [5, 4, 2, 9, 48, 1, 4, 3, ]

print(selection_sort(data_array))