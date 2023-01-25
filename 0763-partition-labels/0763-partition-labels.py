class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lastOccurances = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in lastOccurances:
                lastOccurances[s[i]] = i
        
        result = []
        currentSize = 0
        endOfPartition = 0
        for i in range(len(s)):
            currentSize += 1
            endOfPartition = max(endOfPartition, lastOccurances[s[i]])
            if i == endOfPartition:
                result.append(currentSize)
                currentSize = 0

        return result


