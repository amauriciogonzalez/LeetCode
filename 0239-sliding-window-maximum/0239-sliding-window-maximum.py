class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections

        if (k == 1):
            return nums

        i = 0
        j = 1
        result = []
        deque = collections.deque()
        deque.append(nums[0])
        while j < len(nums):
            if nums[j] < deque[-1]:
                deque.append(nums[j])
            else:
                while deque and deque[-1] < nums[j]:
                    deque.pop()
                deque.append(nums[j])
            if j - i + 1 == k:
                result.append(deque[0])
                if (deque[0] == nums[i]):
                    deque.popleft()
            else:
                j = j + 1
                continue
            i = i + 1
            j = j + 1
        return result