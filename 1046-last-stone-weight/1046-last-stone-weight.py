class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-num for num in stones] # to make a max heap.
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2)
        stones.append(0)
        return abs(stones[0])
        

