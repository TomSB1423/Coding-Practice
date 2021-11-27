# Params
# weight, value
items = [[5, 60], [3, 50], [4, 70], [2, 30]]
capacity = 5
n = len(items) - 1

# Recursion by brute force


def brute_knapsack(items, capacity, n):
    # Base case: if n = 0 or ran out of room return
    if n == 0 or capacity == 0:
        return 0
    if capacity - items[n][0] < 0:
        return brute_knapsack(items, capacity, n-1)
    else:
        # Case 1: choose item
        chosen = brute_knapsack(
            items, capacity - items[n][0], n-1) + items[n][1]
        # Case 2: don't choose item
        not_chosen = brute_knapsack(items, capacity, n-1)
        return max(chosen, not_chosen)
    return 0


print(brute_knapsack(items, capacity, n))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def dynamic_knapsack(items, capacity, n):
    memo = [[0 for i in range(capacity+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            # If does not fit in capacity
            if j-items[i][0] < 0:
                memo[i][j] = memo[i-1][j]
            # Take the max of:
            # Use item: optimum of capacity - weight of item + item
            # Don't use item: value above
            else:
                memo[i][j] = max(memo[i][j-items[i][0]] +
                                 items[i][1], memo[i-1][j])
    print(memo)
    return memo[-1][-1]


print(dynamic_knapsack(items, capacity, n))
