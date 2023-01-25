class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # We use dynamic programming because of the existance of a decision
        # tree here.

        # O(n) time and memory complexity
        # cache = {i : buy / sell boolean value}

        cache = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            if buying:
                buy = dfs(i + 1, False) - prices[i] # Subtract the price from the total
                cooldown = dfs(i + 1, True)
                cache[(i, buying)] = max(buy, cooldown)
            else:
                # i + 2 since we have a cooldown day.
                sell = dfs(i + 2, True) + prices[i] # Add the price to the total
                cooldown = dfs(i + 1, False)
                cache[(i, buying)] = max(sell, cooldown)
            return cache[(i, buying)]
        
        return dfs(0, True)
