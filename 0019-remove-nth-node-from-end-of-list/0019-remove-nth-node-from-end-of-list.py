# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        numNodes = 0
        while temp:
            numNodes += 1
            temp = temp.next
        if numNodes - n == 0:
            head = head.next
            return head
        else:
            temp = head
            iteration = 1
            while temp:
                if iteration == numNodes - n:
                    temp.next = temp.next.next
                    return head
                else:
                    temp = temp.next
                    iteration += 1
            return head