def sort_bubble(array):
    """Sorts array using bubble sort method.
    Loops through array and compares consecutive pairs to
    see if one is bigger then swaps if true.
    Adv:
        - Easy to implement
        - Little memory needed as edits inplace
    Dis:
        - Slow compared to other algorithms -> O(n^2)
    """
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapping = True
    return array


def sort_selection(array):
    """Sorts array using selection sort method.
    Loops through array finds min value then swaps them.
    Adv:
        - Good on small list
        - Little memory needed as edits inplace
    Dis:
        - Slow compared to other algorithms -> O(n^2)
    """
    for i in range(len(array)):
        lowest_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_idx]:
                lowest_idx = j
        array[i], array[lowest_idx] = array[lowest_idx], array[i]
    return array


def sort_insertion(array):
    """Sorts array using _____ sort method.
    Loops through elements in array and compares sizes with previous elements.
    If smaller, shifts previous element up and replaces when loop is over.
    Adv:
        - Simple
        - Works well on small lists
        - Little memory needed as edits inplace
    Dis:
        - Slow compared to other algorithms -> O(n^2)
    """
    for i in range(1, len(array)):
        val = array[i]
        j = i - 1
        while j >= 0 and val < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = val
    return array


def sort_quick(array):
    """Sorts array using quick sort method. Recursive algorithm.
    Chooses a pivot point (can be any value, however some positions are more efficient)
    and creates two arrays with values that are higher and lower than the pivot point.
    It then recusivly sorts these two arrays.
    Adv:
        - Best sorting algorithm
        - Deals well with large arrays
        - Little memory needed as edits inplace
    Dis:
        - Will be slow if list already sorted
    """
    length = len(array)
    if length <= 1:
        return array
    # Picks last element as pivot
    pivot = array.pop(-1)
    items_greater = []
    items_lower = []
    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return sort_quick(items_lower) + [pivot] + sort_quick(items_greater)


def sort_heap(array):
    """Sorts array using heap sort method.
    Loops through array and
    Adv:
        - Widly used as efficient
        - Memory usage is minimal
    Dis:
        - Requires memory as does not edit inplace
    """
    return array


def sort_merge(array):
    """Sorts array using merge sort method.
    Loops through array and
    Adv:
        - Can be applied to files of any size
    Dis:
        - Requires extra space ~=N
        - Less efficient
    """
    def merge(a1, a2):
        arr = []
        while a1 and a2:
            if a1[0] < a2[0]:
                arr.append(a1[0])
                a1.pop(0)
            else:
                arr.append(a2[0])
                a2.pop(0)
        return arr

    if len(array) < 2:
        return array
    N = len(array)
    mid = int(N / 2)
    left = array[:mid]
    right = array[mid:N]
    sort_merge(left)
    sort_merge(right)

    merge(left, right)

    return array


my_array = [10, 5, 3, 8, 6, 9]
print("Unsorted array:", my_array)
# print(sort_bubble(my_array))
# print(sort_insertion(my_array))
# print(sort_quick(my_array))
# print(sort_heap(my_array))
print(sort_merge(my_array))
