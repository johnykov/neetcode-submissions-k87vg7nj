class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        visit = set()
        visiting = set()
        topSort = []

        def dfs(crs):
            if crs in visit:
                return True
            if crs in visiting:
                return False
            visiting.add(crs)

            for neighbor in adj[crs]:
                if not dfs(neighbor):
                    return False
            visiting.remove(crs)
            visit.add(crs)
            topSort.append(crs)
            return True

        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        
        return topSort