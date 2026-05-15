class UnionFind:
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        self.count -= 1
        return True

    def getNumComponents(self) -> int:
        return self.count

