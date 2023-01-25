class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def subsetsR(subset, index):
            result.append(subset[:])
            for i in range(index, len(nums)):
                subset.append(nums[i])
                subsetsR(subset, i+1)
                subset.pop()
        subsetsR([], 0)
        return result

        
            