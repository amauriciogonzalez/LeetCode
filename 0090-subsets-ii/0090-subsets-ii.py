class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        def subsetsWithDupR(subset, index):
            results.append(subset[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                subsetsWithDupR(subset, i + 1)
                subset.pop()
        subsetsWithDupR([], 0)
        return results