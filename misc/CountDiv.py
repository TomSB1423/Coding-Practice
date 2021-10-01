def greedyCanoeistB(W, k):
    canoes = 0
    j = 0
    i = len(W) - 1
    while (i >= j):
        if W[i] + W[j] <= k:
            j += 1
        canoes += 1
        i -= 1
    return canoes


print(greedyCanoeistB([1, 2, 5, 6, 6, 3, 4], 6))
