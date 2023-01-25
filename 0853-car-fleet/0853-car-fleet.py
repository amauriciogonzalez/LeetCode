class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        numCarFleet = 0
        posSpeed = [[p, s] for p, s in zip(position, speed)]
        posSpeed.sort(reverse=True)
        #print(posSpeed)
        timeStack = []
        for element in posSpeed:
            timeStack.append(float(target - element[0]) / element[1])
            #print(element, timeStack)
            if len(timeStack) >= 2 and timeStack[-1] <= timeStack[-2]:
                timeStack.pop()
        return len(timeStack)
