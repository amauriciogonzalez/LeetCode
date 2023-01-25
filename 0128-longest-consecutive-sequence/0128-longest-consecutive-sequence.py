class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        maxLength = 0
        for num in numSet:
            if num + 1 not in numSet:
                length = 1
                observedNum = num
                while observedNum - 1 in numSet:
                    length = length + 1
                    observedNum = observedNum - 1
                maxLength = max(length, maxLength) 
        return maxLength