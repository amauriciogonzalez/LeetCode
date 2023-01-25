class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time O(n)
        # Memory O(1)
        currentMin = 1
        currentMax = 1
        result = nums[0]
        for num in nums:
            temp = num * currentMax # currentMax could change, so we use a temporary variable.
            currentMax = max(num * currentMax, num * currentMin, num)
            currentMin = min(temp, num * currentMin, num)
            result = max(result, currentMax)
        return result
        