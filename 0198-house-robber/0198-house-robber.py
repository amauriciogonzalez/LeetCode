class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # An important DP problem.
        rob1 = 0
        rob2 = 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            # max(gap between current house and previous house, includes previous house)
            temp = max(n + rob1, rob2) # temp is the locally best subproblem solution.
            rob1 = rob2
            rob2 = temp
        return rob2