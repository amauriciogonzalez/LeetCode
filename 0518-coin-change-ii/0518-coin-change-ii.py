class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # ((amount + 1) x len(coins) + 1) 2D cache.
        # cache[i][j] = the number of ways to represent i money with the coins in coins[0:j+1].

        cache = [[0 for j in range(len(coins) + 1)] for i in range(amount + 1)]

        # It takes one way to represent 0 money with the coins in coins[i:].
        for j in range(len(coins) + 1):
            cache[0][j] = 1

        # The final column is never updated from 0.
        # We cycle through columns then rows.
        for i in range(1, amount + 1):
            for j in range(len(coins) - 1, -1, -1):
                cache[i][j] = cache[i][j + 1]
                if i - coins[j] >= 0:
                    cache[i][j] = cache[i][j] + cache[i - coins[j]][j] 
        return cache[amount][0]