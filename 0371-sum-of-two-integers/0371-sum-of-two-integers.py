class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def add(a, b):
            while b != 0:
                temp = (a & b) << 1
                a = a ^ b
                b = temp
            return a

        # if one of a or b is negative...
        if a * b < 0:
            # if a is positive, enter this method again with a and b swapped.
            if a > 0: 
                return self.getSum(b, a)
            # otherwise, if the complement (negative) of a is equivalent to b,
            # then a + b = 0.
            if add(~a, 1) == b:
                return 0
            # otherwise, if -a < b, then take the complment of a and b, add them
            # together, then take the complement of their sum. (-add(-a, -b))
            if add(~a, 1) < b:  
                return add(~add(add(~a, 1), add(1, ~b)), 1) 
        
        # We return here if a * b >= 0 or if -a > b > 0
        return add(a, b)  


        # This solution below does not work in Python for negative numbers.
        """
        while b != 0:
            temp = (a & b) << 1
            a = a ^ b
            b = temp
        return a
        """