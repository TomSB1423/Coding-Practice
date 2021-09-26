class Solution:
    def permute(self, nums):
        if len(nums) < 2:
            return [nums[:]]
        ans = []
        for i in range(len(nums)):
            removed = nums.pop(0)
            result = self.permute(nums)
            for val in result:
                val.append(removed)
            ans += result
            nums.append(removed)
        return ans

s = Solution()
s.permute([1,2,3,4,5])