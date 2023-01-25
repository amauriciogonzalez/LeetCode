class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Similar to a BFS algorithm in which we partition the
        # array into its possible range of steps from the starting position.

        minSteps = 0
        left = 0
        right = 0
        while right < len(nums) -1:
            farthestIndex = 0
            for i in range(left, right + 1):
                farthestIndex = max(farthestIndex, i + nums[i])
            left = right + 1
            right = farthestIndex
            minSteps += 1
        return minSteps
