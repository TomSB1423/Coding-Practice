# WRONG Will need to redo

class Solution:
    def longestPalindrome(self, s):
        maxs = ""
        temp = 0
        for i in range(len(s)-1):
            temp = self.go_from_center(s, i, i)
            temp2 = self.go_from_center(s, i, i+1)
            if len(temp) > len(maxs):
                maxs = temp
            if len(temp2) > len(maxs):
                maxs = temp2
        return maxs

    def go_from_center(self, s, l, r):
        if l > r:
            return ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l: r-1]


s = Solution()
print(s.longestPalindrome("babad"))
