class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -1 * n
            x = 1 / x
        if n == 1:
            return x
        if n == 0:
            return 1
        if n % 2 == 1:
            part = self.myPow(x, (n-1) // 2)
            return part * x * part
        else:
            part = self.myPow(x, n // 2)
            return part * part
        
