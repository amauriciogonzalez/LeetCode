class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # O(1) time complexity solution. We shift left i to find the i'th bit
        # and add it (via an OR operation) to i'th to last place of result's bit map
        # by shifting the bit left 31 - i times.

        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))
        return result