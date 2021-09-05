class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums) and nums[i] < target:
            if nums[i] == target:
                return i
            i += 1
        return i
