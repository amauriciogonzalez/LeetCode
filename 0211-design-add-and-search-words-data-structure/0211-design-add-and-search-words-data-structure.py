class Node(object):
    def __init__(self, val = None):
        self.isEnd = False
        self.val = val
        self.children = []

class WordDictionary(object):

    def __init__(self):
        self.blankRoot = Node()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        def addWordR(node, index):
            if index == len(word):
                node.isEnd = True
                return
            for child in node.children:
                if child.val == word[index]:
                    return addWordR(child, index+1)
            node.children.append(Node(word[index]))
            return addWordR(node.children[-1], index+1)
        return addWordR(self.blankRoot, 0)

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
            if word[index] == '.':
                for child in node.children:
                    # This if statement is necessary. We only want to return True
                    # only when we return true.
                    if searchR(child, index+1): 
                        return True
            else:
                for child in node.children:
                    if child.val == word[index]:
                        return searchR(child, index+1)
            return False
        return searchR(self.blankRoot, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)