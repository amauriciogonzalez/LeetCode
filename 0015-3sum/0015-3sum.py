class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        i = 0
        while i <= len(nums) - 3 and nums[i] <= 0:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                result = nums[i] + nums[j] + nums[k]
                if result > 0:
                    k = k - 1
                elif result < 0:
                    j = j + 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    temp = nums[j]
                    j = j + 1
                    while(j <= len(nums) - 2 and temp == nums[j]):
                        j = j + 1
            temp = nums[i]
            i = i + 1
            while(i <= len(nums) - 3 and temp == nums[i]):
                i = i + 1
        return triplets