class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # we make all possible patterns and add them to hashMap
        # pattern will be keys and values are words that match it

        hashMap = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:] # pattern with one letter replaced with *
                hashMap[pattern].append(word)

        # now we have an adjacency list
        # we perform bfs to find shortest path to endWord in this

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbour in hashMap[pattern]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)
            res += 1
        return 0