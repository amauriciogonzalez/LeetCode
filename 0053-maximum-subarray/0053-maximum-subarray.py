class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time complexity

        maxSum = float('-inf')
        i = 0
        totalSum = 0
        while i < len(nums):
            # If the sum of the subarray observed is negative and
            # if the next number is larger, we consider the next number
            # the start of a new subarray to consider.
            if totalSum < 0 and nums[i] > totalSum:
                totalSum = 0
            totalSum += nums[i]
            maxSum = max(maxSum, totalSum)
            i += 1
        return maxSum
