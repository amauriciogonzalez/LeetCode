class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}

        def dfs(i, j):
            if i == len(s1) and j == len(s2) and i + j == len(s3):
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            cache[(i, j)] = False
            return False

        return dfs(0, 0)