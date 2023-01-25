class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) <= len(nums2):
            smallerList = nums1
            largerList = nums2
        else:
            smallerList = nums2
            largerList = nums1
        totalLength = len(smallerList) + len(largerList)
        half = totalLength // 2
        def binarySearch(i, j):
            print(i, j)
            midpoint = int(float(i + j) // 2)       # smallerListPointer
            p = half - midpoint - 2     # largerListPointer
            print(midpoint, p)
            smallerListLeft = smallerList[midpoint] if midpoint >= 0 else float("-infinity")
            smallerListRight = smallerList[midpoint+1] if midpoint+1 < len(smallerList) else float("infinity")
            largerListLeft = largerList[p] if p >= 0 else float("-infinity")
            largerListRight = largerList[p+1] if p+1 < len(largerList) else float("infinity")
            print(smallerList[0:midpoint+1], largerList[0:p+1])
            if smallerListLeft <= largerListRight and largerListLeft <= smallerListRight:
                if totalLength % 2 == 0:
                    return float(float(max(smallerListLeft, largerListLeft) + min(smallerListRight, largerListRight)) / 2)
                else:
                    return min(smallerListRight, largerListRight)
            elif largerListRight < smallerListLeft:
                return binarySearch(i, midpoint - 1)
            else:
                return binarySearch(midpoint + 1, j)
        return binarySearch(0, len(smallerList) - 1)