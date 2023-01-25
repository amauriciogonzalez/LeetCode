# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        temp1 = head
        temp2 = head.next
        while temp2 and temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next.next
        secondHalf = temp1.next
        prev = None
        temp1.next = None
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp
        firstHalf = head
        secondHalfReversed = prev
        while secondHalfReversed:
            temp = firstHalf.next
            firstHalf.next = secondHalfReversed
            firstHalf = temp
            temp = secondHalfReversed.next
            secondHalfReversed.next = firstHalf
            secondHalfReversed = temp