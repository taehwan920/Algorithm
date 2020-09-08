import itertools


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = 0

        for i in range(1, len(tiles) + 1):
            temp = list(itertools.permutations(tiles, i))
            cnt += len(list(set(temp)))

        return cnt
