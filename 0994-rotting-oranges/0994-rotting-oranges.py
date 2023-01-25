class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # We use multi-source BFS
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        minutes = 0
        numFresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    numFresh += 1
                elif grid[r][c] == 2:
                    queue.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and numFresh > 0:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row not in range(rows) or
                        col not in range(cols) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    numFresh -= 1
            minutes += 1
        
        return minutes if numFresh == 0 else -1


        

            
        