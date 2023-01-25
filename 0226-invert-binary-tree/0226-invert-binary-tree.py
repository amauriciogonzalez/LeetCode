# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.swapChildren(root)
        return root

    
    def swapChildren(self, node):
        if node == None:
            return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.swapChildren(node.left)
        self.swapChildren(node.right)