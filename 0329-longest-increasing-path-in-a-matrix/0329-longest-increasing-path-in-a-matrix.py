class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # cache[(row, col)] = longest increasing path from row, col.
        rows = len(matrix)
        cols = len(matrix[0])
        cache = {}
        
        def dfs(row, col, prevNum):
            if (row not in range(rows) or
                col not in range(cols) or
                matrix[row][col] <= prevNum):
                return 0
            if (row, col) in cache:
                return cache[(row, col)]
            
            result = 1
            result = max(result, 1 + dfs(row + 1, col, matrix[row][col]))
            result = max(result, 1 + dfs(row - 1, col, matrix[row][col]))
            result = max(result, 1 + dfs(row, col + 1, matrix[row][col]))
            result = max(result, 1 + dfs(row, col - 1, matrix[row][col]))
            cache[(row, col)] = result
            return result
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, float('-inf'))

        return max(cache.values())