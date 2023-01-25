class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time complexity O(n * abs(abs(nums) - abs(-nums)))
        cache = {} # {(index, sum), ...}

        def findR(i, sumNums):
            if i == len(nums):
                if sumNums == target:
                    return 1
                else:
                    return 0
            if (i, sumNums) in cache:
                return cache[(i, sumNums)]
            
            cache[(i, sumNums)] = findR(i + 1, sumNums + nums[i]) + findR(i + 1, sumNums + (-1*nums[i]))
            return cache[(i, sumNums)]
        
        return findR(0, 0)