# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def preorder(node, leftBoundary, rightBoundary):
            if not node:
                return True
            if not leftBoundary < node.val:
                return False
            if not rightBoundary > node.val:
                return False
            leftValidation = preorder(node.left, leftBoundary, node.val)
            rightValidation = preorder(node.right, node.val, rightBoundary)
            return leftValidation and rightValidation
        return preorder(root, float("-inf"), float("inf"))
                