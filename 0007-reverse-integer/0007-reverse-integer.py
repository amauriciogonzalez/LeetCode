class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # O(n) and O(1) time and memory complexity solution respectively.

        maximum = (2 ** 31) - 1
        minimum = -2 ** 31
        result = 0
        isNegative = False
        if x < 0:
            x = -x
            isNegative = True
        while x > 0:
            digit = x % 10
            x = x // 10   
            print(result, digit)
            
            # If we are out of bounds, return 0.
            if result > maximum // 10 or (result == maximum // 10 and digit > maximum % 10):
                return 0
            if result < minimum // 10 or (result == minimum // 10 and digit < minimum % 10):
                return 0
            
            result = (result * 10) + digit
        if isNegative:
            return result * -1
        else:
            return result


        # O(n) time and memory complexity solution.

        """
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        s = str(x)
        s = s[::-1]
        x = int(s)
        if isNegative:
            x = -1 * x
        if -2 ** 31 <= x <= (2 ** 31) - 1:
            return x
        else:
            return 0
        """