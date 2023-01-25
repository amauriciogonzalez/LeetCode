class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        numPalindromic = 0
        for i in range(len(s)):
            numPalindromic += self.countPalindromesFromSources(i, i, s)
            numPalindromic += self.countPalindromesFromSources(i, i + 1, s)
        return numPalindromic
    
    def countPalindromesFromSources(self, left, right, s):
        numPalindromic = 0
        while 0 <= left and right < len(s) and s[left] == s[right]:
                numPalindromic += 1
                left -= 1
                right += 1
        return numPalindromic
            