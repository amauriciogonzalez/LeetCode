class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # For this problem, we use Union-Find, or a disjoint-set
        # data structure, which storsa collection of disjoint sets.
        parent = [i for i in range(len(edges) + 1)] # stores parent vertex for each set
        rank = [1] * (len(edges) + 1)                # stores the size of each set

        # Find the parent / root of vertex u.
        def find(u):
            p = parent[u]
            while p != parent[p]:
                parent[p] = parent[parent[p]] # shortens the link of parents (path compression)
                p = parent[p]
            return p
        
        # Unify two vertices while maintaining the disjoint set properties.
        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                # We cannot unify if they have the same parent,
                # we have a redundant connection.
                return False
            if rank[p1] > rank[p2]:
                # p1 is now the parent of p2.
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                # p2 is now the parent of p1.
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for u, v in edges:
            if union(u, v) == False:
                return [u, v]
        