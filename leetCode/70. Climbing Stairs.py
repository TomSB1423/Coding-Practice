class Solution:
    def climbStairs(self, n: int) -> int:
        p = 1
        pp = 1
        temp = 0
        for i in range(n-1):
            temp = p + pp
            p, pp = temp, p
        return p
