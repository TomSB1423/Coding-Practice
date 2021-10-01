def solution(A):
    n = len(A)
    count = [0] * (n+2)
    for i in A:
        if 0 < i <= n:
            count[i-1] += 1
    for i in range(len(count)):
        if count[i] == 0:
            return i + 1
    return None


print(solution([90, 91, 92, 93]))
