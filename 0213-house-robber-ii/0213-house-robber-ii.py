class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[:-1]), self.robHelper(nums[1:]))

    def robHelper(self, nums):
        rob1 = 0
        rob2 = 0
        for n in nums:
            localBest = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = localBest
        return rob2