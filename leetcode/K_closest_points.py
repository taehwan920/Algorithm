from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        _points = list(
            map(lambda x: [sqrt(x[0] ** 2 + x[1] ** 2), x[0], x[1]], points))
        _p = sorted(_points, key=lambda x: x[0])

        result = []
        for i in range(K):
            result.append(_p.pop(0)[1:])
        return result
