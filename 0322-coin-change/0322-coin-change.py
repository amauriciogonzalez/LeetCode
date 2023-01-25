class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # A greedy algorithm does not work here. We could do a DFS / backtracking
        # solution, but we have repeating subproblems. Therefore, we use dynamic
        # programming for an optimal solution.
        
        # We do a bottom-up approach.
        # Time O(amount * len(coins))
        # Memory O(amount)
        # dp[coinAmount] = numCoins to sum to coins
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coinAmount in range(1, len(dp)):
            for coin in coins:
                if coinAmount - coin >= 0:
                    dp[coinAmount] = min(dp[coinAmount], 1 + dp[coinAmount - coin])
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
            