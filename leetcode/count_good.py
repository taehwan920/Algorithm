import itertools


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def is_good(item):
            temp = [False, False, False]
            if abs(item[0] - item[1]) <= a:
                temp[0] = True
            if abs(item[1] - item[2]) <= b:
                temp[1] = True
            if abs(item[0] - item[2]) <= c:
                temp[2] = True
            return all(temp)

        cnt = 0

        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    temp = [arr[i], arr[j], arr[k]]
                    if is_good(temp):
                        cnt += 1

        return cnt
