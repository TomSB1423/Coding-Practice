class Solution:
    def combine(self, n, k):
        ans = []
        sub = []

        def helper(i, sub):
            if len(sub) >= k:
                ans.append(sub[:])
                return
            for j in range(i, n+1):
                sub.append(j)
                helper(j+1, sub)
                sub.pop()
        helper(1, sub)
        return ans


s = Solution()
print(s.combine(4, 2))
