class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        heapq.heapify(hand)
        groups = [[] for _ in range(len(hand) // groupSize)]
        
        while hand:
            #print(groups)
            cardNum = heapq.heappop(hand)
            inserted = False
            for i in range(len(groups)):
                if not groups[i] or (len(groups[i]) < groupSize and cardNum == groups[i][-1] + 1):
                    inserted = True
                    groups[i].append(cardNum)
                    break
            if not inserted:
                return False
        return True

