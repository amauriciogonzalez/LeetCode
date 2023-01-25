class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # For every element, we have a choice to add it to one array or another. Thus,
        # The brute force solution is of time complexity O(2^n).

        # When caching below, we have time complecity O(n * sum(nums)/2) ~ O(n * sum(nums))
        # and memory complexity O(sum(nums))

        total = sum(nums)
        if total % 2 == 1:
            # in this case, we are unable to have equal
            # sums of two subsets.
            return False
    
        target = total // 2
        # Holds possible targets created via the input array.
        dp = set()
        dp.add(0)
        
        for i in range(len(nums) - 1, -1, -1):
            # We use nextDP since we cannot update the set dp while in the next for loop.
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

