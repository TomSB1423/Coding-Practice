def differences(s):
    maxs = ""
    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            maxs = max(s[i:j], maxs)
    return maxs


print(differences("ba"))
