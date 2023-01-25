class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n^2) for taking every character and expanding it as a
        # string outward to find palindromes.
        result = ""
        for i in range(len(s)):
            # Checking odd length substrings
            left = i
            right = i
            while 0 <= left and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(result):
                    result = s[left : right + 1]
                left -= 1
                right += 1
            # Checking even length substrings
            left = i
            right = i + 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(result):
                    result = s[left : right + 1]
                left -= 1
                right += 1   
        return result