class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = nums[:]
        result[0] = 1
        result[-1] = 1
        product = 1
        for i in range(1, len(nums)):
            product = product * nums[i - 1]
            result[i] = product
        print(result)
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product = product * nums[i + 1]
            result[i] = result[i] * product
        print(result)
        return result