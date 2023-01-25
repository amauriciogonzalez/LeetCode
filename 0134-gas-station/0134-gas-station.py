class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # if sum(gas) >= sum(cost), then there exists one solution.

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        requiredIndex = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                requiredIndex = i + 1
                total = 0

        # We do not need to return -1 since by this point, a unique
        # solution exists.
        return requiredIndex