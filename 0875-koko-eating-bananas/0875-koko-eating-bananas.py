import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def eatBananas(eatingSpeed):
            hours = 0
            for p in piles:
                hours += int(math.ceil(float(p) / eatingSpeed))
            return hours

        def findMinEatingSpeed(i, j, result):
            if i > j:
                return result
            midpoint = int(float(i + j) / 2)
            hours = eatBananas(midpoint)
            if hours <= h:
                return findMinEatingSpeed(i, midpoint - 1, midpoint)
            else:
                return findMinEatingSpeed(midpoint + 1, j, result)
        
        return findMinEatingSpeed(1, max(piles), 0)