class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        freqMap = []
        freq = 0
        sampledNum = nums[0]
        for i in range(len(nums)):
            if sampledNum == nums[i]:
                freq = freq + 1
            else:
                freqMap.append([sampledNum, freq])
                sampledNum = nums[i]
                freq = 1
        freqMap.append([sampledNum, freq])
        freqMap.sort(key = lambda x: x[1], reverse=True)
        result = []
        for i in range(len(freqMap)):
            if i < k:
                result.append(freqMap[i][0])
        return result
