class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        def combinationSum2R(index, combination, updatedTarget):
            
            if updatedTarget < 0:
                return
            if updatedTarget == 0:
                result.append(combination[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                combination.append(candidates[i])
                combinationSum2R(i+1, combination, updatedTarget - candidates[i])
                combination.pop()
        combinationSum2R(0, [], target)
        return result

"""
class Solution(object):
    def combinationSum2(self, candidates, target):
"""
"""
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
"""
"""
        candidates.sort()
        results = []
        def combinationSum2R(subset, index):
            if sum(subset) == target and subset not in results:
                results.append(subset[:])
                return
            elif index == len(candidates) or sum(subset) > target:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                combinationSum2R(subset, index + 1)
                subset.pop()
        combinationSum2R([], 0)
        return results
"""

        