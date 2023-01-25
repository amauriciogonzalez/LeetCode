class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # cache[row][col] = numWays to reach the finish
        # so cache[m - 1][n - 1] = 1
        # Below the last row and to the right of the last column, we'll
        # have 0's to maintain result = numWaysDown + numWaysRight
        # O(m * n) time and memory complexity

        cache = [[-1 for i in range(n + 1)] for j in range(m + 1)]
        for j in range(n + 1):
            cache[-1][j] = 0
        for i in range(m + 1):
            cache[i][-1] = 0

        cache[m-1][n-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                print(i, j)
                if i == m - 1 and j == n - 1:
                    continue
                cache[i][j] = cache[i+1][j] + cache[i][j+1]

        return cache[0][0]