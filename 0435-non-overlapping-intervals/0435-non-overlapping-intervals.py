class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        i = 1
        count = 0
        prevEnd = intervals[0][1]
        while i != len(intervals):
            if intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                count += 1
            else:
                prevEnd = intervals[i][1]
            i += 1
        return count