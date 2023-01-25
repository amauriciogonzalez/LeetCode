# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # The array makes the variable, result, global.
        result = [root.val]

        def dfs(node):
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            splitPath = leftMax + node.val + rightMax
            result[0] = max(result[0], splitPath)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return result[0]