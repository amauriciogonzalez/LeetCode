class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(32) ~ O(1) Time complexity solution. 

        result = 0
        # We loop through the bits of the number.
        while n > 0:
            # We add the rightmost bit to the result.
            result += n & 1 # equivalent to result += n % 2
            # Then we shift right to check the next rightmost bit in the
            # next iteration.
            n = n >> 1
        return result
        