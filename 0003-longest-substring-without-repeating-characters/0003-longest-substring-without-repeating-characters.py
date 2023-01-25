class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        for i in range(len(s)):
            j = i
            substring = []
            length = 0
            while(True):
                substring.append(s[j])
                length = length + 1
                j = j + 1
                if j == len(s) or s[j] in substring:
                    break
            maxLength = max(length, maxLength)
        return maxLength