class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}
        for i in range(len(nums)):
            if nums[i] not in store:
                store[target - nums[i]] = i
            else:
                return [store[nums[i]], i]
