class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^3) for n^2 subarrays and n iterations per subarray
        # cache[(l, r)] = max coins collected when the left-most and right-most elements in nums
        # are at l and r, respectively.

        cache = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]

            cache[(l, r)] = 0
            # We pop the i'th balloon last.
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(i + 1, r) + dfs(l, i - 1)
                cache[(l, r)] = max(cache[(l, r)], coins)
            return cache[(l, r)]
        
        return dfs(1, len(nums) - 2)

