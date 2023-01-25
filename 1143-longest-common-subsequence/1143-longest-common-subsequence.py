class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # O(n * m) time and memory complexity
        # cache[i][j] = length of the longest common substring between
        # text1[i:] and text2[j:]

        #          a        c       e   
        # a (longestLen)                    0
        # b                                 0
        # c                                 0
        # d                                 0
        # e                                 0
        #          0        0       0   


        m = len(text1)
        n = len(text2)
        cache = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    cache[i][j] = cache[i + 1][j + 1] + 1
                else:
                    cache[i][j] = max(cache[i + 1][j], cache[i][j + 1])
        return cache[0][0]