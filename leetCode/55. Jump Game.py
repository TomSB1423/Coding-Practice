class Solution:
    def canJump(self, nums):
        idx = 1
        for i in range(len(nums)-2, -1, -1):
            print(nums[i], idx)
            if nums[i] >= idx:
                idx = 1
            else:
                idx += 1
        return True if idx == 1 else False
