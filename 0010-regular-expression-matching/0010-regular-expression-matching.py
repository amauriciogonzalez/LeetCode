class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # cache[(i, j)] = Does p[j:] match the string s[i:]?
        cache = {}

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            if (i, j) in cache:
                return cache[(i, j)]
            
            matchingChar = (i < len(s)) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                matchingNotUsingStar = dfs(i, j + 2)
                matchingUsingStar = matchingChar and dfs(i + 1, j)
                cache[(i, j)] = matchingNotUsingStar or matchingUsingStar
                return cache[(i, j)]
            if matchingChar:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return  cache[(i, j)] 
                
            cache[(i, j)] = False
            return cache[(i, j)] # When there is no star and the characters do not match.
        
        return dfs(0, 0)
            
