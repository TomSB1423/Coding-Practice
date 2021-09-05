def binary_search(array, target):
    """Finds the middle element in the list recursively until
    the middle element is matched with a searched element.
    Generally binary search much quicker, however slower if
    looking for item at start/end of list"""
    low = 0
    high = len(array) - 1
    while high >= low:
        mid = (high + low) // 2
        mid_val = array[mid]
        if mid_val == target:
            return mid
        if mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_array = [1, 3, 5, 7, 9]
print(binary_search(my_array, 9))
