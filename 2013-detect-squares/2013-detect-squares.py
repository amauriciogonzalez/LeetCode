class DetectSquares(object):

    def __init__(self):
        self.pointsToCount = defaultdict(int)        
        self.points = []

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        # Lists are unhashable, so we use tuples.
        x, y = point
        self.pointsToCount[(x, y)] += 1
        self.points.append(point)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        result = 0
        # We loop through all points, treating these as diagonal points and testing if we have a square.
        for pt in self.points:
            # If we don't have a square, continue.
            if (abs(point[0] - pt[0]) != abs(point[1] - pt[1])) or point[0] == pt[0] or point[1] == pt[1]:
                continue
            # If we have a valid square diagonal point, multiply the occurances of the other two points.
            # (the final result will be 0 if there do not exist such point(s)).
            result += self.pointsToCount[(pt[0], point[1])] * self.pointsToCount[(point[0], pt[1])]
        return result
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)