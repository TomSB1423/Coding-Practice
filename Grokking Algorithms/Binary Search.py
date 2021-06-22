def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while high >= low:
        mid = (high + low) // 2
        mid_val = array[mid]
        print(low, mid, high)
        if mid_val == target:
            return mid
        if mid_val < target:
            low = mid +1
        else:
            high = mid -1
    return None

my_array = [1, 3, 5, 7, 9]
print(binary_search(my_array, 9))
