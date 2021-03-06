class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] = digits[-1] + 1
        i = len(digits) - 1
        while digits[i] == 10:
            digits[i] = 0
            if i > 0:
                digits[i - 1] = digits[i - 1] + 1
            else:
                digits = [1] + digits
            i -= 1
        return digits
