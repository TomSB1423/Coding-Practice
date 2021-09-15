class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        count = 0
        for val in nums:
            if count < 0:
                count = 0
            count += val
            maximum = max(maximum, count)
        return maximum
