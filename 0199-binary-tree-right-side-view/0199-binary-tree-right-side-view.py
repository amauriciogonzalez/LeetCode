# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Solving using level order traversal (or breadth first search)
        if not root:
            return []
        queue = [root]
        levels = []
        while queue:
            nextQueue = []
            level = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            levels.append(level[-1])
            queue = nextQueue
        return levels