def solution(A, B):
    if len(A) < 1:
        return 0
    count = 1
    last = B[0]
    for i in range(1, len(A)):
        if A[i] > last:
            last = B[i]
            count += 1
    return count


print(solution([1], [5]))
