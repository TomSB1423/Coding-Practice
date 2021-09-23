class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int(l + (r-l) / 2)
            if target == nums[l]:
                return l
            if nums[l] < target <= nums[mid]:
                r = mid
            elif nums[mid] < target < nums[r]:
                l = mid + 1
            else:
                if target > nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        return -1


s = Solution()
print(s.search([4], 4))
