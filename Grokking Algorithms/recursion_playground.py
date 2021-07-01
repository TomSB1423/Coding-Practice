### Print out values from nested array ###
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
# print_values(my_array)


### Factorial ###
def factorial(x):
    if x <= 1:
        return 1
    # Product of n * (n-1)
    return x * factorial(x - 1)


# print(factorial(5))


### Fibonacci Sequence ###
def fib(x):
    # First two terms are 1
    if x <= 2:
        return 1
    # If not ended, sum of two previous terms
    else:
        return fib(x - 1) + fib(x - 2)


# 1, 1, 2, 3, 5, 8, 13, 21, 34
print(fib(5))
