# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # We use preorder traversal or DFS to solve (we process each node before moving on to
        # the left and right subtrees.

        def dfs(node, maxNum):
            if not node:
                return 0
            numGoodNodes = 0
            if node.val >= maxNum:
                numGoodNodes = 1
            numGoodNodes += dfs(node.left, max(maxNum, node.val))
            numGoodNodes += dfs(node.right, max(maxNum, node.val))
            return numGoodNodes
        
        return dfs(root, root.val)
            