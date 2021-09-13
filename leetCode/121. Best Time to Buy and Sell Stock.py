class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minimum = float("inf")
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] - minimum > profit:
                profit = prices[i] - minimum
        return profit
