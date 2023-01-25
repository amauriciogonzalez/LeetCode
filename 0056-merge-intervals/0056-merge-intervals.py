class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = []
        i = 0
        while i != len(intervals):
            if i != len(intervals) - 1 and intervals[i][1] >= intervals[i+1][0]:
                interval = intervals.pop(i)
                intervals[i] = [min(intervals[i][0], interval[0]), max(intervals[i][1], interval[1])]
            else:
                result.append(intervals[i])
                i += 1
        
        return intervals