# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorderDFS(node):
            if not node:
                return [None]
            leftList = [node.val] + preorderDFS(node.left)
            rightList = preorderDFS(node.right)
            return leftList + rightList

        return str(preorderDFS(root))


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.strip("][").split(", ")
        self.index = 0
        def dfs():
            if data[self.index] == 'None':
                self.index += 1
                return None
            node = TreeNode(int(data[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
                
       

        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))