class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Since the problem requires us to count the arrangements
        # with certain conditions, it is a dynamic programming problem.
        # We can either use a decision tree (brute force), which uses the
        # same subproblems / sub-decision trees, or we can use memoization.
        # We do a bottom-up DP approach starting at the base case.

        # Similar to the Fibonacci sequence (but reversed).
        # We do not need a table.

        left = 1
        right = 1
        for i in range(n - 1):
            temp = left
            left = left + right
            right = temp
        return left
        

