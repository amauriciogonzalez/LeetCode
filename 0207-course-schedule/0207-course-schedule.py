class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # We check if we have a cycle, so we use DFS.
        # We use a hashmap to represent an adjacency list.
        adjacencyList = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjacencyList[course].append(prereq)
        # The visited map stores all courses on the current DFS path.
        visitedSet = set()
        # Checks if we have a cycle.
        def dfs(course):
            if course in visitedSet:
                return False
            elif adjacencyList[course] == []:
                return True
            visitedSet.add(course)
            for prereq in adjacencyList[course]:
                if not dfs(prereq):
                    return False
            visitedSet.remove(course)
            adjacencyList[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True