# Dict method
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


# Alt two pointer method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = []
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x: x[1])
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l][1] + nums[r][1] == target:
                x.append(nums[l][0])
                x.append(nums[r][0])
                return x
            elif nums[l][1] + nums[r][1] > target:
                r -= 1
            elif nums[l][1] + nums[r][1] < target:
                l += 1
