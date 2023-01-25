# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.subtreeIsBalanced(root)
    
    def subtreeIsBalanced(self, node):
        if not node:
            return True
        return self.subtreeIsBalanced(node.left) and self.subtreeIsBalanced(node.right) and abs(self.maxDepth(node.left, 0) - self.maxDepth(node.right, 0)) <= 1

    def maxDepth(self, node, depth):
        if not node:
            return depth
        return max(self.maxDepth(node.left, depth+1), self.maxDepth(node.right, depth+1))