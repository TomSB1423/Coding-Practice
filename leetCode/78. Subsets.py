# class Solution:
#     def subsets(self, nums):
#         ans = [[]]
#         for val in nums:
#             ans += [[val] + x for x in ans]
#         return ans

# Backtracking solution
class Solution:
    def subsets(self, nums):
        res = []
        sub = []

        def helper(i):
            if i >= len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            helper(i+1)
            sub.pop()
            helper(i+1)
        helper(0)
        return res


s = Solution()
s.subsets([1, 2, 3])
