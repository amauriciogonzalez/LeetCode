class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Since we want to find the shortest path, we use BFS
        # O(n^2 * m)
        if endWord not in wordList:
            return 0
        patternToAdj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                patternToAdj[pattern].append(word)
        visited = set([beginWord])
        queue = [beginWord]
        result = 1

        # BFS
        while queue:
            for i in range(len(queue)):
                word = queue.pop(0)
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for adjWord in patternToAdj[pattern]:
                        if adjWord not in visited:
                            visited.add(adjWord)
                            queue.append(adjWord)
            result += 1
        return 0

        
