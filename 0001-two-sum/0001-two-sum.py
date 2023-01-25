class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numTuples = []
        for i in range(len(nums)):
            numTuples.append([nums[i], i])
        numTuples.sort()
        i = 0
        j = len(nums) - 1
        for k in range(len(numTuples)):
            if numTuples[i][0] + numTuples[j][0] == target:
                return [numTuples[i][1], numTuples[j][1]]
            elif numTuples[i][0] + numTuples[j][0] < target:
                i = i + 1
            elif numTuples[i][0] + numTuples[j][0] > target:
                j = j - 1
        return [0, 0]
                
