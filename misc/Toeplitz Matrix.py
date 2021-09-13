def isToeplitz(arr):
    R, C = len(arr), len(arr[0])
    for c in range(C - 1):
        num = arr[0][c]
        for r in range(1, min(R, C - c)):
            if arr[r][r + c] != num:
                return False
    for r in range(R - 1):
        num = arr[r][0]
        for c in range(1, min(C, R - r)):
            print(arr[c][c + r])
            if arr[c + r][c] != num:
                return False
    return True


print(isToeplitz([[3, 9], [5, 3], [6, 5]]))
