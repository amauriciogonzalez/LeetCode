class MedianFinder(object):

    def __init__(self):
        self.maxHeap = [] # left half
        self.minHeap = [] # right half
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, num * -1)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            n = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, n * -1)
        elif len(self.maxHeap) + 1 < len(self.minHeap):
            n = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, n * -1)
        
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0:
            return float((-1 * self.maxHeap[0]) + (self.minHeap[0])) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        else:
            return self.minHeap[0]


        
        
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()