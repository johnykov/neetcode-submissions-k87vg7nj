class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))

        pq = [(0,k)]
        visit = set()
        t = 0

        while pq:
            w1, n1 = heapq.heappop(pq)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for nei, nei_w in adj[n1]:
                if nei not in visit:
                    heapq.heappush(pq, (w1+nei_w, nei))
        return t if len(visit) == n else -1