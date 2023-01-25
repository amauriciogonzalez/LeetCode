class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            startingIndex = i
            while stack and stack[-1][0] > heights[i]:
                instance = stack.pop()
                maxArea = max(maxArea, instance[0] * (i - instance[1]))
                startingIndex = instance[1]
            stack.append([heights[i], startingIndex])
        for instance in stack:
            maxArea = max(maxArea, instance[0] * (len(heights) - instance[1]))
        return maxArea
