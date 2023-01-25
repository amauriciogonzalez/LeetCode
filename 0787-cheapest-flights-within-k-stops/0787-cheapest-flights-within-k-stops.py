class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Dijkstra's Algorithm
        adjacencyList = defaultdict(list)
        for source, terminal, cost in flights:
            adjacencyList[source].append([cost, terminal])
        minHeap = [[0, src, k + 1]]  # [[weight, terminal, pathIndex], ...]
        visited = [0] * n # visted[i] records steps to reach i with the lowest cost.
        while minHeap:
            cost, terminal, remainingPath = heapq.heappop(minHeap)
            if terminal == dst:
                return cost
            if visited[terminal] >= remainingPath:
                continue
            visited[terminal] = remainingPath
            for adjCost, adjTerminal in adjacencyList[terminal]:
                heapq.heappush(minHeap, [cost + adjCost, adjTerminal, remainingPath - 1])
        return -1