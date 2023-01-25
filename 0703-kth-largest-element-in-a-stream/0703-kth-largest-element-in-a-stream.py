class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            # Pop and return the smallest item from the heap
            # until the length of the heap is k.
            heapq.heappop(self.nums)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            # Pop and return the smallest item from the heap
            # until the length of the heap is k.
            heapq.heappop(self.nums)
        return self.nums[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)