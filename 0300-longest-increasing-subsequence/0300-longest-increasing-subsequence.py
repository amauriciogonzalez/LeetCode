class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute force time complexity is O(2^n) since there are
        # two choices for every number, which is to include it or not.

        # With caching, longIncSub[index to start a subsequence] = longest increasing
        # subsequence from the index.
        # So longIncSub[len(nums) - 1] = 1 always.
        # Time O(n^2)
        
        longIncSub = [1 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # If the subsequence is increasing...
                if nums[i] < nums[j]:
                    longIncSub[i] = max(longIncSub[i], 1 + longIncSub[j])
        return max(longIncSub)