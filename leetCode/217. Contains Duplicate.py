class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        for val in nums:
            if not count.get(val):
                count[val] = 1
            else:
                return True
        return False
