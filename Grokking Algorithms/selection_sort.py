def selection_sort(array):
    for i in range(len(array)):
        lowest_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest_idx]:
                lowest_idx = j
        array[i], array[lowest_idx] = array[lowest_idx], array[i]
    return array


my_array = [1,4,2,20,10,5,3]
print(selection_sort(my_array))
