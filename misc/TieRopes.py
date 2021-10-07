def solution(K, A):
    count = 0
    cur_length = 0
    for val in A:
        cur_length += val
        if cur_length >= K:
            cur_length = 0
            count += 1
    return count
