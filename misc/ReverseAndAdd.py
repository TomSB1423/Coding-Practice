def s(n):
    reversed = int(str(n)[::-1])
    ans = str(n + reversed)
    for i in range(int(len(ans) / 2)):
        if ans[i] != ans[-i]:
            return False
    return True


print(s(9339))
