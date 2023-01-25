class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The O(n) solution involves using a hashset.
        # We use the xor operator for a O(1) memory complexity solution.
        # Note that 0 ^ n = 0 and n ^ n = 0. 
        # This solution works because the xor operator cancels out the result
        # when operating on duplicate values, which there are an even number of.

        result = 0
        for n in nums:
            result = result ^ n
        return result