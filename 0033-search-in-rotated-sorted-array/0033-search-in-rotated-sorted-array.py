class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(i, j):
            if i > j:
                return -1 
            midpoint = int(float(i + j) / 2)
            midNum = nums[midpoint]
            if target == midNum:
                return midpoint
            elif (nums[0] <= target and target < midNum) or (target < midNum and midNum <= nums[-1]) or (nums[0] <= target and midNum <= nums[-1] and nums[0] > nums[-1]):
                return binarySearch(i, midpoint - 1)
            else:
                return binarySearch(midpoint + 1, j)
                
        return binarySearch(0, len(nums) - 1)