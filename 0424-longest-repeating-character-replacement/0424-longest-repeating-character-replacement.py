class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        charSet = {}
        maxLength = 0
        i = 0
        maxKeyValue = 0
        for j in range(len(s)):
            charSet[s[j]] = 1 + charSet.get(s[j], 0)
            maxKeyValue = max(maxKeyValue, charSet[s[j]])
            length = j - i + 1
            while (length - maxKeyValue) > k:
                charSet[s[i]] = charSet[s[i]] - 1
                i = i + 1
                length = j - i + 1
            maxLength = max(maxLength, length)
        return maxLength