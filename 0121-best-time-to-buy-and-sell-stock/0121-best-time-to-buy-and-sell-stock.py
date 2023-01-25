class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(prices[i] - minPrice, maxProfit)
        return maxProfit