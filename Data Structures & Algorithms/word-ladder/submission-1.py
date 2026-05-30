class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = list(set(wordList + [beginWord]))
        graph = defaultdict(list)

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if sum([a != b for a,b in zip(wordList[i], wordList[j])]) == 1:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        visit = {beginWord}
        q = deque([(beginWord, 1)])
        reached_end = False

        while q:
            node, length = q.popleft()
            if node == endWord:
                return length
            
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append((nei, length + 1))

        return 0