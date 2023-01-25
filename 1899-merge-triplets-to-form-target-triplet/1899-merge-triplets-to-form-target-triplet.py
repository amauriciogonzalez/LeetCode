class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        accpetableIndices = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    accpetableIndices.add(i)
                    
        if len(accpetableIndices) == 3:
            return True
        else:
            return False