from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Budujemy graf
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # 2. Sortujemy malejąco, aby pop() dawał najmniejszy leksykograficznie
        for src in graph:
            graph[src].sort(reverse=True)
        
        # 3. Iteracyjny Hierholzer ze stosem
        stack = ["JFK"]
        result = []
        
        while stack:
            node = stack[-1]  # podglądamy wierzchołek stosu
            
            if graph[node]:  # jeśli są jeszcze krawędzie
                next_node = graph[node].pop()  # bierzemy najmniejszą
                stack.append(next_node)  # idziemy w głąb
            else:  # jeśli nie ma krawędzi
                result.append(stack.pop())  # dodajemy do wyniku i wracamy
        
        # 4. Odwracamy wynik
        return result[::-1]