class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or not beginWord or not endWord:
            return 0

        memory = {}
        for word in wordList:
            for i, e in enumerate(word):
                key = word[:i] + '$' + word[i+1:]
                if not memory.get(key):
                    memory[key] = []
                memory[key].append(word)

        parents = {beginWord: None}
        frontier = [beginWord]
        levels = 1

        while frontier:
            _next = []
            for word in frontier:
                neighbors = []
                for i, e in enumerate(word):
                    key = word[:i] + '$' + word[i+1:]
                    if key in memory:
                        neighbors += memory[key]

                for neighbor in neighbors:
                    if neighbor == endWord:
                        return levels + 1

                    if neighbor not in parents:
                        parents[neighbor] = word
                        _next.append(neighbor)

            frontier = _next
            levels += 1

        return 0
