def solution(A):
    dp = [0] * 6
    dp[-1] = A[0]
    for i in range(1, len(A)):
        max_val = float("-inf")
        for j in range(1, 7):
            if i-j >= 0:
                max_val = max(max_val, dp[-j] + A[i])
        dp.append(max_val)
        dp.pop(0)
    return dp[-1]

solution( [1, -2, 0, 9, -1, -2])