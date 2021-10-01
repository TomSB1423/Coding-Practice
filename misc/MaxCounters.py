# Not optimal
def solution(N, A):
    counters = [0] * N
    for i in A:
        if 0 < i <= N:
            counters[i-1] += 1
        else:
            temp = max(counters)
            counters = [temp] * N
    return counters


print(solution(1, [1]))
