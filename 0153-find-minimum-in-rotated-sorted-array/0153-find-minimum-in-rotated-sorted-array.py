class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def search(i, j):
            if i + 1 == j or i == j:
                return min(nums[i], nums[j])
            midpoint = int(float(i + j) / 2)
            if nums[midpoint] <= nums[-1]:
                return search(i, midpoint)
            else:
                return search(midpoint + 1, j)
        return search(0, len(nums) - 1)