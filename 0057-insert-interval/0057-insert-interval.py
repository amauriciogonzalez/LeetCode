class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # O(n) time and memory complexity

        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                result = result + intervals[i:]
                return result
            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else: # The newInterval overlaps the current interval in some way.
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        result.append(newInterval)

        return result