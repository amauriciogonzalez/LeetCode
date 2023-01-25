class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strsIndexed = []
        for i in range(len(strs)):
            strsIndexed.append([sorted(strs[i]), i])
        strsIndexed.sort()
        result = []
        instancedResult = []
        startingIndex = 0
        for i in range(len(strsIndexed)):
            if strsIndexed[startingIndex][0] == strsIndexed[i][0]:
                instancedResult.append(strs[strsIndexed[i][1]])
            else:
                startingIndex = i
                result.append(instancedResult)
                instancedResult = []
                instancedResult.append(strs[strsIndexed[startingIndex][1]])
        result.append(instancedResult)
        return result