# 2. Сортировка выбором

def find_small_element(mass):
    small_element = mass[0]
    small_element_index = 0
    for i in range(1, len(mass)):
        if mass[i] < small_element:
        small_element = mass[i]
        small_element_index = i
    return small_element_index