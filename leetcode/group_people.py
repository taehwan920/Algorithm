class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        groups = [[] for i in range(n+1)]
        result = []
        for i in range(n):
            now = groupSizes[i]
            groups[now].append(i)
            if len(groups[now]) == now:
                result.append(groups[now])
                groups[now] = []

        return result
