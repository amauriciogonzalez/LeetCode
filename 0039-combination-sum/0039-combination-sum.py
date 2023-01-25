class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def combinationSumR(combination, index, updatedTarget):
            if updatedTarget == 0:
                result.append(combination[:])
                return
            elif updatedTarget < 0:
                return
            for i in range(index, len(candidates)):
                combination.append(candidates[i])
                # not i + 1 since we want to reuse the same elements
                combinationSumR(combination, i, updatedTarget - candidates[i])
                combination.pop()
        combinationSumR([], 0, target)
        return result