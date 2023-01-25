class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # We do a modified version of Djikstra's algorithm, 
        # a BFS with a minimum heap. We use this greedy algorithm
        # to find a minimum height path, nothing with weights.
        visited = set()
        visited.add((0, 0))
        minHeap = [[grid[0][0], 0, 0]] # [[grid[row][col], row, col], ...]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while minHeap:
            elevation, row, col = heapq.heappop(minHeap)
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return elevation
            for dr, dc in directions:
                adjRow = row + dr
                adjCol = col + dc
                if (adjRow not in range(len(grid)) or
                    adjCol not in range(len(grid[0])) or
                    (adjRow, adjCol) in visited):
                    continue
                visited.add((adjRow, adjCol))
                heapq.heappush(minHeap, [max(elevation, grid[adjRow][adjCol]), adjRow, adjCol])
        return -1
