class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Time and Memory complexity O(n * m)
        #  * Alternatively, we could have a 2D array with
        # cache = [[float('inf') for j in range(N)] for i in range(M)] instead.
        # cache[(i, j)] = the number of operations to convert word1[i:] to word2[j:]
        cache = {}

        # Top down approach
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            # * with the 2D array, we could state
            # if cache[i][j] != float('inf')
            # in which we return cache[i][j]
            if (i, j) in cache:
                return cache[(i, j)]
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            insert = dfs(i, j + 1) + 1
            delete = dfs(i + 1, j) + 1
            replace = dfs(i + 1, j + 1) + 1
            cache[(i, j)] = min(insert, delete, replace)
            return cache[(i, j)]

        return dfs(0, 0)