class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        sub = ""
        for char in s:
            if char in sub:
                sub = sub[sub.index(char) + 1:] + char
            else:
                sub += char
            max_sub = max(max_sub, len(sub))
        return max_sub

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        sub = ""
        for char in s:
            if char in sub:
                sub = sub[sub.index(char) + 1:] + char
            else:
                sub += char
            max_sub = max(max_sub, len(sub))
        return max_sub