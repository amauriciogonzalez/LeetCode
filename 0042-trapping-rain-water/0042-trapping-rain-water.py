class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftMax = 0
        rightMax = 0
        result = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            if height[i] <= height[j]:
                if height[i] >= leftMax:
                    leftMax = height[i]
                else:
                    result = result + leftMax - height[i]
                i = i + 1
            else:
                if height[j] >= rightMax:
                    rightMax = height[j]
                else:
                    result = result + rightMax - height[j]
                j = j - 1
        return result