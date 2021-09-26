class Solution:
    def subsets(self, nums):
        ans = [[]]
        for val in nums:
            ans += [[val] + x for x in ans]
        return ans


s = Solution()
s.subsets([1, 2, 3, 4, 5])
