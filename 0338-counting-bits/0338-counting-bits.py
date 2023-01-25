class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # In counting the number of bits in a number, we mod the number by 2 and divide it
        # by 2 in each iteration. This is O(log2(n)) time complexity. Doing this for each number i
        # where 0 <= i <= n yields O(nlog(n)) time complexity.
        # Drawing out the bit mappings for each number, you can see that there is a lot of
        # repeated patterns between every iteration and that iteration number minus the integer
        # representation of the location of the most significant bit. Therefore, we may use
        # dynamic programming to solve this problem (1 + cache[n - most significant bit]).

        cache = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            cache[i] = 1 + cache[i - offset]
        return cache
