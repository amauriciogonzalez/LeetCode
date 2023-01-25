class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        pointDis = []
        for point in points:
            distance = abs(point[0]) ** 2 + abs(point[1]) ** 2
            pointDis.append([distance, point[0], point[1]])
        heapq.heapify(pointDis)
        result = []
        for i in range(k):
            dis, x, y = heapq.heappop(pointDis)
            result.append([x, y])
        return result