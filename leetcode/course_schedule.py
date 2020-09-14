class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        counts = [0 for i in range(n)]
        prevs = [[] for i in range(n)]

        for this, prev in prerequisites:
            counts[this] += 1
            prevs[prev].append(this)

        q = []
        result = 0
        for i in range(n):
            if counts[i] == 0:
                q.append(i)

        while q:
            now = q.pop(0)
            result += 1
            for next_l in prevs[now]:
                counts[next_l] -= 1
                if counts[next_l] == 0:
                    q.append(next_l)

        return True if result == n else False
