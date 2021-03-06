import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        chrs = list(set(s))
        cnt = {}

        for c in chrs:
            cnt[c] = s.count(c)

        items = list(cnt.items())
        items = sorted(items, key=lambda x: x[1], reverse=True)
        result = ""

        for item in items:
            result += item[1] * item[0]

        return result

# 힙 이용


class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        chrs = list(set(s))
        cnt = []

        for c in chrs:
            heapq.heappush(cnt, (-s.count(c), c))

        result = ''
        while cnt:
            num, c = heapq.heappop(cnt)
            result += c * -num
        return result
