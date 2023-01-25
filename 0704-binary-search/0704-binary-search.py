class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(i, j):
            midpoint = int(float(i + j) / 2)
            if i > j:
                return -1
            else:
                if nums[midpoint] == target:
                    return midpoint
                elif nums[midpoint] < target:
                    return binarySearch(midpoint + 1, j)
                elif nums[midpoint] > target:
                    return binarySearch(i, midpoint - 1)
        return binarySearch(0, len(nums) - 1)