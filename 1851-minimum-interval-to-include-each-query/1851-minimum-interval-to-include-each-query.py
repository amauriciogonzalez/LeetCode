class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # O(nlogn + qlogq) Time complexity via sorting intervals and queries.
        intervals.sort()
        intervalHeap = [] # [(size, rightmostVal), ...]
        result = {}
        i = 0
        # Creates a copy of queries and sorts it.
        for query in sorted(queries):
            # Add to the heap all all possible intervals the query might belong to.
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(intervalHeap, (right - left + 1, right))
                i += 1
            
            # Remove intervals that the query does not belong to.
            while intervalHeap and intervalHeap[0][1] < query:
                heapq.heappop(intervalHeap)
            
            # Assign the corresponding output for the query.
            if intervalHeap:
                result[query] = intervalHeap[0][0]
            else:
                result[query] = -1
            
        return [result[query] for query in queries]

        
        
        