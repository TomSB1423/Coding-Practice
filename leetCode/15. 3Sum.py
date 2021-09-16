class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(nums)):
            store = {}
            for j in range(i + 1, len(nums)):
                if nums[j] not in store:
                    store[-nums[i] - nums[j]] = nums[j]
                else:
                    temp = sorted([nums[i], store[nums[j]], nums[j]])
                    if temp not in ans:
                        ans.append(temp)
        return ans
