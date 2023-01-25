class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # This can also be done via dynamic programming with a time complexity of O(n^2).
        # We would have cache[index] = T/F can we reach the last index from index.

        # O(n) time complexity greedy solution in which we shift the goal leftward
        # when an earlier index can reach the goal, which starts at the rightmost index.

        goal = len(nums) - 1
        i = len(nums) - 2

        while i >= 0:
            if (goal - i) <= nums[i]:
                goal = i
            i -= 1
        
        if goal == 0:
            return True
        else:
            return False