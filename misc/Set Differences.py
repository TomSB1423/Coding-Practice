def differences(a, b):
    ans = []
    for val in a:
        if val not in b:
            ans.append(val)
    return ans if ans else None


print(differences([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5]))
