class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        wordList.add(beginWord)

        graph = defaultdict(set)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                graph[pattern].add(word)
                        
        result = 0
        queue = deque([beginWord])
        visited = set([beginWord])

        while queue:

            result += 1
            lenght = len(queue)

            for _ in range(lenght):
                word = queue.popleft()

                if word == endWord:
                    return result

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    
                    for child in graph[pattern]:
                        if child not in visited:
                            queue.append(child)
                            visited.add(child)


        return 0
        
        
        
        
                        
        