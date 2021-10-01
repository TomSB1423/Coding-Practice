def func(A, K):
    if not A:
        return A
    for i in range(K):
        temp = A.pop()
        A.insert(0, temp)
    return A
