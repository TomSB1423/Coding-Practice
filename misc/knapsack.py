# Params
# weight, value
items = [[5, 60], [3, 50], [4, 70], [2, 30]]
capacity = 5
n = len(items) - 1

## Recursion by brute force
def brute_knapsack(items, capacity, n):
    # Base case: if n = 0 or ran out of room return
    if n == 0 or capacity == 0:
        return 0
    if capacity - items[n][0] < 0:
        return brute_knapsack(items, capacity, n-1)
    else:
        # Case 1: choose item
        chosen = brute_knapsack(items, capacity - items[n][0], n-1) + items[n][1]
        # Case 2: don't choose item
        not_chosen = brute_knapsack(items, capacity, n-1)
        return max(chosen, not_chosen)
    return 0


print(brute_knapsack(items, capacity, n))



## Recursion by brute force
def brute_knapsack(items, capacity, n):
    # Base case: if n = 0 or ran out of room return
    if n == 0 or capacity == 0:
        return 0
    if capacity - items[n][0] < 0:
        return brute_knapsack(items, capacity, n-1)
    else:
        # Case 1: choose item
        chosen = brute_knapsack(items, capacity - items[n][0], n-1) + items[n][1]
        # Case 2: don't choose item
        not_chosen = brute_knapsack(items, capacity, n-1)
        return max(chosen, not_chosen)
    return 0







def dynamic_knapsack(items, capacity, n):
    memo = [[0 for i in range(capacity+1)] for j in range(n+1)]
    for i in range(len(n+1)):
        for j in range(len(capacity+1)):
            # Base case
            if j-i < 0:
                memo[i][j] = memo[i-1][j]
            else:
                
        
    # Case 1: choose item
    
    # Case 2: don't choose item
    

    return












------------------------------------
# Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
 
 
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
 
# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
 
# This code is contributed by Bhavya Jain