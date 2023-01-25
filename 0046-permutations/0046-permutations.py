class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        def permuteR(permutation, index):
            if index == len(nums):
                results.append(permutation[:])
                return
            for i in range(index, len(nums)):
                permutation[index], permutation[i] = permutation[i], permutation[index]
                permuteR(permutation, index + 1)
                permutation[index], permutation[i] = permutation[i], permutation[index]
        permuteR(nums[:], 0)
        return results
