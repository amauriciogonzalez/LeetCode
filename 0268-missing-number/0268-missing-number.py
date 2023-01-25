class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Below are four O(n) time complexity answers.

        result = 0
        for i in range(len(nums)):
            result = result ^ (i + 1) ^ nums[i]
        return result

        """
        result = len(nums)
        for i in range(0, len(nums)):
            result += i - nums[i]
        return result
        """

        """
        return ((len(nums) * (len(nums) + 1)) // 2) - sum(nums)
        """

        """
        return sum(range(0, len(nums) + 1)) - sum(nums)
        """