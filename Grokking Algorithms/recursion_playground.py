def print_values(array):
    for i in range(len(array)):
        if type(array[i]) is list:
            print_values(array[i])
        else:
            print(array[i])


my_array = [
    [1, [2.2, 2.3, [2.35, 2.36, 2.37, 2.38]], 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

print_values(my_array)
