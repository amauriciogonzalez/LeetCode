class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacencyList = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjacencyList[course].append(prereq)
        # Courses on the current path will be marked via a -1, finished courses are marked via 1.
        visited = [0 for i in range(numCourses)]
        result = []
        def dfs(course):
            if visited[course] == -1:
                return False
            elif visited[course] == 1:
                return True
            visited[course] = -1
            for prereq in adjacencyList[course]:
                if dfs(prereq) == False:
                    return False
            visited[course] = 1
            result.append(course)
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return result
            
            
            
        