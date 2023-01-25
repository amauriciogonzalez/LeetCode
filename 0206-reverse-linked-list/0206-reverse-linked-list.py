# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp2 = None
        prev = None
        temp1 = head
        while temp1:
            temp2 = temp1.next
            temp1.next = prev
            prev = temp1
            temp1 = temp2
        return prev
