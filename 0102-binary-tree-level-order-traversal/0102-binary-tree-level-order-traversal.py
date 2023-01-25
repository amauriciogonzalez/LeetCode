# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # We implement breadth first search
        # BFS(root node)
        # {
        #   create queue
        #   create list of visited nodes
        #   mark root node as visited
        #   enqueue root node
        #   while (queue is not empty)
        #   {
        #       x = queue.top()
        #       queue.pop()
        #       for (all immediate neighbors of x)
        #       {
        #           if (not visited)
        #           {
        #               enqueue
        #               mark as visited
        #           }
        #       }
        #   }
        # }
        
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
            levels.append(level)
            queue = nextQueue
        return levels

        



        
