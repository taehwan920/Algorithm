import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        sample = list(set(words))
        repeats = []

        for s in sample:
            heapq.heappush(repeats, [-words.count(s), s])

        result = []
        for i in range(k):
            result.append(heapq.heappop(repeats)[1])

        return result
