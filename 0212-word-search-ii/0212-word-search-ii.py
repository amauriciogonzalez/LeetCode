class Node(object):
    def __init__(self, val=None):
        self.isEnd = False
        self.val = val
        self.children = {}
class Trie(object):
    def __init__(self):
        self.blankRoot = Node() 
    def insert(self, word):
        def traverse(node, index):
            if index == len(word):
                node.isEnd = True
                return
            for children in node.children:
                if children == word[index]:
                    return traverse(node.children[children], index+1)
            node.children[word[index]] = Node(word[index])
            return traverse(node.children[word[index]], index+1)
        return traverse(self.blankRoot, 0)
    def search(self, word):
        def searchR(node, index):
            if index == len(word):
                if node.isEnd:
                    return True
                else:
                    return False
            for children in node.children:
                if children.val == word[index]:
                    return searchR(children, index+1)
            return False
        return searchR(self.blankRoot, 0)

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ROWS, COLS = len(board), len(board[0])
        results = []
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(r, c, node, word):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                board[r][c] == " " or board[r][c] not in node.children):
                return
            temp_char = board[r][c]
            board[r][c] = " "
            node = node.children[temp_char]
            word += temp_char
            
            if node.isEnd:
                results.append(word)
                node.isEnd = False
            
            if not node.children:
                del node
            else:
                dfs(r + 1, c, node, word)
                dfs(r - 1, c, node, word)
                dfs(r, c + 1, node, word)
                dfs(r, c - 1, node, word)
            
            board[r][c] = temp_char
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.blankRoot, "")
        return results


        