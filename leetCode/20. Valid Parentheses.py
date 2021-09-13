class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        mapping = {"{": "}", "(": ")", "[": "]"}
        for i in range(len(s)):
            if s[i] in mapping:
                stack.append(s[i])
            elif stack and s[i] == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return False if stack else True
