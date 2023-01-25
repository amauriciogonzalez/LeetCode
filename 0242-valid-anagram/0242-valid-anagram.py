class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = s.encode("ascii")
        t = t.encode("ascii")
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False