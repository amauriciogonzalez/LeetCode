# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if self.isIdentical(root, subRoot):
            return True
        elif root == None and subRoot != None:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isIdentical(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right)
        else:
            return False
