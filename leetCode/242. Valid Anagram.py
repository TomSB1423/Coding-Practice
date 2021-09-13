class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = {}
        for i in s:
            if not count.get(i):
                count[i] = 1
            else:
                count[i] += 1

        for j in t:
            if not count.get(j):
                return False
            else:
                count[j] -= 1
        return True if all(x == 0 for x in count.values()) else False
