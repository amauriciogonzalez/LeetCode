class Node(object):
    def __init__(self, val=None):
        self.isEnd = False
        self.val = val
        self.children = []

class Trie(object):

    def __init__(self):
        self.blankRoot = Node()
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        def traverse(node, index):
            if index == len(word):
                node.isEnd = True
                return
            for child in node.children:
                if child.val == word[index]:
                    return traverse(child, index+1)
            node.children.append(Node(word[index]))
            return traverse(node.children[-1], index+1)
        return traverse(self.blankRoot, 0)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def searchR(node, index):
            if index == len(word):
                if node.isEnd:
                    return True
                else:
                    return False
            for child in node.children:
                if child.val == word[index]:
                    return searchR(child, index+1)
            return False
        return searchR(self.blankRoot, 0)
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        def startsWithR(node, index):
            if index == len(prefix):
                return True
            for child in node.children:
                if child.val == prefix[index]:
                    return startsWithR(child, index+1)
            return False
        return startsWithR(self.blankRoot, 0)
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)