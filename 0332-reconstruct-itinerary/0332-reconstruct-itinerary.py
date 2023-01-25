class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # O((V + E)^2)
        # O(E) memory

        adjacencyList = {fro : [] for fro, to in tickets}
        result = ["JFK"]
        tickets.sort()
        for fro, to in tickets:
            adjacencyList[fro].append(to)

        # A backtracking algorithm
        def dfs(fro):
            if len(result) == len(tickets) + 1:
                return True
            if fro not in adjacencyList:
                return False
            temp = list(adjacencyList[fro])
            print(temp)
            for toPlace in temp:
                print(toPlace)
                adjacencyList[fro].pop(0)
                result.append(toPlace)
                if dfs(toPlace):
                    return True
                adjacencyList[fro].append(toPlace)
                result.pop()
            return False

        dfs("JFK")
        return result

    
    