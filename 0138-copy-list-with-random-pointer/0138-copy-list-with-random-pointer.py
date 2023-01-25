"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToNewMap = {None: None}
        temp = head
        while temp:
            oldToNewMap[temp] = Node(temp.val)
            temp = temp.next
        temp1 = head
        while temp1:
            temp2 = oldToNewMap[temp1]
            temp2.random = oldToNewMap[temp1.random]
            temp2.next = oldToNewMap[temp1.next]
            temp1 = temp1.next
        return oldToNewMap[head]
