class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftMin = 0
        leftMax = 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin = max(0, leftMin - 1)
                leftMax -= 1
            else: # When c == "*"  
                leftMin = max(0, leftMin - 1)
                leftMax += 1
            if leftMax < 0:
                return False
        return leftMin == 0
        