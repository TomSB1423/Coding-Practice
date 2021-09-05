# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1 = 0
        p2 = n
        while p1 < p2:
            mid = int((p2 + p1) / 2)
            print(p1, p2, mid)
            if isBadVersion(mid):
                p2 = mid
            else:
                p1 = mid + 1
        return p2


def isBadVersion(x, bad_val=4):
    if x >= bad_val:
        return True
    else:
        return False


s = Solution()
print(s.firstBadVersion(10))
