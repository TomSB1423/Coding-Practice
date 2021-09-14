class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):

            if total - leftSum - nums[i] == leftSum:
                return i
            leftSum += nums[i]
        return -1
