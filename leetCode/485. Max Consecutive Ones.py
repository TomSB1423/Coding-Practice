class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maxs = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                maxs = max(maxs, current)
            else:
                current = 0
        return maxs
