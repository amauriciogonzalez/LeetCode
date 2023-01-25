class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
            if (height[i] <= height[j]):
                i = i + 1
            else:
                j = j - 1
        return maxArea