class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights)
        cols = len(heights[0])
        # We start from the border nodes and return the intersection
        # of these sets (the nodes that can reach both the Pacific
        # and Atlantic oceans)
        pacificNodes = set()
        atlanticNodes = set()

        def dfs(r, c, visited, prevHeight):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        
        for c in range(cols):
            dfs(0, c, pacificNodes, heights[0][c])
            dfs(rows - 1, c, atlanticNodes, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pacificNodes, heights[r][0])
            dfs(r, cols - 1, atlanticNodes, heights[r][cols - 1])
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacificNodes and (r, c) in atlanticNodes:
                    result.append([r, c])
        return result
