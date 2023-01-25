# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeSet = set()
        temp = head
        while temp:
            if temp in nodeSet:
                return True
            else:
                nodeSet.add(temp)
            temp = temp.next
        return False