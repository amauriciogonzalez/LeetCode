# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.calcDiameter(root, 0)

    def calcDiameter(self, node, diameter):
        if node == None:
            return diameter
        diameter = max(self.maxDepth(node.left, 1) + self.maxDepth(node.right, 1) - 2, diameter)
        return max(self.calcDiameter(node.left, diameter), self.calcDiameter(node.right, diameter), diameter)

    def maxDepth(self, node, depth):
        return max(self.maxDepth(node.left, depth+1), self.maxDepth(node.right, depth+1)) if node else depth