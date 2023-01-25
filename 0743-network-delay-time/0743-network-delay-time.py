class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # We utilize Dijkstra's algorithm (BFS with a minHeap / priority queue)
        # to solve this single source shortest path.
        # O(E * logV^2) ~ O(E * logV)

        adjacencyList = defaultdict(list)
        for source, terminal, time in times:
            adjacencyList[source].append([time, terminal])
        
        result = 0
        visited = set()
        minHeap = [[0, k]]  # [[time, terminal], ...]
        while minHeap:
            time, terminal = heapq.heappop(minHeap)
            if terminal in visited:
                continue
            visited.add(terminal)
            result = time
            for adjTime, adjTerminal in adjacencyList[terminal]:
                if adjTerminal not in visited:
                    heapq.heappush(minHeap, [time + adjTime, adjTerminal])
        return result if len(visited) == n else -1