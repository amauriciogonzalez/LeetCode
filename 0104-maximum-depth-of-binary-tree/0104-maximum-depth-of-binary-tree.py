# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.calcDepth(root, 0)
    
    def calcDepth(self, node, depth):
        if node == None:
            return depth
        depth += 1
        return max(self.calcDepth(node.left, depth), self.calcDepth(node.right, depth))