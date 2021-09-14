class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if sum(arr) % 3 != 0:
            return False
        total = sum(arr) / 3
        temp = 0
        count = 0
        for val in arr:
            temp += val
            if temp == total:
                temp = 0
                count += 1
        print(count)
        return count >= 3
