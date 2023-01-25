# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prevHead = ListNode()
        temp = prevHead
        carry = 0
        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            digitSum = digit1 + digit2 + carry
            digitResult = digitSum % 10
            carry = digitSum // 10
            temp.next = ListNode(digitResult)

            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prevHead.next
