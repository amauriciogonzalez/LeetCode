class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        result = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            result.append(cost[i] + min(result[i - 1], result[i - 2]))
        return min(result[-2], result[-1])
