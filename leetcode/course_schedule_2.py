class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        counts = [0 for i in range(n)]
        prevs = [[] for i in range(n)]

        for nex, pre in prerequisites:
            counts[nex] += 1
            prevs[pre].append(nex)

        q = []
        result = []
        for i in range(n):
            if counts[i] == 0:
                q.append(i)

        while q:
            now = q.pop(0)
            result.append(now)
            for nex in prevs[now]:
                counts[nex] -= 1
                if counts[nex] == 0:
                    q.append(nex)

        return result if len(result) == n else []
