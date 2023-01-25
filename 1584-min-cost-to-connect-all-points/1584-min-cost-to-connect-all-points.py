class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # We find an MST using Prim's algorithm (easier and efficient)
        # O(v^2 * log(v))

        # Building the adjacency list with distances
        adjacencyList = {i : [] for i in range(len(points))}   # i : [[cost, pointIndex], ...]
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                manDistance = abs(x1-x2) + abs(y1-y2)
                adjacencyList[i].append([manDistance, j])
                adjacencyList[j].append([manDistance, i])
        
        # Prim's algorithm
        result = 0
        visited = set()
        frontier = [[0, 0]] # minHeap [[cost, pointIndex], ...]
        while len(visited) < len(points):
            cost, i = heapq.heappop(frontier)
            if i in visited:
                continue
            result += cost
            visited.add(i)
            for adjCost, adj in adjacencyList[i]:
                if adj not in visited:
                    heapq.heappush(frontier, [adjCost, adj])
        return result