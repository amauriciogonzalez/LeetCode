class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Set = {}
        charSet = {}
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1Set[s1[i]] = 1 + s1Set.get(s1[i], 0)
            charSet[s2[i]] = 1 + charSet.get(s2[i], 0)

        i = 0
        j = len(s1)
        while (True):
            if (charSet == s1Set):
                return True
            if (j >= len(s2)):
                break
            charSet[s2[j]] = 1 + charSet.get(s2[j], 0)
            j = j + 1
            charSet[s2[i]] = charSet.get(s2[i], 0) - 1
            if charSet[s2[i]] == 0:
                charSet.pop(s2[i])
            i = i + 1
        return False