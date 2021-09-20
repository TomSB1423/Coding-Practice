# Slow way
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32, -1, -1):
            if n % (2**i) >= 0 and n % (2**i) != n:
                count += 1
                n = n % (2**i)
                print(n, 2**i, n % (2**i))
        return count

# Fast way is to use a bit shift - haven't learnt yet