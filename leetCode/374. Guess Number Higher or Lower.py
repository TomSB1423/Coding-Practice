# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        pick = None
        p1 = 0
        p2 = n
        while p1 < p2:
            mid = (p1 + p2) / 2
            pick = guess(mid)
            if pick is 0:
                return mid
            elif pick is 1:
                p1 = mid + 1
            else:
                p2 = mid
        return n
