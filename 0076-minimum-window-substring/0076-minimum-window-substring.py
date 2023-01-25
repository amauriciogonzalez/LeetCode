class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def isSubset(set1, set2):
            for c in set1:
                if (set1.get(c, 0) > set2.get(c, 0)):
                    return False
            return True

        if len(t) > len(s):
            return ""

        tSet = {}
        windowSet = {}
        for k in range(len(t)):
            tSet[t[k]] = 1 + tSet.get(t[k], 0)
            windowSet[s[k]] = 1 + windowSet.get(s[k], 0)

        i = 0
        j = len(t)
        window = s[0:len(t)]
        smallestWindow = s + 'a'
        while (True):
            while(isSubset(tSet, windowSet)):
                if (len(window) < len(smallestWindow)):
                    smallestWindow = window
                window = window[1:]
                windowSet[s[i]] = windowSet[s[i]] - 1
                i = i + 1
            if j != len(s):
                window = window + s[j]
                windowSet[s[j]] = 1 + windowSet.get(s[j], 0)
                j = j + 1
            if j == len(s) and not isSubset(tSet, windowSet):
                window = s[i-1] + window
                break
        if smallestWindow == s + 'a':
            return ("")
        else:
            return smallestWindow