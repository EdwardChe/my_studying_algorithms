def quick_sorting(arr):
    if len(arr) < 2:
        return arr
    else:
        sup_point = arr[0]
        less = [i for i in arr[1:] if i <= sup_point]
        more = [i for i in arr[1:] if i > sup_point]
        return quick_sorting(less) + [sup_point] + quick_sorting(more)
array = [4, 2, 1, 6, 0, 3]
print(quick_sorting(array))