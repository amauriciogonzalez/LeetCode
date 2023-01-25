class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Time and Memory complexity O(n * m)
        # cache[(i, j)] = how many subsequences of s[i:] equal t[j:]
        cache = {}

        # Recursive approach (top-down)
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            numWays = 0
            if s[i] == t[j]:
                numWays += dfs(i + 1, j + 1)
                numWays += dfs(i + 1, j)
            else:
                numWays += dfs(i + 1, j)
            cache[(i, j)] = numWays
            return numWays
        
        return dfs(0, 0)
            
            