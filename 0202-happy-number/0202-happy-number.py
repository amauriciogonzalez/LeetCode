class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # We can solve this with a hashset to check if we have a repeated value, making
        # our solution O(n) memory. Here, we use a linked list cycle detection algorithm below for
        # a O(1) memory solution. 

        slow = n
        fast = self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)
        if slow == 1:
            return True
        else:
            return False

    
    def sumSquareDigits(self, n):
        total = 0
        while n != 0:
            total += (n % 10) ** 2
            n = n // 10
        return total    

    # Alternatively,
    """
    def sumSquareDigits(self, n):
        total = 0
        n = list(str(n))
        for c in n:
            total += int(c) ** 2
        return total
    """