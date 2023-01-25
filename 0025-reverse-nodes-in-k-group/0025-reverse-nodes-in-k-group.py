# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prevHead = ListNode(0, head)
        prevGroup = prevHead
        while True:
            kthNode = self.getLastGroupNode(prevGroup, k)
            if not kthNode:
                break
            nextGroup = kthNode.next
            
            prev = nextGroup
            current = prevGroup.next
            while current != nextGroup:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            temp = prevGroup.next
            prevGroup.next = kthNode
            prevGroup = temp
        return prevHead.next


    
    def getLastGroupNode(self, node, k):
        while node and k > 0:
            node = node.next
            k = k - 1
        return node
