class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        flat = [c for c in s if c.isalnum()]
        flatReversed = flat[:]
        flatReversed.reverse()
        if flat == flatReversed:
            return True
        else:
            return False