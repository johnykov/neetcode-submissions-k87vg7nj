class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        components = n
        #print(parent)
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x,y = find(x), find(y)
            if x == y: 
                return False
            parent[x] = y
            return True
            

        for u,v in edges:
            if union(u,v):
                components -= 1

        
        return components
        