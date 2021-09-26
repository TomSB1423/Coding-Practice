class Solution:
    def coinChange(self, coins, amount):
        coins.sort()
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                else:
                    break
        return dp[amount] if dp[amount] != amount + 1 else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
