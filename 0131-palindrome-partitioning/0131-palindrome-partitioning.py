class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        def isPalindrome(string, leftI, rightI):
            while leftI < rightI:
                if string[leftI] != string[rightI]:
                    return False
                leftI += 1
                rightI -= 1
            return True

        result = []

        def partitionR(partitionResult, index):
            if index == len(s):
                result.append(partitionResult[:])
                return
            for i in range(index, len(s)):
                # without this check, we return all possible partitions of string s.
                if isPalindrome(s, index, i):
                    partitionResult.append(s[index : i + 1])
                    partitionR(partitionResult, i + 1)
                    partitionResult.pop()

        partitionR([], 0)
        return result